# 프로젝트 개요

파이썬 실습

- 체크리스트: [CHECKLISTS.md](CHECKLISTS.md)
- 작업 로그: [LOGS.md](LOGS.md)

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