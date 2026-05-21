def main():
    list1 = ["a", "b", "c", 1, 2, 3]
    list2 = ["에이", "비", "씨", "one", "two", "three"]
    
    # 파이썬 스타일 (pydentic code)
    for ele in list1:
        print (ele)
    
    # C스타일.. 나쁜 예
    for i in range(len(list1)):
        print(list1[i], i)
        print(list1[i], list2[i])

    #  루프의 횟수를 체크를 해야 하는 경우 (파이썬 스타일)
    for i, ele in enumerate(list1):
        print(ele, i)
    for ele1, ele2 in zip(list1, list2):  #zip으로 묶는다
        print(ele1, ele2)

if __name__ == "__main__":
    main()
    
    
# a
# b
# c
# 1
# 2
# 3
# a 0
# a 에이
# b 1
# b 비
# c 2
# c 씨
# 1 3
# 1 one
# 2 4
# 2 two
# 3 5
# 3 three
# a 0
# b 1
# c 2
# 1 3
# 2 4
# 3 5
# a 에이
# b 비
# c 씨
# 1 one
# 2 two
# 3 three