def remFirst(L,target):
    if L==[]:
        return []

    if L[0] == target:
        return L[1:]
    else:
        return [L[0]] + remFirst(L[1:],target)

L = [1,3,2,5,2,2]
hh = remFirst(L,2)
print(hh)
