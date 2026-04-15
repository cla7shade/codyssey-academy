from quiz_state import QuizState


class QuizGame:
    def __init__(self, state_filename: str = 'state.json'):
        self.state = QuizState(state_filename)

    def run(self):
        try:
            while True:
                self._print_menu()
                choice = self._input_int('선택: ', 1, 5)
                if choice == 1:
                    self._play_quiz()
                elif choice == 2:
                    self._add_quiz()
                elif choice == 3:
                    self._list_quizzes()
                elif choice == 4:
                    pass  # 점수 확인
                elif choice == 5:
                    self.state.save_state()
                    print('저장 후 종료합니다.')
                    break
        except (KeyboardInterrupt, EOFError):
            print('\n프로그램을 종료합니다.')
            self.state.save_state()

    def _print_menu(self):
        print()
        print('========================================')
        print('          나만의 퀴즈 게임')
        print('========================================')
        print('1. 퀴즈 풀기')
        print('2. 퀴즈 추가')
        print('3. 퀴즈 목록')
        print('4. 점수 확인')
        print('5. 종료')
        print('========================================')

    def _input_int(self, prompt: str, min_val: int, max_val: int) -> int:
        while True:
            raw = input(prompt).strip()
            if not raw:
                print('입력값이 없습니다. 다시 입력해주세요.')
                continue
            try:
                value = int(raw)
            except ValueError:
                print('숫자를 입력해주세요.')
                continue
            if not (min_val <= value <= max_val):
                print(f'{min_val}~{max_val} 사이의 숫자를 입력해주세요.')
                continue
            return value

    def _play_quiz(self):
        quizzes = self.state.quizzes
        if not quizzes:
            print('등록된 퀴즈가 없습니다.')
            return

        print(f'\n퀴즈를 시작합니다! (총 {len(quizzes)}문제)')

        correct = 0
        for i, quiz in enumerate(quizzes, 1):
            print(f'\nQ{i}. {quiz.question}')
            for j, choice in enumerate(quiz.choices, 1):
                print(f'  {j}. {choice}')
            answer = self._input_int('정답: ', 1, len(quiz.choices))
            if quiz.is_answer(answer):
                print('정답입니다!')
                correct += 1
                continue
            print(f'오답입니다. 정답은 {quiz.answer}번입니다.')

        score = round(correct / len(quizzes) * 100)
        print(f'\n결과: {len(quizzes)}문제 중 {correct}개 정답 ({score}점)')

        if score > self.state.best_score:
            self.state.best_score = score
            print('최고 점수를 갱신했습니다!')

    def _add_quiz(self):
        print('\n-- 퀴즈 추가 --')
        question = input('문제: ').strip()
        if not question:
            print('문제를 입력해주세요.')
            return

        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f'선택지 {i}: ').strip()
                if choice:
                    choices.append(choice)
                    break
                print('선택지를 입력해주세요.')

        answer = self._input_int('정답 번호 (1~4): ', 1, 4)
        self.state.add_quiz(question, choices, answer)
        print('퀴즈가 추가되었습니다.')

    def _list_quizzes(self):
        quizzes = self.state.quizzes
        if not quizzes:
            print('등록된 퀴즈가 없습니다.')
            return

        print(f'\n-- 퀴즈 목록 ({len(quizzes)}개) --')
        for i, quiz in enumerate(quizzes, 1):
            print(f'{i}. {quiz.question}')
