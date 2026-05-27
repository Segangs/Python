# 클래스 만들기

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
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
    print("이름\t 국어\t 수학\t 영어\t 과학")
    for student in students:
        print (f"{student.name}\t {student.korean}\t {student.math}\t {student.english}\t {student.science}")

if __name__ == "__main__":
    main()