from dataclasses import dataclass

@dataclass
class Student:
    name : str
    korean : int
    math : int
    english : int
    science : int
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
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
    print(students[1])
    print(students[0].get_sum())


if __name__ == "__main__":
    main()