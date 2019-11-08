
def filter_Target(L, target):
    '''

    ''' 
    
    # iterative thinking: looping through the L, if the same will not add to result List
    # using recursion winding or unwinding phase to get each char, then do operation base on return ans

    # base case
    if len(L) == 0:
        return []
    
    # reduced problem 
    last_number = L.pop();
    ans = filter_Target(L, target)

    if last_number == target:
        return ans
    else:
        ans.append(last_number)
        return ans

def filter_Target_Winding(L, target):
    
    if len(L) == 0:
        return []

    # get the first number and remove it from the list
    first_number = L.pop(0)

    if first_number == target:
        print("Equal")
    else:
        print(first_number)

    ans = filter_Target_Winding(L, target)

    
    pass

def main():
    print(filter_Target([4,2,3,4,2],4))
    pass

if  __name__ == "__main__":
    main()
    pass
