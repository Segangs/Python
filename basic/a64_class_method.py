# 클래스 만들기

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
    
    # print(Student)
    # print(students[0])
    
    print("이름\t 국어\t 수학\t 영어\t 과학\t 총점\t 평균")
    for student in students:
        #print(student.to_string()+f"\t{student.get_sum()}\t"+f"{student.get_average()}")
        print(student)  # __repr__에 감춰두고 불러온다. (윗줄과 같은 결과)
        

if __name__ == "__main__":
    main()