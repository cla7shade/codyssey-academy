import pytest
from unittest.mock import patch

from quiz import Quiz
from quiz_state import QuizState
from quiz_game import QuizGame


@pytest.fixture
def game(tmp_path):
    """임시 state 파일을 사용하는 QuizGame 인스턴스."""
    return QuizGame(str(tmp_path / 'state.json'))


class TestInputInt:
    def test_valid_input_returns_int(self, game):
        with patch('builtins.input', return_value='3'):
            assert game._input_int('선택: ', 1, 5) == 3

    def test_retries_on_empty_input(self, game):
        with patch('builtins.input', side_effect=['', '2']):
            assert game._input_int('선택: ', 1, 5) == 2

    def test_retries_on_non_integer(self, game):
        with patch('builtins.input', side_effect=['abc', '4']):
            assert game._input_int('선택: ', 1, 5) == 4

    def test_retries_on_below_range(self, game):
        with patch('builtins.input', side_effect=['0', '1']):
            assert game._input_int('선택: ', 1, 5) == 1

    def test_retries_on_above_range(self, game):
        with patch('builtins.input', side_effect=['6', '5']):
            assert game._input_int('선택: ', 1, 5) == 5

    def test_boundary_min_accepted(self, game):
        with patch('builtins.input', return_value='1'):
            assert game._input_int('선택: ', 1, 5) == 1

    def test_boundary_max_accepted(self, game):
        with patch('builtins.input', return_value='5'):
            assert game._input_int('선택: ', 1, 5) == 5

    def test_whitespace_around_number_accepted(self, game):
        with patch('builtins.input', return_value=' 3 '):
            assert game._input_int('선택: ', 1, 5) == 3


class TestPlayQuiz:
    def test_no_quizzes_prints_message(self, game, capsys):
        game.state.quizzes = []
        game._play_quiz()
        assert '등록된 퀴즈가 없습니다' in capsys.readouterr().out

    def test_all_correct_sets_best_score(self, game):
        game.state.quizzes = [Quiz('Q1', ['A', 'B', 'C', 'D'], 1)]
        game.state.best_score = -1

        with patch('builtins.input', return_value='1'):
            game._play_quiz()

        assert game.state.best_score == 100

    def test_all_wrong_score_is_zero(self, game):
        game.state.quizzes = [Quiz('Q1', ['A', 'B', 'C', 'D'], 1)]
        game.state.best_score = -1

        with patch('builtins.input', return_value='2'):
            game._play_quiz()

        assert game.state.best_score == 0

    def test_best_score_not_updated_when_lower(self, game):
        game.state.quizzes = [Quiz('Q1', ['A', 'B', 'C', 'D'], 1)]
        game.state.best_score = 100

        with patch('builtins.input', return_value='2'):
            game._play_quiz()

        assert game.state.best_score == 100

    def test_partial_correct_score(self, game):
        game.state.quizzes = [
            Quiz('Q1', ['A', 'B', 'C', 'D'], 1),
            Quiz('Q2', ['A', 'B', 'C', 'D'], 2),
        ]
        game.state.best_score = -1

        # Q1 정답(1), Q2 오답(1)
        with patch('builtins.input', side_effect=['1', '1']):
            game._play_quiz()

        assert game.state.best_score == 50


class TestPlayQuizMessages:
    def test_correct_answer_prints_message(self, game, capsys):
        game.state.quizzes = [Quiz('Q1', ['A', 'B', 'C', 'D'], 1)]
        with patch('builtins.input', return_value='1'):
            game._play_quiz()
        assert '정답' in capsys.readouterr().out

    def test_wrong_answer_prints_correct_answer(self, game, capsys):
        game.state.quizzes = [Quiz('Q1', ['A', 'B', 'C', 'D'], 1)]
        with patch('builtins.input', return_value='2'):
            game._play_quiz()
        output = capsys.readouterr().out
        assert '오답' in output
        assert '1' in output  # 정답 번호 안내


class TestAddQuiz:
    def test_adds_quiz_to_state(self, game):
        initial_count = len(game.state.quizzes)
        inputs = ['새 질문', '선택1', '선택2', '선택3', '선택4', '2']

        with patch('builtins.input', side_effect=inputs):
            game._add_quiz()

        assert len(game.state.quizzes) == initial_count + 1
        added = game.state.quizzes[-1]
        assert added.question == '새 질문'
        assert added.answer == 2

    def test_empty_question_returns_without_adding(self, game):
        initial_count = len(game.state.quizzes)

        with patch('builtins.input', return_value=''):
            game._add_quiz()

        assert len(game.state.quizzes) == initial_count

    def test_retries_on_empty_choice(self, game):
        # 선택지 2번에서 빈 값 후 재입력
        inputs = ['질문', '선택1', '', '선택2', '선택3', '선택4', '1']

        with patch('builtins.input', side_effect=inputs):
            game._add_quiz()

        added = game.state.quizzes[-1]
        assert added.choices == ['선택1', '선택2', '선택3', '선택4']


class TestPrintMenu:
    def test_menu_contains_all_options(self, game, capsys):
        game._print_menu()
        output = capsys.readouterr().out
        assert '퀴즈 풀기' in output
        assert '퀴즈 추가' in output
        assert '퀴즈 목록' in output
        assert '점수 확인' in output
        assert '종료' in output


class TestRunInterrupts:
    def test_keyboard_interrupt_saves_and_exits(self, game):
        with patch.object(game, '_print_menu', side_effect=KeyboardInterrupt):
            with patch.object(game.state, 'save_state') as mock_save:
                game.run()
                mock_save.assert_called_once()

    def test_eof_error_saves_and_exits(self, game):
        with patch.object(game, '_print_menu', side_effect=EOFError):
            with patch.object(game.state, 'save_state') as mock_save:
                game.run()
                mock_save.assert_called_once()


class TestListQuizzes:
    def test_no_quizzes_prints_message(self, game, capsys):
        game.state.quizzes = []
        game._list_quizzes()
        assert '등록된 퀴즈가 없습니다' in capsys.readouterr().out

    def test_lists_all_quizzes(self, game, capsys):
        game.state.quizzes = [
            Quiz('첫 번째 질문', ['A', 'B', 'C', 'D'], 1),
            Quiz('두 번째 질문', ['A', 'B', 'C', 'D'], 2),
        ]
        game._list_quizzes()
        output = capsys.readouterr().out
        assert '첫 번째 질문' in output
        assert '두 번째 질문' in output


class TestShowScore:
    def test_no_score_yet(self, game, capsys):
        game.state.best_score = -1
        game._show_score()
        assert '아직 퀴즈를 풀지 않았습니다' in capsys.readouterr().out

    def test_shows_best_score(self, game, capsys):
        game.state.best_score = 80
        game._show_score()
        assert '80' in capsys.readouterr().out
