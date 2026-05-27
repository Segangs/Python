class Student:
    def study(self):
        print("studying")
        
class Teacher:
    def teach(self):
        print("teaching")
        
def main():
    student = Student()
    classroom = [Student(), Student(), Teacher(), Teacher(), Teacher()]
    
    
    # 클래스의 인스턴스인지 확인하는 함수. 어떤 클래스의 인스턴스인지 확인해 준다.
    print(isinstance(student, Student)) #True
    print(isinstance(student, int)) # False
    print(isinstance(student, object)) # True. 모든 파이썬의 클래스는 object를 상속받는다.
    
    print(isinstance(1, object))# True.
    print(isinstance([1,2,3, student], object)) # True. 모든 파이썬의 클래스는 object를 상속받는다.
    
    for person in classroom:
        if isinstance(person, Student):
            person.study() 
        if isinstance(person, Teacher):
            person.teach()   


if __name__ == "__main__":
    main()