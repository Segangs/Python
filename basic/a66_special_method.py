# 스페셜 메소드

class Student:
    def __init__(self, name, korean, math, english, science): # 초기화 (생성자는 아님)
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}"
    
    def __repr__(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t {self.get_sum()}\t {self.get_average()}"
    
    # 스트링메소드
    def __str__(self) -> str:
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t {self.get_sum()}\t {self.get_average()} str"
    
    # 사칙연산 메소드
    def __add__(self, other) : 
        return self.get_sum() + other.get_sum()
    
    def __div__(self, other) : 
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
    
def main():
    students = [
        Student("abc", 30, 65, 45, 44),
        Student("dfe", 30, 35, 85, 14),
        Student("vdw", 37, 65, 96, 24),
        Student("fsa", 38, 65, 75, 34),
        Student("ggg", 39, 12, 14, 44),
        Student("eee", 12, 18, 35, 74),
        Student("qqq", 66, 65, 55, 84),
    ]
    
    print("student[0] > student[1]", students[0] > students[1])
    print("student[0] > student[1]", students[0] > 90)
    print("student[0] + student[1]", students[0] + students[1])
    print("student[0] - student[1]", students[0] - students[1])
    print("student[0] * student[1]", students[0] * students[1])
    print("student[0] / student[1]", students[0] / students[1])
        

if __name__ == "__main__":
    main()