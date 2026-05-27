#디스트럭터 (소멸자 같은 개념..)

class Test:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 이 생성 되었습니다.")
        
    def __del__(self):
        print(f"{self.name} - 파괴 되었습니다.")
        
#def __new__(self)

#파이썬 객체는 내부말고 외부에서 관리를 한다.


def main():
    a = Test("a")
    b = Test("b")
    c = Test("c")
    print(a,b,c)
    del c  
    
if __name__ == "__main__":
    main()
    #메인함수가 종료되면서 하나씩 파괴된다.
    