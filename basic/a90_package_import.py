# 모듈 만들기
# from 파일명 import 함수명 as 단축어

# 유명한 라이브러리 이름을 파일로 만들면 안된다.


# from .module_a import module_var_a #내부 폴더의 module_a를 찾는다.
# from .module_b import module_var_b
from test_package import *    # __init__.py를 만들면 위 두 문장을 포함하여 쓸수있음.

def main():
    print(module_var_a)
    print(module_var_b)
    module_a_func()
    print(module_var_a)


if __name__ == "__main__": 
    main()
