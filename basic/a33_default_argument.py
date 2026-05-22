def print_n_time(
    *value: str,
    n: int = 2,   #defult 값을 줌
    
) -> str:
    """_summary_
    교육용 테스트 함수이다.
    Args:
        value (str): 출력할 메세지
        n (int): 반복 출력횟수

    Returns:
        str: 에러 반환
    """
    print(type(value))
    # temp1, temp2, temp3 = value
    # (temp1, temp2, temp3) = (first, second, third)
    for i in range(n):
        print(value)
        # print("first", temp1, "sencond", temp2, "third", temp3)
        for v in value:
            print(v, end=" ")
        print("\n\n")
    return "ok"


def print_keyword_argument(a,b,c,d=5,*e):
    print(a,b,c,d,e)

def main():
    return_var = print_n_time("abc", "def", "ghi", "ddd")
    return_var = print_n_time("abc", "def", "ghi", "ddd", n=4)  # n=4
    print(type(return_var))
    print(*return_var)
    
    print_keyword_argument(1,2,3,4,5,6,7)
    print_keyword_argument(1,2,3)


if __name__ == "__main__":
    main()