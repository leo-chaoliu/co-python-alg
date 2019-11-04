from abc import ABC, abstractmethod     #Abstract Base Class
from StackBase import StackBase
from StackList import StackList

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- For Stack ADT Lab Question

- Basic documentation only

"""
def makeSorted( input ):
    """
    [input] is a list of numbers (refer to numList as defined in main function)

    This function print the list of numbers in ascending order.

    Restriction: Touch each number ONCE and no additional data structures 
    """

    #You are allowed to change the name of the stack to improve
    # readability. Other than that, you CANNOT declare / use additional variables
    
    storeStack = StackList() 
    changeStack = StackList()
    
    #Similarly the output list should only be used to stored the sorted number
    result = []

    #You can only access the number in list in this loop ONCE
    
    n = len(input)
    storeStack.push(input[0])

    for i in range(1,n):
        if input[i] < storeStack.getTop():
            storeStack.push(input[i])
        
        else:
            
            while input[i] >= storeStack.getTop():
                temp = storeStack.getTop()
                storeStack.pop()
                changeStack.push(temp)
           
            storeStack.push(input[i])
           
            for k in range(changeStack.size()):
                temp = storeStack.getTop()
                changeStack.pop()
                storeStack.push(temp)
    
    for i in range(storeStack.size()):
        temp = storeStack.getTop()
        storeStack.pop()
        result.append(temp)

    #You can have code outside of the loop if needed

    return result



def main():
    # sList = input("Give a list of numbers: ").split(" ")
    # numList = [int(s) for s in sList]
    #numList is a list of numbers now
    # result = makeSorted(numList)
    result = makeSorted([4,8,6,5,9,7])
    

    print(numList)
    print(result)


if __name__ == "__main__":
    main()