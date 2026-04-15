import json

from quiz import Quiz


DEFAULT_QUIZZES = [
    Quiz("Python에서 리스트를 복사할 때 얕은 복사가 되는 방법은?",
         ["a = b", "a = b.copy()", "a = b[:]", "a = list(b)"], 1),
    Quiz("다음 중 immutable 타입이 아닌 것은?",
         ["int", "str", "tuple", "list"], 4),
    Quiz("Git에서 변경사항을 스테이징 영역에 올리는 명령어는?",
         ["git commit", "git push", "git add", "git fetch"], 3),
    Quiz("시간 복잡도 O(1)이 의미하는 것은?",
         ["입력 크기에 비례", "입력 크기의 제곱에 비례", "입력 크기와 무관하게 일정", "로그에 비례"], 3),
    Quiz("HTTP 상태 코드 404가 의미하는 것은?",
         ["요청 성공", "서버 내부 오류", "요청한 리소스를 찾을 수 없음", "권한 없음"], 3),
]


class QuizState:
    def __init__(self, filename: str):
        self.filename = filename
        self.quizzes: list[Quiz] = []
        self.best_score: int = -1
        self.load_state()

    def _init_defaults(self):
        self.quizzes = list(DEFAULT_QUIZZES)
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
