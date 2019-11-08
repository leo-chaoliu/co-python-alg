from abc import ABC, abstractmethod     #Abstract Base Class
from StackBase import StackBase
from StackList import StackList
import operator                         #only for advanced version

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- For Stack ADT tutorial

- Basic documentation only

"""

def evaluatePostfix( eList ):
    """
    [eList] is a List of strings. Each strings is either and operand, e.g. "123"; or an operator, e.g. "+".

    This function returns the result (a single integer value) of evaluating the postfix expression.
    """
    return 0

def main():
    print("Give a postfix expression (space between number and operator)")
    s = input("> ")

    sList = s.split(" ")
    print(sList)
    print("Result is "+ str(evaluatePostfix(sList)))



if __name__ == "__main__":
    main()