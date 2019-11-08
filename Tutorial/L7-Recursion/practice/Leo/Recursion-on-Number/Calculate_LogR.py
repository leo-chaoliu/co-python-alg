
def calculate_LogR_Wrapper(N,B):
    result = []

    calculate_LogR_2(N,B, result)

    return result

    pass

def calculate_LogR_2(N, B, result):
    '''
    Give a recursive function logR(N,B) that takes in a number N and abase B,
    both positive(i.e.>0). The function returns ceiling of log B (N).
    e.g. LogR(7, 2) = 2
    ''' 

    # count how many times B could repeat itself until it above N
    # each recursion accumulate 1 to it's ans

    # base case
    if N < B:
        return 
    
    # reduced problem logR(N//B, B)
    calculate_LogR_2(N//B, B, result)

    result.append(1)

    return

def calculate_LogR(N, B):
    '''
    Give a recursive function logR(N,B) that takes in a number N and abase B,
    both positive(i.e.>0). The function returns ceiling of log B (N).
    e.g. LogR(7, 2) = 2
    ''' 

    # count how many times B could repeat itself until it above N
    # each recursion accumulate 1 to it's ans

    # base case
    if N < B:
        return 0
    
    # reduced problem logR(N//B, B)
    ans = 1 + calculate_LogR(N//B, B)
    return ans

def main():
    print(calculate_LogR(7, 2))
    print(calculate_LogR(1234, 10))
    print(calculate_LogR_Wrapper(1234, 10))

    pass

if  __name__ == "__main__":
    main()
    pass
