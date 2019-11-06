from abc import ABC, abstractmethod     #Abstract Base Class
from SinglyNode import SinglyNode
from StackBase import StackBase


"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- Implemented Stack (LIFO order) ADT:
    - Specification:  StackBase Base Class
    - Implementations: 
        A. Python List (StackArray Class)
        B. LinkedList (StackLinkedList Class)

- Basic documentation only

"""

class StackLinkedList(StackBase):
    """
    Stack ADT implementation using Linked List (Singly Linked List)
    """ 
    def __init__(self):
        self._head = None
        self._size = 0

    def getTop(self):
        """ Return the top item of stack. None if stack is empty."""
        if not self.isEmpty():
            return self._head.item   
        else:
            return None
    
    def push(self, newItem):
        """ Push (i.e. add) [newItem] on top of stack."""
        newPtr = SinglyNode(newItem)
    
        newPtr.next = self._head
        self._head = newPtr
        self._size += 1
        
        return True

    def pop(self):
        """ Pop (i.e. pop) [newItem] from top of stack."""
        if not self.isEmpty():
            self._head = self._head.next
            self._size -= 1
            return True
        else:
            return False
        
    def size(self):
        """ Return size of the Stack, i.e. number of items"""
        return self._size
    
    def isEmpty(self):
        """ Return True if Stack is empty. False otherwise"""
        return self._size == 0

def main():
    s = StackLinkedList()

    print("Stack size = ",end='')
    print(s.size(), end='')   
    print(" | Stack empty = ",end='')
    print(s.isEmpty())

    s.push(1)
    s.push(2)
    s.push(3)

    print("Pushed 1, 2, 3 | Top = ",end='')
    print(s.getTop())

    print("Pop result = ",end='')
    print(s.pop())

    print("Top = ",end='')
    print(s.getTop())

    print("Stack emtpy = ",end='')
    print(s.isEmpty())

    print("Stack size = ",end='')
    print(s.size()) 

    s.pop()
    s.pop()
    s.pop()
    print("Popped 3 times, Stack emtpy = ",end='')
    print(s.isEmpty())

    print("Top = ",end='')
    print(s.getTop())


if __name__ == "__main__":
    main()