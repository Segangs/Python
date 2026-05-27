import rust_hello

def main():
    print(rust_hello.make_greeting)
    print(rust_hello.add(10,20))
    a = cpp_hello.hello("aaa")
    print(a.greet())
    
if __name__ == "__main__":
    main()