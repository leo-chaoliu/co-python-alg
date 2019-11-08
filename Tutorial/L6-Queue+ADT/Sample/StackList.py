from abc import ABC, abstractmethod     #Abstract Base Class
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

class StackList(StackBase):
    """
    Stack ADT implementation using Python List, i.e. a dynamic array
    """
    def __init__(self):
        self._items = []

    def getTop(self):
        """ Return the top item of stack. None if stack is empty."""
        if not self.isEmpty():
            return self._items[-1]    #negative index = count from the end of list
        else:
            return None

    def push(self, newItem):
        """ Push (i.e. add) [newItem] on top of stack."""
        self._items.append(newItem)

    def pop(self):
        """ Pop (i.e. pop) [newItem] from top of stack."""
        if not self.isEmpty():
            self._items.pop()         #last item is removed
            return True
        else:
            return False

    def size(self):
        """ Return size of the Stack, i.e. number of items"""
        return len(self._items)
    
    def isEmpty(self):
        """ Return True if Stack is empty. False otherwise"""
        return len(self._items) == 0

def main():
    s = StackList()

    print(s.size())   
    print(s.isEmpty())

    s.push(1)
    s.push(2)
    s.push(3)

    print("Pushed 1, 2, 3")
    print(s.getTop())
    top = s.pop()
    print(top)
    print(s.getTop())
    print(s.isEmpty())
    s.pop()
    s.pop()
    s.pop()
    print(s.isEmpty())
    print(s.getTop())


if __name__ == "__main__":
    main()