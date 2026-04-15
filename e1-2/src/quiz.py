class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer
    def is_answer(self, number: int):
        return self.answer == number
    