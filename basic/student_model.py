import random
from pathlib import Path
import pickle
from student_model import student

def main():
    path = Path(r"C:\segang\python\basic\__pycache__\test.pickle")
    hanguls = list("최강박이손정적고구류")
    hanguls2 = list("가나다라마바사아자차카타파하김님딤형준장정성깅궭쀍")
    students = [
        student(
            random.choice(hanguls)+"".join(random.choices(hanguls2, k=2)),
            random.randint(65,100),
            random.randint(65,100),
            random.randint(65,100),
            random.randint(65,100),
        )
        for _ in range(100)
    ]
    
    student.print()
    with path.open("wb") as f:
        pickle.dump(students, f)    
        
    
if __name__ == "__main__":
    main()