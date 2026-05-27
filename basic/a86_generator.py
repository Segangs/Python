#제네레이터 사용
# yield와 같이 사용한다.
# 객체가 반환되기때문에 사용방법은 불편 (for문과 엮어서 쓴다)

def test():
    print("TEST A")
    # return 0
    yield 0
    print('test B')
    yield 1
    
def main():
    generated_func = test()
    #print(generated_func.__next__())
    print(next(generated_func))
    print(next(generated_func))
    
    
    try:
        print(next(generated_func))
    except StopIteration:
        print("generator end")
    print ("main C")

if __name__ == "__main__":
    main()