from abc import ABC, abstractmethod     #Abstract Base Class
from enum import Enum

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- Implemented BST ADT:
    - Specification:  BSTBase Base Class
    - Implementation: 
        A. Reference base - (BSTRef Class)

- Basic documentation only

"""

class Traversal(Enum):
    """
    Enumeration for more readable code.

    Represent the four possible Binary Tree Traversals.
    """
    IN = 1
    PRE = 2
    POST = 3
    LEVEL = 4

class BSTBase(ABC):
    """
    Base class for BST ADT
    """
    @abstractmethod
    def size(self):
        """
        Return size of the BST, i.e. number of items in BST.
        """
        pass

    @abstractmethod
    def findMinElement( self ):
        """
        Return the (key, data) for the node with smallest key.
        """
        pass
    
    def insert(self, key, data):
        """
        Insert (key, data) into BST.

        [key] is used to determine the location of the insertion.
        """
        pass


    def delete(self, key):
        """
        Detele node with [key] from BST.
        """
        pass
    
    def traversal(self, which):
        """
        Print the BST by the specified traversal.

        [which] should be one of the Enumeration in the Traversal Enum class
        """
        pass
    
def main():
    bt = BSTBase()  #should fail as it is a abstract class

if __name__ == "__main__":
    main()