class A:
    pass

def main():
    dict_a = {}
    dict_b = dict()
    print(type(dict_a))  # <class 'dict'>
    print(type(dict_b)) # <class 'dict'>
    
    #set이랑 햇갈릴수 있음.
    set_a = {1,2}
    print(type(set_a)) #<class 'set'>
    a = A()
    dict_c = {"a":1234, "b":879, "c":876, 1234:5678, 3.14:1111, a:4.4444,} #<class 'dict'>
    print(type(dict_c)) #<class 'dict'>
    print(dict_c) # {'a': 1234, 'b': 879, 'c': 876}
    print(dict_c[a])
    print(dict_c[3.14])
    print(dict_c["c"])
    
    

if __name__ == "__main__":
    main()