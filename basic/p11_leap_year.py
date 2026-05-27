"""
Practice 011. 윤년 판정

난이도: beginner
수업 순서: 011
학습 주제: 조건문
관련 기본 예제: basic/a18-a20

문제:
    연도를 받아 윤년 여부를 반환하세요.

예시:
    - 2024 -> True

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 11
TOPIC = "조건문"
TITLE = "윤년 판정"


def is_leap_year(year: int) -> bool:
    """문제 요구사항에 맞게 구현하세요.
    
    윤년(Leap year) 판정 조건:
    1. 연도가 4로 나누어 떨어지면 윤년입니다.
    2. 단, 연도가 100으로 나누어 떨어지면 윤년이 아닙니다 (평년).
    3. 하지만, 연도가 400으로 나누어 떨어지면 다시 윤년이 됩니다.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    print(f"Practice {ORDER:03d}: {TITLE}")
    print(f"난이도: {LEVEL} | 주제: {TOPIC}")
    
    # 테스트 예시들
    test_years = [2024, 2000, 1900, 2023, 2100]
    print("\n--- 윤년 판정 테스트 결과 ---")
    for year in test_years:
        result = is_leap_year(year)
        status = "윤년 (Leap Year)" if result else "평년 (Common Year)"
        print(f"연도: {year} -> 결과: {result} ({status})")


if __name__ == "__main__":
    main()
