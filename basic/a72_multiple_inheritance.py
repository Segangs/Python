# 다중 상속

class Person:
    def __init__(self,b):
        self.b=b
    def greeting(self):
        print("안녕하세요")
        
class University:
    def __init__(self, a):
        self.a = a
        
    def message_credit(self):
        print("학점관리")
        

class Undergraduate(Person, University):
    def __init__(self):
        Person.__init__(self, 1) 
        University.__init__(self, 2)  # super를 쓰지 않고도 self를 사용하면 불러올수 있다.
        
    def study(self):
        print("공부하기")
        

def main():
    james = Undergraduate()
    james.greeting()
    james.message_credit()
    james.study()
    print(james.a, james.b)
    print(Undergraduate.__mro__[1].__dict__) # mro를 지원한다.
        
if __name__ == "__main__":
    main()