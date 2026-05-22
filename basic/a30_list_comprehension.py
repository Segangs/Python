# 리스트 컴프리헨션
# 

import random

def main():
    # 결과 for 변수 in 컨테이너 (1,2,3,4) if 조건(else붙이는건 안됨)
    li = [i+1 for i in range(100) if i % 2 ==0] # 100 이하의 홀수만 리스트에 들어가도록 함
    random.shuffle(li) # 랜덤섞기도 가능
    print(li)
    
    
    li = [i**2+1 for i in range(100) if i % 2 ==0] # 제곱해서 더하기 1
    random.shuffle(li) # 랜덤섞기도 가능
    print(li)
    print(min(li), max(li), sum(li))
    li.sort()
    print(li)
    li.sort(reverse=True)
    print(li)

if __name__ == "__main__":
    main()