"""
For IT5003 - by SYJ 

Version 1.0 (2019 November)
- TreenNode class for the reference based tree node

- BTSimple Class for PE, a simplified Binary Tree class

- Basic documentation only

"""

import math

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
        self.level = 1
        self.leftT = leftPtr
        self.rightT = rightPtr

    def _getLevel(self):
        L_left = L_right = 0

        if self.leftPrt!=None:
            L_left = self.leftPtr.level

        if self.rightPrt!=None:
            L_right = self.rightT.level

        return (L_left, L_right)
    def updateLevel(self):
        L_left, L_right = self._getLevel()
        self.level = (L_left if L_left >L-right else L-right) + 1
    
    
    def toString(self):
        return "[K:%d|D%s | left at %d |right at %d]"%(self.key, self.data, self.leftT, self.rightT)

class BTSimple:
    """
    Simplified BT implemented with reference
    """
    def __init__(self, vList):
        """
        Construct a BT base on the [vList]
        vList has the format [root, [Left Tree], [Right Tree]], 
            where left and right tree has the same format
        """
        self._root = self._buildBT(vList)
        self._size = len(vList)
        
    def _buildBT(self, vList):
        if vList == []:
            return None
        
        t = TreeNode(vList[0], str(vList[0]))
    
        if len(vList) > 1:
            t.leftT = self._buildBT(vList[1])
            t.rightT = self._buildBT(vList[2])

        return t

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

        print(BTSimple._spaces(level), end='')
        print(T.key, end='')
        if T.leftT != None or T.rightT != None:
            print("---")
        else:
            print()
        self._pPrintRecursive(T.leftT, level+1)

    def prettyPrint(self):
        """
        Print the Binary Tree in more visual way. 
        """
        self._pPrintRecursive(self._root, 0)
    
    """
    VERSION 1
    """

    #You can add additional parameter to the method
    def _pathV1( self, a):

        if self.leftT == None and self.rightT == None:
            return a += 1
        
        a = 1 + self._pathV1(self.leftT,a)
        a = 1 + self._pathV1(self.rightT,a)

            
        pass    #change to your code
    
    def pathV1(self):
        #You can add arguments to the call _pathV1()
        return self._pathV1( )
    
    """
    VERSION 2
    """
    #You can add additional parameter to the method
    def _pathV2( self ):
        pass    #change to your code
    
    def pathV2(self):
        #You can add arguments to the call _pathV2()
        return self._pathV2( )

    """
    VERSION 3
    """
    #You can add additional parameter to the method
    def _pathV3( self ):
        pass    #change to your code
    
    def pathV3(self):
        #You can add arguments to the call _pathV3()
        return self._pathV3( )


def main():

    #BTSimple construct a tree from a list with the format
    # [root, [Left Tree], [Right Tree]], where left and right tree has the same format
    bt = BTSimple([1,[2, [4], [5, [8], [9]]], [7]]) #the same tree as in the question
    bt.prettyPrint()

    #You only need to implement ONE of the following
    print( bt.pathV1() )
    print( bt.pathV2() )
    print( bt.pathV3() )



if __name__ == "__main__":
    main()
