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
    # during the winding phase, string input have loggest lenth, which able to be accesed at the end
    # so if we want to reverse the string, get the last one in each winding iteration
    print("{} -> ".format(str_[n-1]))
    print("{} -> ".format(str_[0]))
    
    reverse_string_inner(str_, n-1)
    
    # during unwind phase, the string from length of 0 to grows logger, 
    # so we could get the string in order in this stage 
    print("--unwind--")
    print("{} -> ".format(str_[n-1]))
    print("{} -> ".format(str_[0]))

    pass

if __name__ == "__main__":
    reverse_string("abcdefg")
    pass