# 프로퍼티 만들기,   getter, setter
# Descriptor -> attr, getattr, setattr, delattr

import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    

    
    @property
    def radius(self):
        return self.__radius #. 2. 이게 나옴
    
    @radius.getter
    def radius(self) :
        print("getter") 
        return self.__radius
    
    @radius.setter
    def radius(self, value) : 
        print("setter")
        if isinstance(value, int) and value >0:
            self.__radius = value
        else:
            print("임의 정수만 넣으시오")
    
    
    def get_area(self):
        return math.pi * (self.__radius**2)
        
def main():
    circle = Circle(10)
    print(circle.radius) # 1. 이걸 실행하면 (소괄호를 안붙이고 변수처럼 사용)
    circle.radius = 20
    circle.radius = 3.14
    circle.radius = -5
    print(circle.get_area())
    
    # descriptor
    print(circle.__dict__)
    print(vars(circle))
    print(getattr(circle, "get_area"))
    print(getattr(circle, "get_area")())
    print(getattr(circle, "get_area2", None))
    
    # _의 쓰임
    for i in range(100):
        print ("<loop>", end="")
    
    for _ in range(100):
        print ("[loop]", end="")
        
    a_tu = 1,2,3,"valuable text"
    _ ,_, _, text = a_tu
    print(text)
    
    
if __name__ == "__main__":
    main()