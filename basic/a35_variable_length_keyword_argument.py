# 키워드 아규먼트
# args -> tuple
# kargs -> dict(key:value, ...)

def print_n_times(*args, **kargs):
    for value in args:
        print("여기는 아규먼트")
        print(value)
    for value in kargs:
        print("여기는 키워드 아규먼트")
        print(value)
    for key, value in kargs.items():
        print("딕셔너리 문법 사용")
        print(key, value)


def main():
    print_n_times(1,2,3,4,5,6) #아규먼트만 나옴
    print_n_times(1,2,3,4,5,6,a=1,b=2,c=3) # 키워드 아규먼트도 나옴
    
if __name__ == "__main__":
    main()