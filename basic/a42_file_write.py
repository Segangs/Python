# 객체 직렬화

from pathlib import Path

def main():
    path = Path(r"C:\segang\python\basic\__pycache__")
    # f = open(path + "\\text.txt", "w")  # fopen이 없고 파이썬에서는 open만 있다.
    # f.write("Hello Python Programming...!")
    # f.close()
    
    with open(path / "text.txt", "a", encoding="utf-8") as f:    # 위와 같이 쓰지 말고 with를 쓰면 close까지 같이 해줌
        f.write("hello!!!")
    
    

if __name__ == "__main__":
    main()