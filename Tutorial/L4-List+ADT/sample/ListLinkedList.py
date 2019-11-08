from abc import ABC, abstractmethod     #Abstract Base Class

#Our own classes 
from ListBase import ListBase           
from SinglyNode import SinglyNode

"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- Implemented List (with index, not ordered) ADT:
    - Specification: ListBase Base Class
    - Implementations: 
        A. Array (ListArray Class)
        B. LinkedList (ListLinkedList Class)

- Basic documentation only

"""

class ListLinkedList(ListBase):
    """
    List ADT implementation using linked list (disjoint memory locations)
    """
    def __init__(self):
        self._head = None
        self._size = 0

    def isEmpty(self):
        """ Return True if List is empty. False otherwise"""
        return self._size == 0   
    
    def getLength(self):
        """" Return size of the list, i.e. number of items"""
        return self._size

    def _traverse(self, index):
        """ Internal helper method. Return a reference to it. "index"-th item."""
        if index < 1 or index > self._size:
            return None
        
        ptr = self._head
        for i in range(1, index):
            ptr = ptr.next
        return ptr
        
    def insert(self, index, item):
        """ Insert [newItem] at [index]
            - [index] ranges from [1... current length+1]

            Return True if item can be inserted. False otherwise.
        """
        if index < 1 or index > self._size+1:
            return False

        newPtr = SinglyNode(item) #Create a new node
        if index == 1:
            newPtr.next = self._head
            self._head = newPtr
        else:
            prev = self._traverse(index-1)
            newPtr.next = prev.next
            prev.next = newPtr  
        self._size += 1
        return True

    def remove(self, index):
        """ Remove item at [index]
            - [index] ranges from [1... current length]

            Return True if item can be deleted. False otherwise.
        """
        if index < 1 or index > self._size:
            return False
        
        if index == 1:
            cur = self._head
            self._head = self._head.next
        else:
            prev = self._traverse(index-1)
            cur = prev.next
            prev.next = cur.next
        #In language with no auto garbage collection
        # need to dispose of the memory used by node
        # referred by cur
        self._size -= 1
        return True

    def retrieve(self, index):
        """ Return item if [index] is valid. None otherwise."""
        if index < 1 or index > self._size:
            return None
        ptr = self._traverse(index)
        return ptr.item

    def toString(self):
        """ Simple string representation of all items in list. """
        ptr = self._head
        str = "Size[{:d}] | ".format(self._size)
        while ptr != None:
            str += ptr.toString()
            ptr = ptr.next
        return str

def main():
    l = ListLinkedList()

    print(l.toString())

    l.insert(1, 100)
    l.insert(2, 200)
    l.insert(1, 50)
    l.insert(4, 300)
    l.insert(2, 75)
    l.insert(5, 250)
    print(l.toString())

    l.remove(1)
    print(l.toString())

    l.remove(l.getLength())
    print(l.toString())

    l.remove(3)
    print(l.toString())

    while l.getLength() > 0:
        l.remove(1)
    print(l.toString())


if __name__ == "__main__":
    main()