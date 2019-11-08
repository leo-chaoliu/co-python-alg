from abc import ABC, abstractmethod     #Abstract Base Class
import math

#Our own stack implementations
from StackList import StackList
from StackLinkedList import StackLinkedList

def main():
    #Python List Implementation
    mystack = StackList()

    #Linked List Implementation
    #mystack = StackList
    
    #Initialize the first two fibonacci numbers
    mystack.push( 1 )
    mystack.push( 1 )

    for i in range(10):
        prev1 = mystack.getTop( )
        mystack.pop( )
        prev2 = mystack.getTop( )

        cur = prev1 + prev2
        
        mystack.push( prev1 )
        mystack.push( cur )
        
        print(cur)

if __name__ == "__main__":
    main()

