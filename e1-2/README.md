# 프로젝트 개요

Python으로 구현한 CLI 퀴즈 게임이다. 퀴즈를 풀고, 직접 퀴즈를 추가하고, 최고 점수를 기록할 수 있다. 데이터는 `state.json`에 저장되어 프로그램을 재실행해도 유지된다.

- 체크리스트: [CHECKLISTS.md](CHECKLISTS.md)
- 작업 로그: [LOGS.md](LOGS.md)

# 퀴즈 주제와 선정 이유

주제: 프로그래밍

Python 변수 타입, Git 명령어, 시간 복잡도, HTTP 상태 코드 등 개발자가 자주 접하는 기초 개념을 퀴즈로 구성했다. 학습한 내용을 직접 문제로 만들고 풀어보면서 개념을 검증하기 위해 선정했다.

# 실행 방법

```bash
cd src
python quiz_game.py
```

또는 진입점 파일이 있는 경우:

```bash
python src/main.py
```

# 기능 목록

| 기능 | 설명 |
|------|------|
| 퀴즈 풀기 | 저장된 퀴즈를 순서대로 풀고 정답/오답 여부를 확인한다. 완료 시 결과와 점수를 출력한다. |
| 퀴즈 추가 | 문제, 선택지 4개, 정답 번호를 입력해 퀴즈를 등록한다. |
| 퀴즈 목록 | 저장된 퀴즈 목록을 번호와 함께 출력한다. |
| 점수 확인 | 퀴즈 풀기를 통해 기록된 최고 점수를 확인한다. |
| 종료 | 현재 상태를 `state.json`에 저장하고 프로그램을 종료한다. |

# 파일 구조

```
e1-2/
├── src/
│   ├── quiz.py          # Quiz 클래스 정의
│   ├── quiz_state.py    # 상태 저장/로드 및 기본 퀴즈 데이터
│   └── quiz_game.py     # 게임 루프 및 메뉴 처리
├── state.json           # 퀴즈 데이터 및 최고 점수 (자동 생성)
├── CHECKLISTS.md
├── LOGS.md
└── README.md
```

# 데이터 파일 설명

경로: `state.json` (프로젝트 루트)

역할: 퀴즈 목록과 최고 점수를 저장한다. 프로그램 종료 시 자동으로 저장되고, 다음 실행 시 불러온다. 파일이 없으면 기본 퀴즈 5개로 초기화되고, 파일이 손상된 경우에도 동일하게 초기화된다.

스키마:

```json
{
  "quizzes": [
    {
      "question": "문제 텍스트",
      "choices": ["선택지1", "선택지2", "선택지3", "선택지4"],
      "answer": 1
    }
  ],
  "best_score": 80
}
```

| 키 | 타입 | 설명 |
|----|------|------|
| `quizzes` | `array` | 퀴즈 목록 |
| `quizzes[].question` | `string` | 문제 텍스트 |
| `quizzes[].choices` | `string[]` | 선택지 목록 |
| `quizzes[].answer` | `number` | 정답 번호 (1-indexed) |
| `best_score` | `number` | 최고 점수 (0~100). 기록 없으면 `-1` |

# 실행 환경

- Docker version 28.5.2, build ecc6942
- git version 2.53.0
- macOS Sequoia Version 15.7.4 (24G517)
- zsh 5.9 (x86_64-apple-darwin24.0)

# 정리한 내용

## Python 기초

### 변수의 정의

변수는 값을 저장하는 메모리 공간이고, 변수는 이름과 값, 타입을 갖는다.

변수는 크게 mutable, immutable로 나뉜다. immutable은 불변 변수로, 힙 영역에 한 번 할당되면 그 값은 수정되지 않는다. immutable 변수의 값을 수정하더라도 그 변수가 차지하고 있던 힙 영역은 수정되지 않고, 변수 자체가 새로운 힙 영역을 가리키게 된다.

```python
a = 1 # 힙 영역 할당
a = 2 # 힙 영역 재할당 후 2 assign
```

immutable 타입에는 int, str, float, tuple, NoneType, bool, bytes가 있고, mutable 타입에는 list, dict, set, bytearray, 클래스 인스턴스가 있다.

주의할 점은 mutable 변수는 다른 변수에 복사하면 값 자체가 복사되어 대상 변수가 가리키는 힙 영역에 할당되는 것이 아니라, 원본 변수가 가리키는 메모리 주소가 복사된다.

아래 예제에서 b에 a를 복사했는데, 결과적으로 a와 b가 같은 메모리 주소를 가리키게 되어 a 내부의 값을 변경하면 b 내부의 값 또한 함께 변경된다.

```python
a = {
    "hello": "world"
}
b = a # b는 a가 가리키는 메모리 주소를 가리킴
print(b["hello"]) # 결과: world

a["hello"] = "noworld"
print(b["hello"]) # 결과: noworld
```

### if/else/elif

if는 주어진 조건에 맞춰 코드 블럭의 실행 여부를 결정하는 구문이다.
elif는 앞선 if, elif가 모두 False일 때, 추가 조건을 검사하여 해당 조건이 True일 때 코드를 실행하는 구문이다.
else는 앞선 모든 조건문이 False일 때 코드를 실행하는 구문이다.

```python
if 조건1:
    실행1
elif 조건2:
    실행2
else:
    실행3
# 조건1 평가
# ├── True  → 실행1 → 끝
# └── False ↓
#     조건2 평가
#     ├── True  → 실행2 → 끝
#     └── False ↓
#               실행3 → 끝
```

### for/while

for, while은 모두 반복문이다.
for문은 iterable에서 값을 하나씩 꺼내어, 남은 값이 없을 때까지 코드를 반복하는 구문이다. while문은 주어진 조건식이 True일 동안 반복하는 반복문이다. 

**참고**: iterable에는 list, str, tuple, set, dictinoary가 있다. range와 open(filename: str)의 리턴값도 iterable에 해당한다.

### 함수 정의

```python
def method_name(arg1: str, arg2: int = 1) -> int:
    print(arg1)
    print(arg2)
```

`->`, `:` 뒤의 str, int 등의 인자는 타입힌트이다. 타입은 강제가 아니고, 타입이 다르더라도 런타임 오류를 발생시키지 않는다.

return문으로 함수가 특정한 값을 반환하도록 할 수 있다.

함수의 인자는 두 가지 형태로 전달이 가능한데, 각각 positional argument, keyword argument 이다.
positional argument는 함수 호출 시 인자의 순서로 매개변수에 값을 전달하는 방식이다. keyword argument는 매개변수의 이름을 명시하여 값을 전달하는 방식이다.

두 방식은 혼용이 가능하지만, positional argument가 keyword argument보다 항상 앞에 와야 한다는 규칙과, 같은 매개변수에 중복된 값을 전달할 수 없다는 규칙을 지켜야 한다.

default parameter는 함수 정의 시 매개변수에 기본값을 지정하는 것이다. 호출 시 해당 인자를 생략하면 기본값이 사용된다. 기본값이 없는 매개변수가 항상 앞에 와야 한다.

```python
def greet(name, age=20):  # age의 기본값 = 20
    pass

greet("철수")      # age 생략 → age=20 사용
greet("철수", 25)  # age 전달 → age=25 사용
```

주의할 점은 mutable 타입을 기본값으로 사용하면 안 된다는 것이다. 기본값 객체는 함수 정의 시 한 번만 생성되어 호출 간에 공유되기 때문이다.

```python
def add_item(item, lst=[]):  # 위험
    lst.append(item)
    return lst

add_item(1)  # [1]
add_item(2)  # [1, 2] — 새 리스트가 아님

def add_item(item, lst=None):  # 올바른 방법
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

`/`와 `*`로 인자 전달 방식을 제한할 수 있다. `/` 앞의 매개변수는 positional로만, `*` 뒤의 매개변수는 keyword로만 전달 가능하다.

```python
def foo(a, b, /, c, *, d, e):
    pass

# a, b → positional only
# c    → 둘 다 가능
# d, e → keyword only
```

### 클래스와 객체

절차지향 프로그래밍은 프로그램을 순차적으로 실행되는 절차(함수)의 흐름으로 구성한다. 데이터와 함수가 분리되어 있으며, 함수가 데이터를 받아 처리하는 방식으로 동작한다.

객체지향 프로그래밍은 프로그램을 데이터(속성)와 그 데이터를 처리하는 함수(메서드)를 하나로 묶은 객체 단위로 구성한다.

절차지향은 데이터와 함수가 분리되어 있어 프로그램이 커질수록 어떤 함수가 어떤 데이터를 다루는지 파악하기 어렵고, 관련 코드가 여러 곳에 흩어져 수정 범위를 특정하기 어렵다. 객체지향은 관련 데이터와 동작을 객체 단위로 묶기 때문에 코드의 응집도가 높아지고, 한 객체의 내부 구현이 바뀌어도 외부 코드에 영향을 주지 않는다. 또한 클래스를 한 번 정의하면 인스턴스를 여러 개 만들어 재사용할 수 있고, 상속을 통해 기존 클래스를 변경하지 않고 기능을 확장할 수 있다.

클래스는 설계도이고, 객체는 설계도로 만든 부품의 실체이다.

## Git 기초

### Git이 필요한 이유

Git은 소스 코드의 형상 관리 프로그램으로, 커밋, 브랜치 단위로 소스코드의 버전을 관리할 수 있다.
커밋 단위로 소스 코드를 관리하므로 버그 발생 시 그 버그의 발생 시점을 쉽게 추적할 수 있다는 장점이 있다.
또한 여러 사람이 작업할 때나, 서로 다른 기능을 개발해야 할 때 브랜치로 작업을 분리해 상호의 코드를 덮어쓰지 않고 독립적으로 수정한 뒤 합칠 수 있다.

### Git 주요 명령어

| 명령어 | 설명 |
|--------|------|
| `git init` | 현재 디렉토리를 Git 저장소로 초기화한다. `.git` 디렉토리가 생성된다. |
| `git add` | 변경된 파일을 스테이징 영역에 올린다. `add`로 선택한 것만 커밋된다. `.`은 현재 디렉토리 기준 변경사항, `-A`는 저장소 전체 변경사항(삭제 포함)을 올린다. |
| `git commit` | 스테이징 영역의 변경사항을 이력으로 기록한다. 각 커밋은 고유한 해시값으로 식별된다. |
| `git push` | 로컬 저장소의 커밋을 원격 저장소에 업로드한다. |
| `git pull` | 원격 저장소의 변경사항을 로컬에 가져와 병합한다. `fetch` + `merge`를 한 번에 수행한다. |
| `git checkout` | 브랜치를 전환한다. `-b` 옵션으로 브랜치를 생성하면서 전환할 수 있다. |
| `git clone` | 원격 저장소를 로컬에 복제한다. 전체 이력이 함께 복사된다. |

### 브랜치 생성 및 병합

| 명령어 | 설명 |
|--------|------|
| `git branch 브랜치명` | 브랜치를 생성한다. |
| `git checkout -b 브랜치명` | 브랜치를 생성하고 전환한다. |
| `git merge 브랜치명` | 현재 브랜치에 대상 브랜치를 병합한다. |
| `git rebase 브랜치명` | 현재 브랜치의 커밋을 대상 브랜치 끝으로 재배치한다. |

`feature` 브랜치에서 작업을 마치고 `main`에 합치는 일반적인 흐름은 다음과 같다.

```bash
git checkout -b feature       # feature 브랜치 생성 후 전환
# ... 작업 후 커밋 ...
git checkout main             # main으로 복귀
git merge feature             # feature를 main에 병합
```

#### merge vs rebase

`merge`는 두 브랜치를 합치는 병합 커밋을 새로 만든다. 분기 이력이 그대로 남아 언제 어디서 갈라졌는지 확인할 수 있다.

```
      A - B - C  (feature)
     /         \
D - E - - - - - F  (main, merge 후)
```

`rebase`는 현재 브랜치의 커밋들을 대상 브랜치 끝으로 이어 붙인다. 분기 이력이 사라지고 커밋이 일렬로 정리되어 이력이 깔끔해지지만, 커밋 해시가 새로 생성된다.

```
D - E - A'- B'- C'  (feature, rebase 후)
```

rebase를 권장하지 않는 이유는 이력을 조작하기 때문이다. 커밋 해시가 바뀌면 같은 브랜치를 기반으로 작업하던 다른 사람의 이력과 달라진다. 이 상태에서 push하려면 강제 push(`--force`)가 필요하고, 그 과정에서 다른 사람의 커밋을 덮어쓸 수 있다. 문제가 생겼을 때 원래 이력이 사라져 원인을 추적하기도 어렵다.

rebase는 아직 push하지 않은 로컬 브랜치에서 커밋을 정리할 때만 사용하는 것이 안전하다.

### 저장소 생성 및 GitHub 연결

GitHub에서 새 저장소를 생성한 뒤, 아래 순서로 로컬과 연결한다.

```bash
git init -b main
git add .
git commit -m "init"
git remote add origin https://github.com/유저명/저장소명.git  # origin은 원격 저장소에 붙이는 별칭
git push -u origin main  # -u로 upstream 설정
```
### clone / pull 실습

실습 수행 로그: [LOGS.md](LOGS.md#git-저장소-복제-실습)
