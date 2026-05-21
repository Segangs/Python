class A:
    def __repr__(self):
        return "this is class A!!"

def main():
    print(12345)
    print(1_234_567)
    print("Segang")
    print(3.141562)
    print('python "class"')

    print("this is", "python", "Class")
    print(10,20,30, "hi", "fifty")
    print()

    print("this is", "python", "Class!!", sep="_", end="")
    print("this is", "python", "Class!!", sep=".")
    
    print(A())
    print(type(A()))
    

if __name__ == "__main__":
    main()