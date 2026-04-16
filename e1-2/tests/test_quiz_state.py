import json
import pytest

from quiz import Quiz
from quiz_state import QuizState, DEFAULT_QUIZZES


class TestDefaultQuizzes:
    def test_default_quizzes_count(self):
        assert len(DEFAULT_QUIZZES) >= 5

    def test_default_quizzes_have_four_choices(self):
        for quiz in DEFAULT_QUIZZES:
            assert len(quiz.choices) == 4

    def test_default_quizzes_answer_in_range(self):
        for quiz in DEFAULT_QUIZZES:
            assert 1 <= quiz.answer <= 4


class TestQuizStateInit:
    def test_loads_defaults_when_file_missing(self, tmp_path):
        state = QuizState(str(tmp_path / 'nonexistent.json'))
        assert state.quizzes == list(DEFAULT_QUIZZES)
        assert state.best_score == -1

    def test_loads_from_existing_file(self, tmp_path):
        data = {
            'quizzes': [{'question': 'Q1', 'choices': ['A', 'B'], 'answer': 1}],
            'best_score': 80,
        }
        state_file = tmp_path / 'state.json'
        state_file.write_text(json.dumps(data), encoding='utf-8')

        state = QuizState(str(state_file))
        assert len(state.quizzes) == 1
        assert state.quizzes[0].question == 'Q1'
        assert state.best_score == 80

    def test_falls_back_to_defaults_on_corrupt_json(self, tmp_path):
        state_file = tmp_path / 'state.json'
        state_file.write_text('{ not valid json', encoding='utf-8')

        state = QuizState(str(state_file))
        assert state.quizzes == list(DEFAULT_QUIZZES)
        assert state.best_score == -1


class TestQuizStateScore:
    def test_get_best_score_initial(self, tmp_path):
        state = QuizState(str(tmp_path / 'state.json'))
        assert state.get_best_score() == -1

    def test_get_best_score_after_update(self, tmp_path):
        state = QuizState(str(tmp_path / 'state.json'))
        state.best_score = 60
        assert state.get_best_score() == 60


class TestQuizStateAddQuiz:
    def test_add_quiz_appends(self, tmp_path):
        state = QuizState(str(tmp_path / 'state.json'))
        initial_count = len(state.quizzes)

        state.add_quiz('새 질문', ['A', 'B', 'C', 'D'], 3)

        assert len(state.quizzes) == initial_count + 1
        added = state.quizzes[-1]
        assert added.question == '새 질문'
        assert added.choices == ['A', 'B', 'C', 'D']
        assert added.answer == 3

    def test_add_multiple_quizzes(self, tmp_path):
        state = QuizState(str(tmp_path / 'state.json'))
        initial_count = len(state.quizzes)

        state.add_quiz('Q1', ['A', 'B'], 1)
        state.add_quiz('Q2', ['C', 'D'], 2)

        assert len(state.quizzes) == initial_count + 2


class TestQuizStateSaveLoad:
    def test_save_then_load(self, tmp_path):
        state_file = str(tmp_path / 'state.json')
        state = QuizState(state_file)
        state.quizzes = [Quiz('저장 질문', ['A', 'B', 'C', 'D'], 2)]
        state.best_score = 75
        state.save_state()

        loaded = QuizState(state_file)
        assert len(loaded.quizzes) == 1
        assert loaded.quizzes[0].question == '저장 질문'
        assert loaded.quizzes[0].answer == 2
        assert loaded.best_score == 75

    def test_save_creates_valid_json(self, tmp_path):
        state_file = tmp_path / 'state.json'
        state = QuizState(str(state_file))
        state.best_score = 50
        state.save_state()

        data = json.loads(state_file.read_text(encoding='utf-8'))
        assert 'quizzes' in data
        assert data['best_score'] == 50
