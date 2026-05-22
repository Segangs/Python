# 리스트

# 파이썬에서도 글로벌 변수가 있으나 가급적 안쓰는게 좋다. (dependency)
# 리스트를 만들어서 감싸서 넘긴다.
# 리스트의 값이 넘어가는게 아니고 메모리 정보가 넘어감 (C의 포인터와 유사)
# 파이썬은 기본적으로 값을 복사하지만 리스트같은 컨테이너 개체들은 값이 아니라 메모리를 다룬다.


def make_20(var_a_b):
    var_a_b[0] = 20

def main():
    ver_a = 10
    #...
    # global ver_a
    wrapper_list = [ver_a]
    make_20(wrapper_list)
    var_a = wrapper_list[0]
    print(var_a) # 20
    
    list_a = [1,2,3]   # 리스트 뒤에 [1,2,3]. 을 붙이면 사용할 수 있는 메소드들 나옴..
    list_b = [4,5,6, list_a] # 값의 복사가 아니고 메모리를 참조한다.
    
    print(list_b)
    list_a[2] = 30
    print(list_b)
    

if __name__ == "__main__":
    main()