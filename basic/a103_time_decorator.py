#decorator
#wrap으로 앞뒤로 코드를 감싼다.
# 시작시간 잰 후 함수 종료를 재서, 함수의 실행 시간을 측정하는데 쓰기도 한다.

from functools import wraps
import time

def runtime_check(n):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"func 실행 전 코드..{n} / 함수이름 : {func.__name__}")
            start_time = time.time()
            for i in range(n):
                result = func(*args, **kwargs)
            end_time = time.time()
            print(f"실행 시간은 {(end_time - start_time) /n:.3} 입니다.")
            return result
        return wrapper
    return my_decorator


@runtime_check(3) # 3번 반복해 본다.
def print_hello(n,s):
    for _ in range(n):
        s += 1
    return s


def main():
    re = print_hello(50_000_000, 10_000_000)
    print(re)
    

if __name__ == "__main__":
    main()