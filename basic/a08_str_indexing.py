# str 인덱싱과 슬라이싱

def main():
    print("안녕하세요")    
    str_var = "안녕하세요"
    print(str_var[0]) # 안
    print(str_var[1]) # 녕
    print(str_var[2]) # 하
    print(str_var[3]) # 세
    print(str_var[4]) # 요
    # str_var[5] = "여" 안됨
    str_var = str_var.replace("요", "여")


    for c in str_var: # 5번 실행
        print("for로 불러온 원소" , c)
        
    str_var *= 3 #
    print(str_var[5:10]) # 5번째부터 10번째까지 자르겠다 slicing
    print(str_var[-3]) # -5 -4 -3 -2 -1 0
    print(str_var[5:10:2]) # 2는 stop
    print(str_var[-1::-1]) # -5 -4 -3 -2 -1 0 원소 거꾸로 출력 
    print("str_var 길이", len(str_var))
    print("str_var 길이", str_var.__len__())
    
    
if __name__ == "__main__":
    main()