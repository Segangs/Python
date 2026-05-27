# 클래스 변수

class Student:
    count = int() # 이것이 클래스의 변수
    students = list() # 리스트
    
    def __init__(self, name, korean, math, english, science): # 초기화 (생성자는 아님)
        count1 = int() # 여기다 넣으면 함수의 변수가 된다. (1회용으로 쓰고 싶을때)
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self) # 객체가 생성되었을때 리스트에 본인을 집어넣음.
        
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}"
    
    def __repr__(self):
        return f"{self.name}\t\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t {self.get_sum()}\t {self.get_average()}"
    
    # 스트링메소드
    def __str__(self) -> str:
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t {self.get_sum()}\t {self.get_average()} str"
    
    # 사칙연산 메소드
    def __add__(self, other) : 
        return self.get_sum() + other.get_sum()
    
    def __sub__(self, other) : 
        return self.get_sum() - other.get_sum()
    
    def __mul__(self, other) : 
        return self.get_sum() * other.get_sum()
    
    def __truediv__(self, other):
        return self.get_sum() / other.get_sum()
    
    
    # 관계 연산자 메소드 
    # greater than : gt / less than : lt / equal : eq / negative : ne / grater than equql : ge / less than equal : le
    
    def __gt__ (self, value):
        if isinstance(value, Student) : 
            return self.get_sum() > value.get_sum()
        else :
            return "error"
            raise
        
    @classmethod
    def print(cls): #self가 안들어가고 클래스 자체가 들어간다.
        print("이름\t 국어\t 수학\t 영어\t 과학\t 총점\t 평균")
        print()
        print("------------------학생 목록 ------")
        for student in Student.students:
            print(student)
        print("---------------------------------")
            
    
def main():
    Student("abc", 30, 65, 45, 44)
    Student("dfe", 30, 35, 85, 14)
    Student("vdw", 37, 65, 96, 24)
    Student("fsa", 38, 65, 75, 34)
    Student("ggg", 39, 12, 14, 44)
    Student("eee", 12, 18, 35, 74)
    Student("qqq", 66, 65, 55, 84)
    print(f"등록된 학생 수는 {Student.count}")
    Student.print()
    
        
        

        

if __name__ == "__main__":
    main()