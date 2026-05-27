# 🐍 Python 학습 노트

> `basic/` 폴더의 실습 파일을 기반으로 작성된 파이썬 학습 노트입니다.

---

## 📚 목차

1. [기초 문법](#1-기초-문법)
   - [Hello World & `__name__`](#11-hello-world--__name__)
   - [변수와 타입](#12-변수와-타입)
   - [키워드 목록](#13-키워드-목록)
   - [print() 함수](#14-print-함수)
2. [문자열 (String)](#2-문자열-string)
3. [리스트 (List)](#3-리스트-list)
   - [리스트 기초](#31-리스트-기초)
   - [리스트 참조 전달](#32-리스트-참조-전달)
   - [리스트 메서드](#33-리스트-메서드)
   - [for 루프와 enumerate / zip](#34-for-루프와-enumerate--zip)
   - [리스트 컴프리헨션](#35-리스트-컴프리헨션)
4. [딕셔너리 (Dictionary)](#4-딕셔너리-dictionary)
5. [함수 (Function)](#5-함수-function)
   - [기본 함수 정의](#51-기본-함수-정의)
   - [가변 인자 (`*args`)](#52-가변-인자-args)
   - [기본값 인자 & 키워드 인자 (`**kwargs`)](#53-기본값-인자--키워드-인자-kwargs)
6. [파일 입출력](#6-파일-입출력)
7. [예외 처리](#7-예외-처리)
8. [클래스 (Class)](#8-클래스-class)
   - [클래스 기초](#81-클래스-기초)
   - [인스턴스 메서드](#82-인스턴스-메서드)
   - [isinstance 함수](#83-isinstance-함수)
   - [스페셜 메서드 (Magic Method)](#84-스페셜-메서드-magic-method)
   - [클래스 변수 & 클래스 메서드](#85-클래스-변수--클래스-메서드)
   - [소멸자 (`__del__`)](#86-소멸자-__del__)
   - [프로퍼티 (Property)](#87-프로퍼티-property)
   - [상속 (Inheritance)](#88-상속-inheritance)
   - [다중 상속](#89-다중-상속)
9. [고급 함수 기법](#9-고급-함수-기법)
   - [재귀 & 피보나치](#91-재귀--피보나치)
   - [캐시 (`functools.cache`)](#92-캐시-functoolscache)
   - [제네레이터 (Generator)](#93-제네레이터-generator)
   - [래퍼 함수](#94-래퍼-함수)
   - [데코레이터 (Decorator)](#95-데코레이터-decorator)
   - [실행 시간 측정 데코레이터](#96-실행-시간-측정-데코레이터)
10. [모듈 & 패키지](#10-모듈--패키지)
11. [데이터 직렬화](#11-데이터-직렬화)
    - [JSON](#111-json)
    - [YAML](#112-yaml)
12. [실용 라이브러리](#12-실용-라이브러리)
    - [커맨드라인 인자 (`sys.argv`)](#121-커맨드라인-인자-sysargv)
    - [로깅 (Logging)](#122-로깅-logging)
    - [Matplotlib 그래프](#123-matplotlib-그래프)
    - [HTTP 요청 (requests)](#124-http-요청-requests)
13. [데이터클래스 (`dataclass`)](#13-데이터클래스-dataclass)

---

## 1. 기초 문법

### 1.1 Hello World & `__name__`

> 📄 파일: [`hello.py`](basic/hello.py)

```python
print("hello, world")

def main():
    print("hello world2")
    print(__name__)

if __name__ == "__main__":   # import를 당했을 때 __main__이 아니게 된다.
    main()
```

**핵심 개념**
- 파이썬 스크립트를 **직접 실행**하면 `__name__` → `"__main__"`
- 다른 파일에서 **import** 하면 `__name__` → 모듈 파일명 (예: `"hello"`)
- `if __name__ == "__main__":` 패턴으로 **직접 실행 시에만 동작하는 코드**를 분리

---

### 1.2 변수와 타입

> 📄 파일: [`variable.py`](basic/variable.py)

```python
def main():
    int_a = 10
    print(int_a)       # 10
    print(type(int_a)) # <class 'int'>
    int_a = "ten"      # 동적 타이핑: 같은 변수에 다른 타입 대입 가능
    print(type(int_a)) # <class 'str'>
```

**네이밍 컨벤션 (Convention)**

| 대상 | 규칙 | 예시 |
|------|------|------|
| 변수 / 함수명 | 소문자 시작, 스네이크 케이스 | `my_variable`, `print_hello` |
| 클래스명 | 대문자 시작, 파스칼 케이스 | `Student`, `MyClass` |
| 식별자 | 문자 + 숫자 + `_` 조합 | `a_b_c`, `thePythonClass` |

> ⚠️ 파이썬은 **동적 타이핑** 언어 — 런타임에 타입이 결정되며, 같은 변수에 다른 타입을 재할당할 수 있다.

---

### 1.3 키워드 목록

> 📄 파일: [`a02_keyword.py`](basic/a02_keyword.py)

```python
import keyword

def main():
    print(keyword.kwlist)  # 파이썬의 모든 예약어 출력
```

파이썬 예약어는 **변수명으로 사용 불가** (예: `if`, `for`, `class`, `return` 등)

---

### 1.4 print() 함수

> 📄 파일: [`a04_print.py`](basic/a04_print.py)

```python
print(1_234_567)                           # 숫자에 _ 사용 가능 (가독성)
print('python "class"')                    # 문자열 내 따옴표 혼합

print("A", "B", "C", sep="_", end="")     # sep: 구분자, end: 끝 문자
print("A", "B", "C", sep=".")

class A:
    def __repr__(self):
        return "this is class A!!"

print(A())        # __repr__ 출력
print(type(A()))  # <class '__main__.A'>
```

**print() 주요 옵션**

| 옵션 | 기본값 | 설명 |
|------|--------|------|
| `sep` | `" "` (공백) | 여러 값 사이 구분자 |
| `end` | `"\n"` (줄바꿈) | 출력 끝에 붙는 문자 |
| `file` | `sys.stdout` | 출력 대상 (파일로도 출력 가능) |

---

## 2. 문자열 (String)

> 📄 파일: [`a08_str_indexing.py`](basic/a08_str_indexing.py)

```python
str_var = "안녕하세요"

# 인덱싱
print(str_var[0])   # 안
print(str_var[-1])  # 요  (음수 인덱스: 뒤에서부터)

# 문자열은 불변(immutable) → 직접 수정 불가
# str_var[4] = "여"  ← 에러!
str_var = str_var.replace("요", "여")  # 새 문자열 생성으로 대체

# 슬라이싱 [start:stop:step]
str_var *= 3
print(str_var[5:10])     # 5~9번 인덱스
print(str_var[5:10:2])   # 5,7,9번 인덱스 (2칸씩)
print(str_var[-1::-1])   # 역순 출력

# 길이
print(len(str_var))
print(str_var.__len__())  # 내부적으로는 __len__ 호출
```

**슬라이싱 `[start:stop:step]` 정리**

| 표현 | 의미 |
|------|------|
| `s[2:5]` | 인덱스 2, 3, 4 |
| `s[:3]` | 처음부터 인덱스 2까지 |
| `s[3:]` | 인덱스 3부터 끝까지 |
| `s[-1::-1]` | 끝부터 역순으로 전체 |
| `s[::2]` | 처음부터 2칸씩 |

---

## 3. 리스트 (List)

### 3.1 리스트 기초

> 📄 파일: [`a21_list.py`](basic/a21_list.py)

```python
import datetime

list_a = []           # 빈 리스트 선언
list_b = list()       # 클래스로도 선언 가능

ptime = datetime.datetime.now()
list_d = [1, 2, 3.141592, "choi", ptime]  # 다양한 타입 혼합 가능
list_d[3] = "kim"                          # 값 수정 가능 (mutable)

# 2차원 리스트
list_e = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_e[1][1])   # 5
```

---

### 3.2 리스트 참조 전달

> 📄 파일: [`a22_list_function.py`](basic/a22_list_function.py)

```python
def make_20(var_a_b):
    var_a_b[0] = 20    # 리스트 자체를 수정 (참조 전달)

def main():
    ver_a = 10
    wrapper_list = [ver_a]
    make_20(wrapper_list)
    print(wrapper_list[0])   # 20

    list_a = [1, 2, 3]
    list_b = [4, 5, 6, list_a]  # list_a의 메모리를 참조
    list_a[2] = 30
    print(list_b)   # [4, 5, 6, [1, 2, 30]] ← list_b도 바뀜!
```

> ⚠️ **핵심**: 리스트는 함수에 전달될 때 **값의 복사가 아닌 메모리 주소(참조)** 가 전달된다.  
> C의 포인터와 유사한 개념. 리스트 내부 값을 변경하면 원본에도 영향을 미친다.

---

### 3.3 리스트 메서드

> 📄 파일: [`a23_list_method.py`](basic/a23_list_method.py)

```python
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 합치기
list_a + list_b            # 새 리스트 반환
list_a := list_a.__add__(list_b)  # elephant sign (왈러스 연산자)
list_a.extend(list_b)     # list_a 자체를 수정

# 추가 / 삽입
list_b.append("추가 원소")   # 끝에 추가
list_b.insert(3, 7)          # 인덱스 3에 7 삽입

# 삭제
list_b.pop()      # 마지막 원소 꺼내기 (리스트에서 삭제)
list_b.pop(0)     # 인덱스 0 원소 꺼내기
list_b.remove(6)  # 값이 6인 원소 삭제
del list_e[4]     # 인덱스 4 원소 메모리 삭제

# 검색
list_b.index("e")          # "e"의 인덱스 반환
print("g" in list_e)       # 포함 여부 (True/False)

# 길이
len(list_e)
```

| 메서드 | 설명 |
|--------|------|
| `append(x)` | 끝에 원소 추가 |
| `insert(i, x)` | 인덱스 i에 원소 삽입 |
| `extend(list)` | 다른 리스트로 확장 |
| `pop(i)` | 인덱스 i의 원소 꺼내기 |
| `remove(x)` | 값 x를 찾아 첫 번째 것 삭제 |
| `index(x)` | x의 인덱스 반환 |

---

### 3.4 for 루프와 enumerate / zip

> 📄 파일: [`a19.py`](basic/a19.py)

```python
list1 = ["a", "b", "c", 1, 2, 3]
list2 = ["에이", "비", "씨", "one", "two", "three"]

# ✅ 파이썬 스타일 (Pythonic)
for ele in list1:
    print(ele)

# ❌ C 스타일 (비추천)
for i in range(len(list1)):
    print(list1[i])

# ✅ 인덱스가 필요한 경우 → enumerate 사용
for i, ele in enumerate(list1):
    print(ele, i)

# ✅ 두 리스트를 동시에 순회 → zip 사용
for ele1, ele2 in zip(list1, list2):
    print(ele1, ele2)
```

---

### 3.5 리스트 컴프리헨션

> 📄 파일: [`a30_list_comprehension.py`](basic/a30_list_comprehension.py)

```python
import random

# 기본 문법: [결과 for 변수 in 컨테이너 if 조건]
li = [i+1 for i in range(100) if i % 2 == 0]  # 홀수 인덱스만
random.shuffle(li)   # 리스트 랜덤 셔플

li = [i**2 + 1 for i in range(100) if i % 2 == 0]
print(min(li), max(li), sum(li))  # 최솟값, 최댓값, 합계
li.sort()                          # 오름차순 정렬
li.sort(reverse=True)              # 내림차순 정렬
```

> 💡 리스트 컴프리헨션은 `for` + `if`를 한 줄로 간결하게 표현하는 파이썬의 핵심 문법이다.

---

## 4. 딕셔너리 (Dictionary)

> 📄 파일: [`a25_dictionary.py`](basic/a25_dictionary.py)

```python
dict_a = {}          # 빈 딕셔너리
dict_b = dict()      # 클래스로도 선언 가능

# ⚠️ 주의: {}는 set이 아니라 dict! set는 값이 있어야 구분됨
set_a = {1, 2}       # <class 'set'>

# 다양한 타입의 key 사용 가능
a = A()
dict_c = {
    "a": 1234,
    "b": 879,
    3.14: 1111,
    a: 4.4444,       # 객체도 key가 될 수 있다
}

print(dict_c["c"])   # 값 접근
print(dict_c[a])     # 객체를 key로 접근
```

**dict vs set 구분**

| 표현 | 타입 |
|------|------|
| `{}` | `dict` (빈 딕셔너리) |
| `{1, 2}` | `set` |
| `{"a": 1}` | `dict` |

---

## 5. 함수 (Function)

### 5.1 기본 함수 정의

> 📄 파일: [`a31_function.py`](basic/a31_function.py)

```python
# 타입 힌트와 docstring 사용 권장
def print_n_time(value: str, n: int) -> str:
    """교육용 테스트 함수이다.

    Args:
        value (str): 출력할 메세지
        n (int): 반복 출력횟수

    Returns:
        str: 에러 반환
    """
    for i in range(n):
        print(value)
    return "ok"
```

**함수 작성 팁**
- **타입 힌트** (`value: str`, `-> str`): 정적 분석 도구가 타입을 추론할 수 있게 도와줌
- **docstring**: 함수의 역할, 인자, 반환값을 문서화 → IDE에서 자동으로 표시됨

---

### 5.2 가변 인자 (`*args`)

> 📄 파일: [`a32_argument.py`](basic/a32_argument.py)

```python
def print_n_time(n: int, *value: str) -> str:
    print(type(value))    # <class 'tuple'>
    for i in range(n):
        for v in value:
            print(v, end=" ")

def main():
    print_n_time(3, "abc", "def", "ghi", "ddd")
    # n=3, value=("abc", "def", "ghi", "ddd")
```

> `*args`는 여러 위치 인자를 **튜플**로 묶어서 받는다.

---

### 5.3 기본값 인자 & 키워드 인자 (`**kwargs`)

> 📄 파일: [`a33_default_argument.py`](basic/a33_default_argument.py), [`a35_variable_length_keyword_argument.py`](basic/a35_variable_length_keyword_argument.py)

```python
# 기본값 인자 (Default Argument)
def print_n_time(*value: str, n: int = 2) -> str:
    ...

print_n_time("abc", "def")        # n=2 (기본값)
print_n_time("abc", "def", n=4)   # n=4 (명시적 지정)
```

```python
# **kwargs: 키워드 인자를 딕셔너리로 받음
def print_n_times(*args, **kargs):
    for value in args:              # args는 tuple
        print(value)
    for key, value in kargs.items():  # kargs는 dict
        print(key, value)

print_n_times(1, 2, 3, a=1, b=2, c=3)
```

**인자 종류 정리**

| 종류 | 문법 | 타입 | 설명 |
|------|------|------|------|
| 위치 인자 | `def f(a, b)` | - | 순서대로 전달 |
| 가변 위치 인자 | `def f(*args)` | `tuple` | 여러 값을 튜플로 수집 |
| 기본값 인자 | `def f(n=2)` | - | 값 미전달 시 기본값 사용 |
| 가변 키워드 인자 | `def f(**kwargs)` | `dict` | `key=value` 형태를 딕셔너리로 수집 |

---

## 6. 파일 입출력

> 📄 파일: [`a42_file_write.py`](basic/a42_file_write.py), [`a43_file_read.py`](basic/a43_file_read.py)

```python
from pathlib import Path

path = Path(r"C:\segang\python\basic\__pycache__")

# 파일 쓰기 - with 문 사용 권장 (자동으로 close)
with open(path / "text.txt", "a", encoding="utf-8") as f:
    f.write("hello!!!")
    print("프린트로도 파일에 쓸 수 있다.", file=f)  # print의 file 인자 활용

# 파일 읽기
with open(path / "text.txt", "r", encoding="utf-8") as f:
    data = f.read()        # 전체 읽기
    data = f.readlines()   # 줄 단위로 리스트로 읽기
    data = f.readline()    # 한 줄씩 읽기

    # 파일이 클 때: while + 왈러스 연산자
    while data := f.readline():
        print(data)
```

**파일 모드**

| 모드 | 의미 |
|------|------|
| `"r"` | 읽기 (기본값) |
| `"w"` | 쓰기 (기존 내용 덮어씀) |
| `"a"` | 추가 (기존 내용 뒤에 붙임) |
| `"b"` | 바이너리 모드 (예: `"rb"`) |

**표준 파일 디스크립터**
```python
import sys
sys.stdin.fileno()   # 0 - 표준 입력
sys.stdout.fileno()  # 1 - 표준 출력
sys.stderr.fileno()  # 2 - 표준 에러 (버퍼 없이 바로 출력)

print("error", file=sys.stderr)   # 에러 스트림에 출력
```

---

## 7. 예외 처리

> 📄 파일: [`a47_try_exception.py`](basic/a47_try_exception.py)

```python
import math

# 사용자 정의 예외 클래스
class NegativeError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.args = ("이것은 내가 만든 네거티브 에러이다.",)

def main():
    user_input = input("정수 입력")

    try:
        number_input = int(user_input)
        if number_input < 0:
            raise NegativeError       # 직접 예외 발생
    except ValueError as e:
        print("정수를 입력하지 않았습니다.", e)
    except NegativeError as e:
        print("양의 정수를 입력하세요..", e)
    else:
        # 예외가 발생하지 않았을 때 실행
        print("원의 넓이:", math.pi * number_input ** 2)
    finally:
        # 예외 발생 여부와 무관하게 항상 실행
        print("프로그램이 끝났습니다.")
```

**try-except 구조**

```
try      → 예외가 발생할 수 있는 코드
except   → 예외 발생 시 처리
else     → 예외가 없을 때 실행
finally  → 항상 실행 (정리 코드)
```

---

## 8. 클래스 (Class)

### 8.1 클래스 기초

> 📄 파일: [`a63_class_student.py`](basic/a63_class_student.py)

```python
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name         # 인스턴스 변수
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

students = [
    Student("abc", 30, 65, 45, 44),
    Student("dfe", 30, 35, 85, 14),
]

for student in students:
    print(f"{student.name}\t {student.korean}\t {student.math}")
```

> `__init__`은 **초기화 메서드** (생성자는 `__new__`). 객체 생성 직후 자동 호출된다.

---

### 8.2 인스턴스 메서드

> 📄 파일: [`a64_class_method.py`](basic/a64_class_method.py)

```python
class Student:
    def __init__(self, name, korean, math, english, science):
        ...

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __repr__(self):
        # print(student) 할 때 출력될 문자열
        return f"{self.name}\t ... \t {self.get_sum()}\t {self.get_average()}"

# __repr__ 덕분에 아래처럼 간단히 출력 가능
for student in students:
    print(student)
```

---

### 8.3 isinstance 함수

> 📄 파일: [`a65_isinstance.py`](basic/a65_isinstance.py)

```python
class Student:
    def study(self): print("studying")

class Teacher:
    def teach(self): print("teaching")

student = Student()
print(isinstance(student, Student))  # True
print(isinstance(student, int))      # False
print(isinstance(student, object))   # True (모든 파이썬 객체는 object를 상속)

# 런타임에 타입을 확인하여 분기 처리
classroom = [Student(), Student(), Teacher(), Teacher()]
for person in classroom:
    if isinstance(person, Student):
        person.study()
    if isinstance(person, Teacher):
        person.teach()
```

---

### 8.4 스페셜 메서드 (Magic Method)

> 📄 파일: [`a66_special_method.py`](basic/a66_special_method.py)

```python
class Student:
    def __repr__(self): ...        # repr() / 개발자용 문자열
    def __str__(self) -> str: ...  # str() / print() 출력 문자열

    # 사칙연산 오버로딩
    def __add__(self, other):      # + 연산자
        return self.get_sum() + other.get_sum()
    def __sub__(self, other): ...  # - 연산자
    def __mul__(self, other): ...  # * 연산자
    def __truediv__(self, other):  # / 연산자
        return self.get_sum() / other.get_sum()

    # 비교 연산자 오버로딩
    def __gt__(self, value):       # > 연산자
        if isinstance(value, Student):
            return self.get_sum() > value.get_sum()

# 사용
print(students[0] + students[1])   # __add__ 호출
print(students[0] > students[1])   # __gt__ 호출
```

**주요 스페셜 메서드 목록**

| 메서드 | 연산자 | 설명 |
|--------|--------|------|
| `__str__` | `str()`, `print()` | 사람이 읽기 좋은 문자열 |
| `__repr__` | `repr()` | 개발자용 문자열 |
| `__add__` | `+` | 덧셈 |
| `__sub__` | `-` | 뺄셈 |
| `__mul__` | `*` | 곱셈 |
| `__truediv__` | `/` | 나눗셈 |
| `__gt__` | `>` | 크다 |
| `__lt__` | `<` | 작다 |
| `__eq__` | `==` | 같다 |
| `__len__` | `len()` | 길이 |

---

### 8.5 클래스 변수 & 클래스 메서드

> 📄 파일: [`a67_class_variable.py`](basic/a67_class_variable.py)

```python
class Student:
    count = int()      # 클래스 변수 (모든 인스턴스가 공유)
    students = list()  # 클래스 변수

    def __init__(self, name, ...):
        count1 = int() # 로컬 변수 (함수 내부에서만 사용)
        ...
        Student.count += 1           # 클래스 변수 접근
        Student.students.append(self) # 생성 시 자기 자신을 리스트에 추가

    @classmethod
    def print(cls):     # self 대신 cls (클래스 자체가 들어옴)
        for student in Student.students:
            print(student)

# 사용
Student("abc", 30, 65, 45, 44)
print(f"등록된 학생 수: {Student.count}")
Student.print()
```

**인스턴스 변수 vs 클래스 변수**

| 구분 | 선언 위치 | 접근 방법 | 공유 여부 |
|------|-----------|-----------|-----------|
| 인스턴스 변수 | `__init__` 내 `self.xxx` | `instance.xxx` | 각 인스턴스 독립 |
| 클래스 변수 | 클래스 블록 상단 | `ClassName.xxx` | 모든 인스턴스 공유 |

---

### 8.6 소멸자 (`__del__`)

> 📄 파일: [`a68_Destructor.py`](basic/a68_Destructor.py)

```python
class Test:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 이 생성 되었습니다.")

    def __del__(self):
        print(f"{self.name} - 파괴 되었습니다.")

def main():
    a = Test("a")
    b = Test("b")
    c = Test("c")
    del c          # 명시적으로 c 삭제 → __del__ 즉시 호출
    # main 종료 시 a, b도 순서대로 파괴됨
```

> 💡 파이썬 객체의 메모리는 **가비지 컬렉터**가 외부에서 관리.  
> `__del__`은 C++의 소멸자와 유사하지만, 호출 시점이 보장되지 않을 수 있다.

---

### 8.7 프로퍼티 (Property)

> 📄 파일: [`a70_property.py`](basic/a70_property.py)

```python
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius   # __ (private 변수)

    @property
    def radius(self):            # getter
        return self.__radius

    @radius.setter
    def radius(self, value):     # setter (유효성 검사 포함)
        if isinstance(value, int) and value > 0:
            self.__radius = value
        else:
            print("양의 정수만 넣으시오")

    def get_area(self):
        return math.pi * (self.__radius ** 2)

circle = Circle(10)
print(circle.radius)    # getter 호출 (소괄호 없이 변수처럼)
circle.radius = 20      # setter 호출
circle.radius = -5      # 유효성 검사 → "양의 정수만 넣으시오"

# descriptor 관련
print(vars(circle))                        # 인스턴스 변수 딕셔너리
print(getattr(circle, "get_area")())      # 메서드 동적 호출
print(getattr(circle, "없는메서드", None)) # 없으면 None 반환
```

**`_` 의 특별한 쓰임새**
```python
# 반복 변수가 필요 없을 때 _ 사용 (관례)
for _ in range(100):
    print("[loop]", end="")

# 튜플 언패킹에서 불필요한 값 무시
a_tu = 1, 2, 3, "valuable text"
_, _, _, text = a_tu
print(text)   # "valuable text"
```

---

### 8.8 상속 (Inheritance)

> 📄 파일: [`a71_class_inheritance.py`](basic/a71_class_inheritance.py)

```python
class Parent:
    def __init__(self, value):
        self.value = "테스트"
        self.value2 = value

    def test(self):
        print("parent 클래스의 test메소드")

class Child(Parent):
    def __init__(self, value):
        super().__init__("child에서 넘어간 값")  # 부모 __init__ 반드시 호출
        print("child __init__ 호출")

    # 오버라이딩 (파이썬은 오버로딩 없음, 오버라이딩만 존재)
    def test(self, *args):
        print("child 클래스의 test메소드")

child = Child("자식 자료")
child.test()      # Child의 test (오버라이딩)
child.test(111)   # *args로 받음
print(child.value)   # Parent에서 설정한 값
print(child.value2)  # super().__init__()으로 전달된 값
```

> ⚠️ 파이썬은 **오버로딩이 없고 오버라이딩만** 있다. `*args`를 활용해 다양한 인자 수를 처리한다.

---

### 8.9 다중 상속

> 📄 파일: [`a72_multiple_inheritance.py`](basic/a72_multiple_inheritance.py)

```python
class Person:
    def __init__(self, b): self.b = b
    def greeting(self): print("안녕하세요")

class University:
    def __init__(self, a): self.a = a
    def message_credit(self): print("학점관리")

class Undergraduate(Person, University):
    def __init__(self):
        Person.__init__(self, 1)      # super() 대신 직접 호출도 가능
        University.__init__(self, 2)

    def study(self): print("공부하기")

james = Undergraduate()
james.greeting()         # Person 메서드
james.message_credit()   # University 메서드
james.study()

# MRO (Method Resolution Order) 확인
print(Undergraduate.__mro__)
```

> `__mro__`(Method Resolution Order)를 통해 파이썬이 메서드를 찾는 순서를 확인할 수 있다.

---

## 9. 고급 함수 기법

### 9.1 재귀 & 피보나치

> 📄 파일: [`a80_fibonacci.py`](basic/a80_fibonacci.py)

```python
cnt = 0

def fibonacci(n):
    global cnt
    cnt += 1
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(36))
print(f"fibonacci 수행 횟수: {cnt}")  # 매우 많음!
```

> ⚠️ 순수 재귀 피보나치는 같은 계산을 반복 → **지수 시간 복잡도** O(2^n)

---

### 9.2 캐시 (`functools.cache`)

> 📄 파일: [`a81_fibonacci_chche.py`](basic/a81_fibonacci_chche.py)

```python
from functools import cache

cnt = 0

@cache
def fibonacci(n):
    global cnt
    cnt += 1
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(36))
print(f"fibonacci 수행 횟수: {cnt}")  # 36번만 수행!
```

> `@cache` 데코레이터: 한 번 계산한 결과를 **메모이제이션**으로 저장 → O(n)으로 성능 개선  
> ⚠️ 모든 함수에 붙이면 오히려 메모리 낭비. **반복 호출이 많은 함수**에만 사용.

---

### 9.3 제네레이터 (Generator)

> 📄 파일: [`a86_generator.py`](basic/a86_generator.py)

```python
def test():
    print("TEST A")
    yield 0        # yield: 값을 반환하고 함수 실행을 일시 중단
    print("test B")
    yield 1

def main():
    gen = test()
    print(next(gen))   # "TEST A" 출력 → 0 반환
    print(next(gen))   # "test B" 출력 → 1 반환

    try:
        print(next(gen))
    except StopIteration:
        print("generator end")   # 더 이상 yield 없음
```

**제네레이터 특징**
- `yield` 키워드로 값을 하나씩 반환
- 함수 실행을 **중단/재개** 가능
- 메모리 효율적 (한 번에 모든 값을 생성하지 않음)
- `next()` 또는 `for` 루프로 소비

---

### 9.4 래퍼 함수

> 📄 파일: [`a101_wrapper_function.py`](basic/a101_wrapper_function.py)

```python
def simple_wrapper(func):
    def wrapper():
        print("func 실행 전 코드...")
        func()
        print("func 실행 후 코드...")
    return wrapper   # 함수를 반환!

def print_hello():
    print("print_hello 함수가 실행됨")

# 래퍼로 감싸기
a = simple_wrapper(print_hello)
a()  # 전/후 코드가 자동으로 실행됨
```

---

### 9.5 데코레이터 (Decorator)

> 📄 파일: [`a102_decorator.py`](basic/a102_decorator.py)

```python
from functools import wraps

def hi(value):
    def my_decorator(func):
        @wraps(func)   # 원본 함수의 __name__ 등을 보존
        def wrapper(*args, **kwargs):
            print(f"func 실행 전..{value}")
            result = func(*args, **kwargs)
            print(f"func 실행 후..{value}")
            return result
        return wrapper
    return my_decorator

@hi('hi')   # = print_hello = hi('hi')(print_hello)
def print_hello(n, v):
    for _ in range(n):
        print(v)
    return 123

print_hello(5, "hello")
print(print_hello.__name__)  # "print_hello" (@wraps 덕분에 보존됨)
```

---

### 9.6 실행 시간 측정 데코레이터

> 📄 파일: [`a103_time_decorator.py`](basic/a103_time_decorator.py)

```python
from functools import wraps
import time

def runtime_check(n):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"함수이름: {func.__name__}")
            start_time = time.time()
            for i in range(n):             # n번 반복 실행
                result = func(*args, **kwargs)
            end_time = time.time()
            print(f"평균 실행 시간: {(end_time - start_time) / n:.3}초")
            return result
        return wrapper
    return my_decorator

@runtime_check(3)   # 3번 반복해서 평균 시간 측정
def print_hello(n, s):
    for _ in range(n):
        s += 1
    return s

re = print_hello(50_000_000, 10_000_000)
```

> 💡 함수의 **성능 프로파일링**에 활용. 자주 호출되는 함수의 실행 시간을 모니터링할 수 있다.

---

## 10. 모듈 & 패키지

> 📄 파일: [`a90_package_import.py`](basic/a90_package_import.py)

```python
# 방법 1: 직접 import
from .module_a import module_var_a
from .module_b import module_var_b

# 방법 2: __init__.py를 만들어 패키지로 묶기
from test_package import *

def main():
    print(module_var_a)
    print(module_var_b)
    module_a_func()
```

**패키지 구조 예시**
```
test_package/
├── __init__.py      ← 이걸 만들면 패키지가 됨
├── module_a.py
└── module_b.py
```

> ⚠️ 유명한 라이브러리 이름(`json.py`, `math.py` 등)으로 파일을 만들면 표준 라이브러리와 충돌 가능!

---

## 11. 데이터 직렬화

### 11.1 JSON

> 📄 파일: [`a111_json_serialization.py`](basic/a111_json_serialization.py)

```python
import json
from pathlib import Path

path = Path(r"C:\segang\python\basic\__pycache__\test.json")
with path.open("r", encoding="utf-8") as f:
    data = json.load(f)   # JSON 파일 → Python dict/list
    print(data)
    print(data["abc"])
    print(data["subject"]["korean"])  # 중첩 접근
```

---

### 11.2 YAML

> 📄 파일: [`a112_yaml_serialization.py`](basic/a112_yaml_serialization.py)

```python
# pip install pyyaml
import yaml
from pathlib import Path

path = Path(r"C:\segang\python\basic\__pycache__\test.yaml")
with path.open("r", encoding="utf-8") as f:
    data = yaml.safe_load(f)   # YAML 파일 → Python dict/list
    print(data["subject"]["korean"])
```

**JSON vs YAML 비교**

| 특징 | JSON | YAML |
|------|------|------|
| 가독성 | 보통 | 높음 |
| 주석 | 불가 | 가능 (`#`) |
| 중첩 표현 | `{}`, `[]` | 들여쓰기 |
| 사용 사례 | API 응답, 데이터 교환 | 설정 파일 |

---

## 12. 실용 라이브러리

### 12.1 커맨드라인 인자 (`sys.argv`)

> 📄 파일: [`a113_main_argument.py`](basic/a113_main_argument.py)

```python
import sys

# python script.py arg1 arg2 ...
# sys.argv[0] = 스크립트 파일명
# sys.argv[1] = 첫 번째 인자

def main():
    if len(sys.argv) < 2:
        print("사용법: 로드할 파일을 명시하시오!")
        sys.exit()   # 프로그램 종료
    print("정상 작동")
```

---

### 12.2 로깅 (Logging)

> 📄 파일: [`a114_logger.py`](basic/a114_logger.py)

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="logger.log",   # 파일에 저장
    encoding="utf-8"
)

logging.debug("디버그 메세지")     # 개발 중 상세 정보
logging.info("프로그램 시작")      # 일반 정보
logging.warning("종료 직전")       # 주의사항
logging.error("에러 발생")         # 에러
logging.critical("치명적 오류")    # 치명적 에러
```

**로그 레벨 (낮은 것부터)**

```
DEBUG → INFO → WARNING → ERROR → CRITICAL
```

> `level=logging.DEBUG` 로 설정하면 DEBUG 이상 모든 레벨 출력됨

---

### 12.3 Matplotlib 그래프

> 📄 파일: [`a115_matplotlib_graph.py`](basic/a115_matplotlib_graph.py)

```python
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path(r"C:\segang\python\basic\__pycache__")
df = pd.read_csv(csv_path / "ta_20260527094029.csv")

df.info()   # 데이터 정보 출력
plt.plot(df['timestamp'], df['average'])  # x축: timestamp, y축: average
plt.show()  # 그래프 표시
```

---

### 12.4 HTTP 요청 (requests)

> 📄 파일: [`a100_request.py`](basic/a100_request.py)

```python
import requests

url = "https://naver.com"
response = requests.get(url)

print("status", response.status_code)  # 200이면 성공
print("text", response.text)           # HTML 본문
```

---

## 13. 데이터클래스 (`dataclass`)

> 📄 파일: [`a98_dataclass.py`](basic/a98_dataclass.py)

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    korean: int
    math: int
    english: int
    science: int

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

students = [
    Student("abc", 30, 65, 45, 44),
    Student("dfe", 30, 35, 85, 14),
]
print(students[1])          # Student(name='dfe', korean=30, ...) 자동 출력
print(students[0].get_sum())
```

**`@dataclass` 장점**

| 기능 | 일반 클래스 | `@dataclass` |
|------|-------------|--------------|
| `__init__` | 직접 작성 | 자동 생성 |
| `__repr__` | 직접 작성 | 자동 생성 |
| `__eq__` | 직접 작성 | 자동 생성 |
| 타입 힌트 | 선택적 | 필수 (가독성 향상) |

> `@dataclass`는 보일러플레이트 코드를 줄여주는 강력한 데코레이터. 데이터를 담는 클래스에 적극 활용하자.

---

## 📁 실습 파일 목록

| 파일명 | 주제 |
|--------|------|
| [`hello.py`](basic/hello.py) | Hello World, `__name__` |
| [`variable.py`](basic/variable.py) | 변수, 타입, 네이밍 컨벤션 |
| [`a02_keyword.py`](basic/a02_keyword.py) | 예약어 목록 |
| [`a04_print.py`](basic/a04_print.py) | print() 함수 |
| [`a08_str_indexing.py`](basic/a08_str_indexing.py) | 문자열 인덱싱/슬라이싱 |
| [`a19.py`](basic/a19.py) | for 루프, enumerate, zip |
| [`a21_list.py`](basic/a21_list.py) | 리스트 기초 |
| [`a22_list_function.py`](basic/a22_list_function.py) | 리스트 참조 전달 |
| [`a23_list_method.py`](basic/a23_list_method.py) | 리스트 메서드 |
| [`a25_dictionary.py`](basic/a25_dictionary.py) | 딕셔너리 |
| [`a30_list_comprehension.py`](basic/a30_list_comprehension.py) | 리스트 컴프리헨션 |
| [`a31_function.py`](basic/a31_function.py) | 함수 기초, 타입 힌트 |
| [`a32_argument.py`](basic/a32_argument.py) | 가변 인자 (`*args`) |
| [`a33_default_argument.py`](basic/a33_default_argument.py) | 기본값 인자 |
| [`a35_variable_length_keyword_argument.py`](basic/a35_variable_length_keyword_argument.py) | `**kwargs` |
| [`a42_file_write.py`](basic/a42_file_write.py) | 파일 쓰기 |
| [`a43_file_read.py`](basic/a43_file_read.py) | 파일 읽기 |
| [`a47_try_exception.py`](basic/a47_try_exception.py) | 예외 처리 |
| [`a63_class_student.py`](basic/a63_class_student.py) | 클래스 기초 |
| [`a64_class_method.py`](basic/a64_class_method.py) | 인스턴스 메서드, `__repr__` |
| [`a65_isinstance.py`](basic/a65_isinstance.py) | isinstance 함수 |
| [`a66_special_method.py`](basic/a66_special_method.py) | 스페셜 메서드 |
| [`a67_class_variable.py`](basic/a67_class_variable.py) | 클래스 변수, `@classmethod` |
| [`a68_Destructor.py`](basic/a68_Destructor.py) | 소멸자 (`__del__`) |
| [`a70_property.py`](basic/a70_property.py) | 프로퍼티, getter/setter |
| [`a71_class_inheritance.py`](basic/a71_class_inheritance.py) | 상속 |
| [`a72_multiple_inheritance.py`](basic/a72_multiple_inheritance.py) | 다중 상속, MRO |
| [`a80_fibonacci.py`](basic/a80_fibonacci.py) | 재귀 함수, 피보나치 |
| [`a81_fibonacci_chche.py`](basic/a81_fibonacci_chche.py) | 메모이제이션, `@cache` |
| [`a86_generator.py`](basic/a86_generator.py) | 제네레이터, `yield` |
| [`a90_package_import.py`](basic/a90_package_import.py) | 모듈/패키지 import |
| [`a98_dataclass.py`](basic/a98_dataclass.py) | `@dataclass` |
| [`a100_request.py`](basic/a100_request.py) | HTTP 요청 (requests) |
| [`a101_wrapper_function.py`](basic/a101_wrapper_function.py) | 래퍼 함수 |
| [`a102_decorator.py`](basic/a102_decorator.py) | 데코레이터 |
| [`a103_time_decorator.py`](basic/a103_time_decorator.py) | 실행 시간 측정 데코레이터 |
| [`a111_json_serialization.py`](basic/a111_json_serialization.py) | JSON 파싱 |
| [`a112_yaml_serialization.py`](basic/a112_yaml_serialization.py) | YAML 파싱 |
| [`a113_main_argument.py`](basic/a113_main_argument.py) | 커맨드라인 인자 |
| [`a114_logger.py`](basic/a114_logger.py) | 로깅 |
| [`a115_matplotlib_graph.py`](basic/a115_matplotlib_graph.py) | Matplotlib 그래프 |

---

*📅 최종 업데이트: 2026-05-27*
