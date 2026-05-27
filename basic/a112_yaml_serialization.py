#yaml으로 파일 불러오기
# pip install pyyaml

import yaml
from pathlib import Path

def main():
    path = Path(r"C:\segang\python\basic\__pycache__\test.yaml")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) #yaml.safe_load를 사용
        print(data)
        print(type(data))
        print(data["abc"])
        print(data["subject"]["korean"])

if __name__ == "__main__":
    main()