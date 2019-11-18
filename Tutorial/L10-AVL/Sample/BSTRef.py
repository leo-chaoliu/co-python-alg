from abc import ABC, abstractmethod     #Abstract Base Class
from enum import Enum
from BSTBase import *   #import both BSTBase and the Traversal Enum

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- BSTRef ADT implemented using reference
- TreenNode class for the reference based tree node

Student Version
- Certain method is left empty for your own practice

- Basic documentation only

"""

class TreeNode:
    """
    Reference based Binary Tree Node.
    """
    def __init__(self, key, data, leftPtr = None, rightPtr = None):
        """
        [key] and [data] are expected.
        """
        self.key = key
        self.data = data
        self.leftT = leftPtr
        self.rightT = rightPtr
    
    def toString(self):
        return "[K:%d|D%s | left at %d |right at %d]"%(self.key, self.data, self.leftT, self.rightT)


class BSTRef:
    """
    BST ADT implemented with reference
    """
    def __init__(self):
        """
        Returns an empty BST
        """
        self._root = None
        self._size = 0  
        
    def size(self):
        """
        Return size of the BST, i.e. number of datas in BST.
        """
        return len(self._size)

    def _findMin( self, T ):
        if T == None:
            return None
        if T.leftT == None:
            return T
        return self._findMin( T.leftT )

    def findMinElement( self ):
        """
        Return the (key, data) for the node with smallest key.
        """
        target = self._findMin(self._root)
        return (target.key, target.data)
    
    def _insert(self, T, key, data ):
        """
        Internal recursive method that carries out the insertion algorithm.
        """
        if T == None:
            return TreeNode( key, data )
        
        if T.key == key:
            raise KeyError("Duplicate Key!")
        elif T.key < key:
            T.rightT = self._insert( T.rightT, key, data )
        else:
            T.leftT  = self._insert( T.leftT, key, data )
        
        return T

    def insert(self, key, data):
        """
        Insert (key, data) into BST.

        [key] is used to determine the location of the insertion.
        """
        self._root = self._insert(self._root, key, data)
        self._size += 1

    def _delete( self, T, key ):
        """
        Internal recursive method that carries out the deletion algorithm.
        """
        return T    #incomplete implementation

    def delete(self, key):
        """
        Detele node with [key] from BST.
        """
        self._root = self._delete( self._root, key)
        self._size -= 1
    
    def _preorder(self, T):
        """
        Internal recursive method to perform Pre-Order Traversal.
        """
        if T == None:
            return "-"
        return "{ %s "%(T.key) + self._preorder(T.leftT) \
            + " " + self._preorder(T.rightT) + " } "

    def _inorder(self, T):
        """
        Internal recursive method to perform In-Order Traversal.
        """
        return "" #Incomplete Implementation

    def _postorder(self, T):
        """
        Internal recursive method to perform Post-Order Traversal.
        """
        return "" #Incomplete Implementation

    def traversal(self, which):
        """
        Print the BST by the specified traversal.

        [which] should be one of the Enumeration in the Traversal Enum class
        """
        if which == Traversal.PRE:
            return "[%d nodes]="%self._size+self._preorder(self._root) 
        elif which == Traversal.IN:
            return "[%d nodes]="%self._size+self._inorder(self._root)
        elif which == Traversal.POST:
            return "[%d nodes]="%self._size+self._postorder(self._root)
    
def main():
    bt = BSTRef()

    bt.insert(5,"Five")
    bt.insert(3,"Three")
    bt.insert(1,"One")
    bt.insert(8,"Eight")
    bt.insert(4,"Four")
    bt.insert(7,"Seven")
    bt.insert(9,"Nine")
    bt.insert(2,"Two")
    bt.insert(6,"Six")

    print(bt.traversal(Traversal.PRE))
    print(bt.traversal(Traversal.IN))
    print(bt.traversal(Traversal.POST))
    print("Min = "+str(bt.findMinElement()))

    bt.delete(4)
    print(bt.traversal(Traversal.PRE))

    bt.delete(3)
    print(bt.traversal(Traversal.PRE))

    bt.delete(1)
    print(bt.traversal(Traversal.PRE))

    bt.delete(8)
    print(bt.traversal(Traversal.PRE))

if __name__ == "__main__":
    main()