def reverse_string_2(str_):
    n = len(str_)
    
    if n == 0: 
        return None

    print("{} -> ".format(str_[n-1]))
    reverse_string_2(str_[:n-1])

    pass


def reverse_string(str_):
    n = len(str_)
    reverse_string_inner(str_, n)

def reverse_string_inner(str_, n):
    if n == 0: 
        return None

    print("--wind--")
    print("{} -> ".format(str_[n-1]))
    
    reverse_string_inner(str_, n-1)
    
    print("--unwind--")
    print("{} -> ".format(str_[n-1]))

    pass

if __name__ == "__main__":
    reverse_string("leovsmolly")
    pass