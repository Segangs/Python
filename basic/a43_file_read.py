# 객체 직렬화 + 파일 디스크립터

import sys
from pathlib import Path


def main():
    path = Path(r"C:\segang\python\basic\__pycache__") 
    with open(path / "text.txt", "r", encoding="utf-8") as f:    # r로 하면 read
        # data = f.readlines() # 리스트로 읽어온다.
        # print(data)
        # for str in data:
        #     print(str)
            
        # data = f.read()  #read함수를 이용하면 한꺼번에 읽어옴
        # print(data)
    
        data = f.readline()
        print(data) #한줄씩 읽는다. 라인 읽은 위치를 기억하고 있다.
        data = f.readline()
        print(data) #한줄씩 읽는다. 라인 읽은 위치를 기억하고 있다.
        data = f.readline()
        print(data) #한줄씩 읽는다. 라인 읽은 위치를 기억하고 있다.
        data = f.readline()
        print(data) #한줄씩 읽는다. 라인 읽은 위치를 기억하고 있다.
        
        # 파일이 굉장히 클때 사용 (한줄씩 계속 읽음)
        while data := f.readline():
            print(data)
    
    
    
    # 
    print(sys.stdin.fileno())
    print(sys.stdout.fileno())
    print(sys.stderr.fileno()) #버퍼 없이 바로 출력
    print("error message", file=sys.stderr)
    with open(path / "text.txt", "a", encoding="utf-8") as f:
        print("이것은 프린트로 파일을 쓴 데이터이다.", file=f)
    

if __name__ == "__main__":
    main()