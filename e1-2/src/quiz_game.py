from quiz_state import QuizState


class QuizGame:
    def __init__(self, state_filename: str = 'state.json'):
        self.state = QuizState(state_filename)
