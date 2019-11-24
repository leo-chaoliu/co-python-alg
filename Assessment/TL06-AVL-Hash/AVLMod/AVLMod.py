from enum import Enum

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- AVLNode class for the reference based tree node

- AVLMod class for lab exercise, essentially a cut-down + standalone version of the full AVL class

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
    
class AVLNode:
    """
    Reference based AVL Binary Tree Node.
    """
    def __init__(self, key, data, leftPtr = None, rightPtr = None):
        """
        [key] and [data] are expected.

        Has additional attribute height to aid AVL Tree operations.
        """
        self.key = key
        self.data = data
        self.height = 1 #for calculating balance factor
        self.leftT = leftPtr
        self.rightT = rightPtr
    
    def _getHeights(self):
        """
        Helper method to get the heights of left, right subtree.

        Return a tuple (left height, right height).
        """
        Hleft = Hright = 0

        if self.leftT != None:
            Hleft = self.leftT.height
        
        if self.rightT != None:
            Hright = self.rightT.height
        
        return (Hleft, Hright)

    def balanceFactor(self):
        """
        Helper method to return the balance factor at this node.

        Return [left subtree height - right subtree height].
        """
        Hleft, Hright = self._getHeights()
        return Hleft - Hright
    
    def updateHeight(self):
        """
        Helper method to update the height of this node.
        """
        Hleft, Hright = self._getHeights()
        self.height = (Hleft if Hleft > Hright else Hright) + 1

    def toString(self):
        return "[K:%d|Data%s|Depth%d | left at %d |right at %d]"%(self.key, self.data, self.depth, self.leftT, self.rightT)


class AVLMod:
    """
    AVL Tree implemented with reference
    Modified for Lab Exercise - Standalone version
    """
    def __init__(self):
        """
        Returns an empty AVL Tree
        """
        self._root = None
        self._size = 0  
   
    def _rotateRight(self, x):
        """ 
        Helper method to perform right rotation at node x.

        Return the rotated tree.
        """
        l = x.leftT
        if l == None:   #cannot rotate!
            return x
        x.leftT = l.rightT
        l.rightT = x

        x.updateHeight()
        l.updateHeight()
        return l
    
    def _rotateLeft(self, x):
        """ 
        Helper method to perform left rotation at node x.

        Return the rotated tree.
        """
        r = x.rightT
        if r == None:   #cannot rotate!
            return x
        x.rightT = r.leftT
        r.leftT = x

        x.updateHeight()
        r.updateHeight()
        return r



    def _insert(self, T, key, data ):
        """
        Internal recursive method that carries out the insertion algorithm.

        Perform AVL Balancing after insertion.
        """
        if T == None:
            return AVLNode( key, data )
        
        if T.key == key:
            raise KeyError("Duplicate Key!")
        elif T.key < key:
            T.rightT = self._insert( T.rightT, key, data )
        else:
            T.leftT  = self._insert( T.leftT, key, data )
        
        return self._balance(T)

    def insert(self, key, data):
        """
        Insert (key, data) into AVL Tree.

        [key] is used to determine the location of the insertion.
        """
        self._root = self._insert(self._root, key, data)
        self._size += 1

    def _delete( self, T, key ):
        """
        Internal recursive method that carries out the deletion algorithm.

        Perform AVL Balancing after deletion. [Incomplete!]
        """
        if T == None:
            raise KeyError("No such key")
        if T.key < key:
            T.rightT = self._delete( T.rightT, key )
        elif T.key > key :
            T.leftT  = self._delete( T.leftT , key )
        else:
            #logic can be re-organized
            #This version follows the lecture closely
            if T.leftT == None and T.rightT == None:
                return None
            elif T.leftT != None and T.rightT == None:
                return T.leftT
            elif T.leftT == None and T.rightT != None:
                return T.rightT
            else:
                successor = self._findMin( T.rightT )
                T.key = successor.key
                T.data = successor.data
                T.rightT = self._delete( T.rightT, successor.key )
        return T

    def delete(self, key):
        """
        Detele node with [key] from AVL Tree.
        """
        self._root = self._delete( self._root, key)
        self._size -= 1

    
    def _preorder(self, T):
        """
        Internal recursive method to perform Pre-Order Traversal.
        """
        if T == None:
            return []
        return [T.key] + self._preorder(T.leftT) + self._preorder(T.rightT)

    def _inorder(self, T):
        """
        Internal recursive method to perform In-Order Traversal.
        """
        if T == None:
            return []
        return  self._inorder(T.leftT) + [T.key] + self._inorder(T.rightT)

    def _postorder(self, T):
        """
        Internal recursive method to perform Post-Order Traversal.
        """
        if T == None:
            return []
        return  self._postorder(T.leftT) + self._postorder(T.rightT) + [T.key]

    def traversal(self, which):
        """
        Return specified traversal of the AVL as a list.

        [which] should be one of the Enumeration in the Traversal Enum class
        """
        if which == Traversal.PRE:
            return self._preorder(self._root) 
        elif which == Traversal.IN:
            return self._inorder(self._root)
        elif which == Traversal.POST:
            return self._postorder(self._root)
       
    def _spaces(level):
        """
        Internal helper method to generate 4 spaces per level.
        """
        return ' '*(level*4)

    def _pPrintRecursive(self, T, level):
        """
        Internal helper method to do "pretty" printing of AVL Tree.
        """
        if T == None:
            return
        
        self._pPrintRecursive(T.rightT, level+1)

        print(AVLMod._spaces(level), end='')
        print(T.key, end='')
        if T.leftT != None or T.rightT != None:
            print("---")
        else:
            print()
        self._pPrintRecursive(T.leftT, level+1)

    def prettyPrint(self):
        """
        Print the AVL Tree in more visual way. 
        """
        self._pPrintRecursive(self._root, 0)
    
    def _balance(self, T):
        """
        Helper method to perform AVL balancing at node T.

        Return a balanced AVL tree. [Incomplete!]
        """
        if T == None:
            return None
    
        T.updateHeight()
        BF = T.balanceFactor()

        # Check Balance Factor and perform rotations if necessary
        # Incomplete:
        #   Check the Balance factor, call the necessary rotation(s) to correct the issue

        return T

def buildTree( L ):
    """
    Function to build a tree by inserting the number in the list [L].

    Return AVL Tree
    """
    avlT = AVLMod()
    for item in L:
        avlT.insert(item, str(item))
    
    return avlT

def main():

    # Test AVL insertion
    avlT = buildTree([1, 2, 3, 4, 5, 6, 7])
    avlT.prettyPrint()
    # print(avlT.traversal(Traversal.POST))

    # Manual test
    # avlT = AVLMod()
    # avlT.prettyPrint()
    # while True:
    #     key = int(input("Key to insert: "))
    #     avlT.insert(key, str(key))
    #     avlT.prettyPrint()

 
if __name__ == "__main__":
    main()