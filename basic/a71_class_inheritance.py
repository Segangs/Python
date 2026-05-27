# 클래스의 상속

class Parent:
    def __init__(self, value):
        self.value = "테스트"
        self.value2 = value
        print("Parent 클래스의 __init__ 메소드가 호출되었다.")
        
        
    def test(self):
        print("parent 클래스의 test메소드 입니다.")
        
        
class Child(Parent):
    def __init__(self, value):
        super().__init__("child에서 넘어간 값")  #꼭 슈퍼를 통해 부모 클래스를 불러오고 init로 초기화 해야한다.
        print("child 클래스의 __init__ 메소드가 호출되었다.")
        
     
    # 함수에 대해서 파이썬에서는 오버로딩이 없다. 오버라이딩만 있다.
    def test(self, *args):
        print("child 클래스의 test메소드 입니다.")

        
def main():
    pObject = Parent("부모 자료")
    pObject.test()
    
    child = Child("자식 자료")
    child.test()
    child.test(111)
    print(child.value)
    print(child.value2)
    
    
if __name__ == "__main__":
    main()