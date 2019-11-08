from abc import ABC, abstractmethod     #Abstract Base Class
from StackBase import StackBase
from StackList import StackList

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- For Stack ADT tutorial

- Basic documentation only

"""

def whichIsMore( input ):
    """
    [input] is a string, where each character is '1' or '0'.
    Return:
    = 1 if there are more 1’s than 0's
    = 0 if there are more 0’s than 1's
    = -1 if there are equal number of 1’s and 0’s

    Restriction: You are not allowed to count the numbers of 1’s and 0’s. 
    """
    return 0


def main():
    s = input("Give a string of 1s and 0s: ")

    result = whichIsMore(s)
    if result == 1:
        print("1s more than 0s")
    elif result == 0:
        print("0s more than 1s")
    else:
        print("Same number of 1s and 0s")


if __name__ == "__main__":
    main()