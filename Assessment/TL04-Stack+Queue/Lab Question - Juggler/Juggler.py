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
    [input] is a list of numbers

    This function print the list of numbers in ascending order.

    Restriction: Touch each number ONCE and no additional data structures 
    """

    #You are allowed to change the name of the stack to improve
    # readability. Other than that, you CANNOT declare / use additional variables
    S1 = StackList() 
    S2 = StackList()
    #Similarly the output list should only be used to stored the sorted number
    result = []

    #You can only access the number in list in this loop ONCE
    for num in input:
        pass

    #You can have code outside of the loop if needed

    return result



def main():
    sList = input("Give a list of numbers: ").split(" ")
    numList = [int(s) for s in sList]
    #numList is a list of numbers now

    printSorted(numList)


if __name__ == "__main__":
    main()