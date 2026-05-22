# 함수 안의 아규먼트를 수정하는 방법은 아래와 같은 방식도 있다.

# 리스트에서 사용할수 있는 메소드.
# 리스트 뒤에 [1,2,3]. 을 붙이면 사용할 수 있는 메소드들 나옴..
# 여러가지 기능들을 제공한다.

import datetime

def main():
    list_a = [1,2,3]
    list_b = [4,5,6]
    
    # return 결과를 수정
    print(list_a + list_b)
    print(list_a.__add__(list_b)) # c++ 의 연산자 오버로딩과 같은..
    
    # elephant sign
    print(list_a := list_a.__add__(list_b))    
    
    # list 자체를 수정
    list_a.extend(list_b)
    print(list_a)
    
    # *연산
    print(list_a * 4)
    print(list_a.__mul__(4))
    
    # append(리스트에 값을 추가하는 함수. 많이 씀.)
    list_b.append("추가 원소")
    print(list_b)
    
    # insert(삽입)
    list_b.insert(3, 7)
    print(list_b)
    
    # 삭제
    print(list_b.pop()) # 자료를 빼서 쓰고 싶을때 사용 (리스트에서 삭제됨)
    print(list_b)
    print(list_b.pop(0))
    print(list_b.remove(6))
    print(list_b)
    
    # 메모리 삭제
    del list_e[4]
    print(list_e)
    
    # del 사용자 정의 객체를 삭제 하는 경우
    print(list_e)
    ptime = datetime.datetime.now()
    list_e.append(ptime)
    print(list_e[16])
    print(list_e)
    
    # 리스트에서 값 찾기
    list_b = ['a','b','c','d','e','f']
    list_e = [*str("abcdef jang segang")]
    print(list_b.index("e"))
    print(list_e)
    
    print("k" in list_e)  # k가 리스트 e에 있나? False
    print("g" in list_e)  # g가 리스트 e에 있나? True
    
    #리스트 길이 구하기
    print(list_e.__len__())
    print(len(list_e))
    
    


if __name__ == "__main__":
    main()