# 리스트 만들기

import datetime

def main():
    list_a = []  # 리스트 선언
    list_b = list()  # 클래스로도 선언 가능
    list_c = [1, 2, 3, 4, 5, 6]

    print(list_a, list_b, list_c)
    print(type(list_a), type(list_b), type(list_c))

    ptime = datetime.datetime.now()
    list_d = [1, 2, 3.141592, "choi", ptime]
    print(list_d)
    print(list_d[3]) # 3번 가져와
    list_d[3] = "kim" # kim으로 변경
    print(list_d[3]) # 3번 가져와
    
    list_e = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(list_e)
    print(list_e[1][1])


if __name__ == "__main__":
    main()
