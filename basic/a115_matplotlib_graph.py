import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    csv_path = Path(r"C:\segang\python\basic\__pycache__")
    df = pd.read_csv(csv_path / "ta_20260527094029.csv")
    df.info()
    # plt.figure(figsize(12,6))
    plt.plot(df['timestamp'], df['average'])
    plt.show()

    
if __name__ == "__main__":
    main()