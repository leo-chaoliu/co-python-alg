def logN(N, B):

    if N < B:
        return 0
    
    ans = 1 + logN(N/2,B)

    return ans

l= logN(7,2)
print(l)


def listTest():
    
    new_list = [[] for i in range(10)]
    return new_list
    pass

print(listTest())
