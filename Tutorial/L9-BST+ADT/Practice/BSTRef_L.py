from abc import ABC, abstractmethod     #Abstract Base Class
from enum import Enum
from BSTBase import *   #import both BSTBase and the Traversal Enum


"""
For IT5003 - by SYJ & Leo & Molly
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
        return self._size

    def _findMin( self, T ):
        # goes down until reach the left bottom one
        # which is the min in BST

        if T == None:
            return None
        if T.leftT == None:
            return T
        
        return self._findMin( T.leftT )

    def findMinElement( self ):
        """
        Return the (key, data) for the node with smallest key.
        """
        # a wrapper function, to show the common interface

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
            # rember to assign the value back
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
        # protection if 
        if T == None:
            raise KeyError("Cannot Find Key Error")
        
        # Find the deletion location
        # Using Binary search
        # Remember to return T back

        if T.key < key:
            T.rightT = self._delete(T.rightT,key)

        elif T.key > key:
            T.leftT = self._delete(T.leftT,key)
         
        # Arrived the deletion location
        else:    
            
            # case 1: no child 
            if T.leftT == None and T.rightT == None:
                return None
                
            # case 2: one child
            elif T.leftT == None and T.rightT != None:
                return T.rightT
           
            elif T.rightT == None and T.leftT != None:
                return T.leftT
          
            # case 3: two children
            # re-construct a new root 
            # using the min of the rightT
            # or using the max of the leftT
            else:
                s = self._findMin(T.rightT)
                T.key = s.key
                T.data = s.data

                # delete the duplication
                # since is the min value, it should has only rightT or no leaf
                # remember to assign it back !
                T.rightT = self._delete(T.rightT,s.key)

        # always return the current T back 
        return T

    def delete(self, key):
        """
        Detele node with [key] from BST.
        """
        self._delete(self._root, key)
        self._size -= 1
        print('Deleted {}\n'.format(key))

    def _preorder(self, T):
        """
        Internal recursive method to perform Pre-Order Traversal.
        """
        if T == None:
            return "-"
        
        r1 = "{ %s "%(T.key)
        r2 = self._preorder(T.leftT)
        r3 = self._preorder(T.rightT) + " } "

        result = "{0}{1} {2}".format(r1, r2, r3)

        return result

    def _inorder(self, T):
        """
        Internal recursive method to perform In-Order Traversal.
        """
        if T == None:
            return "-"

        r1 = "{ " + self._inorder(T.leftT)
        r2 = "{}".format(T.key)
        r3 = self._inorder(T.rightT) + " } "
        
        result = "{} {} {}".format(r1,r2,r3)
        return result

    def _postorder(self, T):
        """
        Internal recursive method to perform Post-Order Traversal.
        """
        if T == None:
            return "-"

        r1 = "{ " + self._postorder(T.leftT)
        r2 = self._postorder(T.rightT)
        r3 = "{}".format(T.key) + " } "
       
        result = "{} {} {}".format(r1,r2,r3)
        return result

    def levelOrder(self):
        pass

    def traversal(self, which):
        """
        Print the BST by the specified traversal.

        [which] should be one of the Enumeration in the Traversal Enum class
        """
        print('\nTraveling, method: {}'.format(which))

        if which == Traversal.PRE:
            return "[%d nodes]="%self._size+self._preorder(self._root) 
        elif which == Traversal.IN:
            return "[%d nodes]="%self._size+self._inorder(self._root)
        elif which == Traversal.POST:
            return "[%d nodes]="%self._size+self._postorder(self._root)
        elif which == Traversal.LEVEL:
            return self.levelOrder()

    # interface function 
    def prettyPrint(self):
        self._prettyPrint(self._root, 0)
        pass

    def _prettyPrint(self, T, height):
        """
        Internal recursive method to perform prettyPrint Traversal.
        """
        if T == None:
            return height
       
        self._prettyPrint(T.rightT, height+1)

        dash = ""
        if T.leftT != None or T.rightT != None:
            dash = "---"

        spacing = height * "    "
        print("{0}{1}{2}".format(spacing,T.key,dash))

        self._prettyPrint(T.leftT, height+1)
    
    def pathSum(self):
        pathSum = self._pathSum(self._root, 0)

        print('pathSum: {}'.format(pathSum))
        pass

    def _pathSum(self, T, sum_):

        # In case left is empty
        if T == None:
            return sum_

        # Start to unwind when T is not a leaf
        if T.leftT == None and T.rightT == None:
            return sum_ + T.key
        
        # Accumulate the sum when it winding down 
        # Assign the right nodes value to sum_
        sum_ = self._pathSum(T.leftT, sum_ + T.key)

        # Only add its right Node value
        # Start to excute in each time at each unwind point
        sum_ = self._pathSum(T.rightT, sum_)

        return sum_
        pass

    def _flipTree(self, T):
        if T == None:
            return None
        
        root = TreeNode(T.key, T.data)
        root.leftT = self._flipTree(T.rightT)
        root.rightT = self._flipTree(T.leftT)

        # in recursion, is the point to unwinding 
        return root
        pass
        
    def flipTree(self):
        '''
        return the mirror image of T
        '''
        return self._flipTree(self._root)
        pass

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
    print(bt.traversal(Traversal.LEVEL))

    print("Min = "+str(bt.findMinElement()))
    
    bt.prettyPrint()

    bt.pathSum()

    bt.prettyPrint()

    bt.delete(3)
    bt.delete(8)

    bt.prettyPrint()

    flippedTree = bt.flipTree()

    print('\nFlipped Tree')
    bt._prettyPrint(flippedTree, 0)

    




if __name__ == "__main__":
    main()