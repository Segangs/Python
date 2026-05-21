print("hello, world")


def main():
    print("hello world2")
    print(__name__)

if __name__ == "__main__":   # import를 당했을 때 __main__이 아니게 된다.
    main()
