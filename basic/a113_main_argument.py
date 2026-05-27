# int main(int argc, char *argv[]) -> 이건 파이썬으로 못할까? 구현해 보자.
# 파일명 뒤에 argument를 붙여 보내야 한다.

# argparser 라이브러리(패키지) 를 사용하면 된다.

# (base) C:\segang\python>C:\ProgramData\miniconda3\python.exe c:/segang/python/a103_main_argument.py
# 사용법 : 로드할 파일을 명시하시오!
# (base) C:\segang\python>C:\ProgramData\miniconda3\python.exe c:/segang/python/a103_main_argument.py wqerqwrweqr
# 정상 작동


import sys

def main():
    sys.argv[0]
    sys.argv[1]
    
def main():
    # print(sys.argv[0])
    # print(sys.argv[1])
    
    if len(sys.argv) < 2 :
        print("사용법 : 로드할 파일을 명시하시오!")
        sys.exit()
    # with open(argv[1]) as f:
    #     pass
    
    print("정상 작동")
    
   
    

if __name__ == "__main__":
    main()