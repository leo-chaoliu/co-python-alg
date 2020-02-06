from enum import Enum

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- TreenNode class for the reference based tree node

- BSTMod class for lab exercise, essentially a cut-down version of the full BST class

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

class BSTMod:
    """
    Simplified BST ADT implemented with reference
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

    def _insert(self, T, key, data ):
        """
        Internal recursive method that carries out the insertion algorithm.
        """
        if T == None:
            return TreeNode( key, data )
        
        if T.key == key:
            raise KeyError("Duplicate Key [%s]!"%(key))
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

    #Note deletion is not supported in this simplified implementation
    
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
        Return specified traversal of the BST as a list.

        [which] should be one of the Enumeration in the Traversal Enum class
        """
        if which == Traversal.PRE:
            return self._preorder(self._root) 
        elif which == Traversal.IN:
            return self._inorder(self._root)
        elif which == Traversal.POST:
            return self._postorder(self._root)

    def _buildBSTfromPreorder(self, L ):
        """ 
        [L] is a list of number organized as a pre-order traversal of a BST. 
        
        Rebuild and return the BST from [L]. 
        """
        #Your Part (a) solution here
        
        if L == []:
            return None

        root = TreeNode(L[0],L[0])

        n = len(L)

        # find the index of the boundary of left subtree and right subtree
        idx = 0
        for i in range(1,n):
            if L[i] < L[0]:
                idx += 1

        root.leftT = self._buildBSTfromPreorder(L[1:idx+1])
        root.rightT = self._buildBSTfromPreorder(L[idx+1:n])

        return root   #modify accordingly
    
    def buildBSTfromPreorder(self, L ):
        """ 
        Just a wrapper to call the actual recursive implementation. 
        
        Note: Calling this method destroy current content of BST.
        """
        self._root = self._buildBSTfromPreorder(L)
        self._size = len(L)

    def _buildBSTfromRandomlist(self,L):
        n = len(L)  

        for i in range(0,n):
            self.insert(L[i],L[i])
    
    def _buildBSTfromSortedList(self, L):
        """
        Internal helper method to build a BST from sorted list
        """
        #Your Part (b) solution here

        if L == []:
            return None
        
        n = len(L)

        rootIdx = n//2

        root = TreeNode(L[rootIdx],L[rootIdx]) 

        root.leftT = self._buildBSTfromSortedList(L[0:rootIdx])
        root.rightT = self._buildBSTfromSortedList(L[rootIdx+1:])

        return root   #modify accordingly


    def buildBalancedBST( self,  L ):
        """ 
        [L] is a list of numbers in random order. 
        
        Build and return a balanced BST from [L]. 
        """

        #Your Part (b) solution here. 
        
        self._buildBSTfromRandomlist(L)
        sortedList = self.traversal(Traversal.IN)
        self._root = self._buildBSTfromSortedList(sortedList)
        
        #Need to figure out how to use the recursive _buildBSTFromSortedList() above

    def _sumTree(self, T, sum):

        if T==None:
            return sum
            
        if T.leftT == None and T.rightT == None:
           sum = sum + T.data
           return sum

        # left sum
        sum = sum + self._sumTree(T.leftT, sum)

        # right sum
        sum = sum + self._sumTree(T.rightT, sum)

        return sum
        pass

    def sumTree(self):
        return self._sumTree(self._root, 0)

def main():

    bt = BSTMod()

    # Part A test below
    # bt.buildBSTfromPreorder([5, 3, 1, 2, 4, 8, 6, 7, 9])

    # Part B test below
    bt.buildBalancedBST([1,2,3])
    # bt.buildBalancedBST([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(bt.traversal(Traversal.IN))

    sum = bt.sumTree()
    print(sum)
    

if __name__ == "__main__":
    main()
