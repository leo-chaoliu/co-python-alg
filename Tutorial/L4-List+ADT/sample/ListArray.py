from abc import ABC, abstractmethod     #Abstract Base Class
import ctypes
from ListBase import ListBase

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

class ListArray(ListBase):
    """
    List ADT implementation using "array" (fixed size consecutive memory locations)
    """
    def __init__(self):
        self._size = 0
        self._enlarge(1)

    def _enlarge(self, newCapacity):
        """ Internal helper method to enlarge the internal item storage"""
        newStorage = (newCapacity * ctypes.py_object)()
        for i in range (self._size):
            newStorage[i] = self._storage[i]
        self._storage = newStorage
        self._capacity = newCapacity

    def isEmpty(self):
        """ Return True if List is empty. False otherwise"""
        return self._size == 0
    
    def getLength(self):
        """ Return size of the list, i.e. number of items"""
        return self._size

    def insert(self, index, newItem):
        """ Insert [newItem] at [index]
            - [index] ranges from [1... current length+1]

            Return True if item can be inserted. False otherwise.
        """
        if index < 1 or index > self._size+1:
            return False
        
        if self._size == self._capacity:
            self._enlarge(self._capacity*2)     # grow 2x in capacity

        internal = index - 1  #internally, index goes from [0..size-1]
        for pos in range(self._size-1, internal-1,-1 ):
            self._storage[pos+1] = self._storage[pos]

        self._storage[internal] = newItem
        self._size += 1
        return True


    def remove(self, index):
        """ Remove item at [index]
            - [index] ranges from [1... current length]

            Return True if item can be deleted. False otherwise.
        """
        if index < 1 or index > self._size:
            return False
        
        internal = index - 1  #internally, index goes from [0..size-1]

        for pos in range(internal, self._size-1):
            self._storage[pos] = self._storage[pos+1]
        self._size -= 1  
        return True

    
    def retrieve(self, index):
        """ Return item if [index] is valid. None otherwise."""
        if index < 1 or index > self._size:
            return None
       
        internal = index - 1  #internally, index goes from [0..size-1]
        return self._storage[internal]
   
    def toString(self):
        """ Simple string representation of all items in list. 
            Shows both the current size and the internal capacity for debugging purpose.
        """
        str = "Size[{:d}/{:d}] | ".format(self._size, self._capacity)
        for i in range(self._size):
            str += "[{}]".format(self._storage[i])
        return str

def main():
    l = ListArray()

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