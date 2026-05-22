# 이 파일은 처음 한번 실행된다.

from .module_a import module_var_a, module_a_func, module_a     # 내부 폴더의 module_a를 찾는다.
from .module_b import module_var_b, module_b_func, module_b

# __all__ = ["module_var_a", "module_var_b", "module_a_func", "module_b_func"]

def package_func():
    print("이것은 패키지 함수입니다")
    
# 패키지 테스트코드를 넣어서 쓸수도 있다. (__init__.py 단독으로 실행하여)
def main():
    print(module_a())
    print(module_b())
    print(module_a_func())
    print(module_b_func())
    print("test_package 패키지에서 실행되는 프린트다.")

if __name__ == "__main__": 
    main()
