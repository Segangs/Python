#피보나치 수열을 이용하여 성능 측정
# cache를 사용하면 빨라지나, 많이 돌리는 함수에만 붙이는게 좋다.

from functools import cache

cnt = 0

@cache
def fibonacci(n):
    global cnt
    cnt += 1
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def main():
    global cnt
    print(fibonacci(36))
    print(f"fibonacci 가 수행된 횟수 {cnt}")
    
  

if __name__ == "__main__":
    main()