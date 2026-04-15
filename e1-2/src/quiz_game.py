from quiz_state import QuizState


class QuizGame:
    def __init__(self, state_filename: str = 'state.json'):
        self.state = QuizState(state_filename)

    def run(self):
        try:
            while True:
                self._print_menu()
                choice = self._input_menu()
                if choice == 1:
                    pass  # 퀴즈 풀기
                elif choice == 2:
                    pass  # 퀴즈 추가
                elif choice == 3:
                    pass  # 퀴즈 목록
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

    def _input_menu(self) -> int:
        while True:
            raw = input('선택: ').strip()
            if not raw:
                print('입력값이 없습니다. 다시 입력해주세요.')
                continue
            try:
                value = int(raw)
            except ValueError:
                print('숫자를 입력해주세요.')
                continue
            if not (1 <= value <= 5):
                print('1~5 사이의 숫자를 입력해주세요.')
                continue
            return value
