from quiz import Quiz


class TestQuiz:
    def test_correct_answer(self):
        quiz = Quiz("질문", ["A", "B", "C", "D"], 2)
        assert quiz.is_answer(2) is True

    def test_wrong_answer(self):
        quiz = Quiz("질문", ["A", "B", "C", "D"], 2)
        assert quiz.is_answer(1) is False

    def test_first_choice_as_answer(self):
        quiz = Quiz("질문", ["A", "B", "C", "D"], 1)
        assert quiz.is_answer(1) is True
        assert quiz.is_answer(2) is False

    def test_last_choice_as_answer(self):
        quiz = Quiz("질문", ["A", "B", "C", "D"], 4)
        assert quiz.is_answer(4) is True
        assert quiz.is_answer(3) is False

    def test_attributes_stored(self):
        quiz = Quiz("파이썬은?", ["언어", "프레임워크", "DB", "OS"], 1)
        assert quiz.question == "파이썬은?"
        assert quiz.choices == ["언어", "프레임워크", "DB", "OS"]
        assert quiz.answer == 1
