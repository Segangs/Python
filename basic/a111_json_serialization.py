#json으로 파일 불러오기

import json
from pathlib import Path

def main():
    path = Path(r"C:\segang\python\basic\__pycache__\test.json")
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
        print(data)
        print(type(data))
        print(data["abc"])
        print(data["subject"]["korean"])

if __name__ == "__main__":
    main()