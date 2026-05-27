#  스레드를 이용

import threading
import time

total = 0  #각 스레드에서 total 에 동시 접근하도록 해보면?

#GIL - global interpreter lock : 스레드가 동시에 접근할수없게 만드는..
#race condition을 없앨려면 아래와 같이 뮤텍스를 적용한다..

lock = threading.Lock()

def task(name, duration):
    global total
    print(f"스레드 {name} 시작")
    for _ in range(1_000_000):
        with lock:    #  LOCK을 걸면 더 안전하게 연산
            total += 1
    time.sleep(duration)
    print(f"스레드 {name} {duration}초 후 완료")


def main():
    # task("first", 5)
    # task("second", 5)
    
    # 스레드를 이용
    threads =[]
    for i in range(4):
        t = threading.Thread(target=task, args=(f"T{i+1}", 5 + i))
        threads.append(t)
        t.start() # 실제 함수가 실행 되는 라인
        
        
    #스레드가 다 끝날때까지 기다리는 함수 join
    for t in threads:
        t.join() # Block 후 아래로 내려감
    
    print("main은 언제 실행될까요?")

if __name__ == "__main__":
    main()