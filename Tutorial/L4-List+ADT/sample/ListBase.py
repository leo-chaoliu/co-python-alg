from abc import ABC, abstractmethod     #Abstract Base Class

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

class ListBase(ABC):
    """
    Base class for List ADT
    """
    @abstractmethod
    def isEmpty(self):
        """ Return True if List is empty. False otherwise"""
        pass
    
    @abstractmethod
    def getLength(self):
        """ Return size of the list, i.e. number of items"""
        pass

    @abstractmethod
    def insert(self, index, newItem):
        """ Insert [newItem] at [index]
            - [index] ranges from [1... current length+1]

            Return True if item can be inserted. False otherwise.
        """
        pass
    
    @abstractmethod
    def remove(self, index):
        """ Remove item at [index]
            - [index] ranges from [1... current length]

            Return True if item can be deleted. False otherwise.
        """
        pass
    
    @abstractmethod
    def retrieve(self, index):
        """ Return item if [index] is valid. None otherwise."""
        pass
   
    @abstractmethod
    def toString(self):
        """ Simple string representation of all items in list"""
        pass

def main():
    l = ListBase() #this should fails as ComplexBase is an abstract class

if __name__ == "__main__":
    main()