import json

from quiz import Quiz


class QuizState:
    def __init__(self, filename: str):
        self.filename = filename
        self.quizzes: list[Quiz] = []
        self.best_score: int = -1
        self.load_state()

    def _init_defaults(self):
        self.quizzes = []
        self.best_score = -1

    def load_state(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                saved_state = json.load(f)
            self.quizzes = [
                Quiz(q['question'], q['choices'], q['answer'])
                for q in saved_state.get('quizzes', [])
            ]
            self.best_score = saved_state.get('best_score', -1)
        except FileNotFoundError:
            self._init_defaults()
        except json.JSONDecodeError:
            print("저장 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
            self._init_defaults()

    def get_best_score(self) -> int:
        return self.best_score

    def add_quiz(self, question: str, choices: list[str], answer: int):
        self.quizzes.append(Quiz(question, choices, answer))

    def save_state(self):
        state = {
            'quizzes': [q.__dict__ for q in self.quizzes],
            'best_score': self.best_score,
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
