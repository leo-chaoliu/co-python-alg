from abc import ABC, abstractmethod  # Abstract Base Class
from enum import Enum
from BSTBase import *  # import both BSTBase and the Traversal Enum
from QueueLinkedList import *

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

    def __init__(self, key, data, leftPtr=None, rightPtr=None):
        """
        [key] and [data] are expected.
        """
        self.key = key
        self.data = data
        self.leftT: TreeNode = leftPtr
        self.rightT: TreeNode = rightPtr

    def toString(self):
        return "[K:%d|D%s | left at %d |right at %d]" % (self.key, self.data, self.leftT, self.rightT)


class BSTRef:
    """
    BST ADT implemented with reference
    """

    def __init__(self):
        """
        Returns an empty BST
        """
        # only for type hint, can be used by third party tools such as type checkers, IDEs, linters, etc.
        # syntax -> variableName: variableType
        self._root: TreeNode = None
        self._size = 0

    def size(self):
        """
        Return size of the BST, i.e. number of datas in BST.
        """
        return self._size

    def _findMin(self, T):
        # goes down until reach the left bottom one
        # which is the min in BST

        if T == None:
            return None
        if T.leftT == None:
            return T

        return self._findMin(T.leftT)

    def findMinElement(self):
        """
        Return the (key, data) for the node with smallest key.
        """
        # a wrapper function, to show the common interface

        target = self._findMin(self._root)
        return (target.key, target.data)

    def _insert(self, T, key, data):
        """
        Internal recursive method that carries out the insertion algorithm.
        """
        if T == None:
            return TreeNode(key, data)

        if T.key == key:
            raise KeyError("Duplicate Key!")
        elif T.key < key:
            # rember to assign the value back
            T.rightT = self._insert(T.rightT, key, data)
        else:
            T.leftT = self._insert(T.leftT, key, data)

        return T

    def insert(self, key, data):
        """
        Insert (key, data) into BST.

        [key] is used to determine the location of the insertion.
        """
        self._root = self._insert(self._root, key, data)
        self._size += 1

    def _delete(self, T, key):
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
            T.rightT = self._delete(T.rightT, key)

        elif T.key > key:
            T.leftT = self._delete(T.leftT, key)

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
                T.rightT = self._delete(T.rightT, s.key)

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

        r1 = "{ %s " % (T.key)
        r2 = self._preorder(T.leftT)
        r3 = self._preorder(T.rightT) + " } "

        result = "{0}{1} {2}".format(r1, r2, r3)

        return result

    def _inorder(self, T):
        # bracket priting
        # """
        # Internal recursive method to perform In-Order Traversal.
        # """
        # if T == None:
        #     return "-"
        #
        # r1 = "{ " + self._inorder(T.leftT)
        # r2 = "{}".format(T.key)
        # r3 = self._inorder(T.rightT) + " } "
        #
        # result = "{} {} {}".format(r1, r2, r3)
        # return result

        # return the [] directly
        if T == None:
            return []

        # in python, [1] + [1,2,3] = [1,1,2,3]
        # return a sorted list
        return  self._inorder(T.leftT) + [T.key] + self._inorder(T.rightT)

    def _postorder(self, T):
        """
        Internal recursive method to perform Post-Order Traversal.
        """
        if T == None:
            return "-"

        r1 = "{ " + self._postorder(T.leftT)
        r2 = self._postorder(T.rightT)
        r3 = "{}".format(T.key) + " } "

        result = "{} {} {}".format(r1, r2, r3)
        return result

    def _levelOrder(self):
        # queue is to store the tree node by level
        queue = QueueLinkedList()
        # result list is to store the node.key only
        resultList = []

        # enqueue the root node ref
        queue.enqueue(self._root)

        # repeat dequeue and enqueue
        # until the queue is empty
        while not queue.isEmpty():
            # get the node in the front
            node: TreeNode = queue.getFront()
            resultList.append(node.key)

            # enqueue the children of the node when dequeue happens
            queue.dequeue()

            if node.leftT != None:
                queue.enqueue(node.leftT)

            if node.rightT != None:
                queue.enqueue(node.rightT)

        return resultList

    def traversal(self, which):
        """
        Print the BST by the specified traversal.

        [which] should be one of the Enumeration in the Traversal Enum class
        """
        print('\nTraveling, method: {}'.format(which))

        if which == Traversal.PRE:
            return "[%d nodes]=" % self._size + self._preorder(self._root)
        elif which == Traversal.IN:
            # return "[%d nodes]=" % self._size + self._inorder(self._root)
            return self._inorder(self._root)
        elif which == Traversal.POST:
            return "[%d nodes]=" % self._size + self._postorder(self._root)
        elif which == Traversal.LEVEL:
            return self._levelOrder()

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

        self._prettyPrint(T.rightT, height + 1)

        dash = ""
        if T.leftT != None or T.rightT != None:
            dash = "---"

        spacing = height * "    "
        print("{0}{1}{2}".format(spacing, T.key, dash))

        self._prettyPrint(T.leftT, height + 1)

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

    def _pathV1(self, T, height):
        pass

    def pathV1(self):
        '''
        Sample output 4
        '''

        return

    # in order traversal
    def _pathV2(self, T, height, list):
        if T == None:
            return height

        self._pathV2(T.leftT, height + 1, list)

        # printing out all nodes key with its height by inOrder traversal
        # print("LeftUnWind: key: {0}, height: {1}".format(T.key, height))

        # path from left to right
        # an Observation for a path:
        # a leaf node or a node with only rightT
        if (T.leftT == None and T.rightT == None) \
                or (T.leftT == None and T.rightT != None):
            # print("key: {0}, height: {1}".format(T.key, height))
            list.append(height)

        self._pathV2(T.rightT, height + 1, list)

        # when left and right all been traversed for a sub tree
        # print("RightUnWind: key: {0}, height: {1}".format(T.key, height))

        # print(list)

    def pathV2(self):
        '''
        Sample output [3,4,4,2]
        '''
        list = []

        if self._root == None:
            return list

        self._pathV2(self._root, 1, list)

        print('\npathV2: {}'.format(list))
        return list

    # in order traversal
    def _pathV3(self, T, height, list):
        if T == None:
            return height

        self._pathV3(T.leftT, height + 1, list)

        # printing out all nodes key with its height by inOrder traversal
        # print("LeftUnWind: key: {0}, height: {1}".format(T.key, height))

        # path from left to right
        # an Observation for a path:
        # a leaf node or a node with only rightT
        if (T.leftT == None and T.rightT == None) \
                or (T.leftT == None and T.rightT != None):
            # print("key: {0}, height: {1}".format(T.key, height))
            list.append([height, [T.key]])

        self._pathV3(T.rightT, height + 1, list)

        # when left and right all been traversed for a sub tree
        # print("RightUnWind: key: {0}, height: {1}".format(T.key, height))

        # the assessor node for it's path should
        # 1. it's height lower than the max height of the path which is item[0] minus the length of it's been collected
        # 2. not be a leaf
        for item in list:
            if height < item[0] - len(item[1]) + 1 and \
                    not (T.leftT == None and T.rightT == None):
                item[1].append(T.key)

        # print(list)

    def pathV3(self):
        '''
        Sample output with the binary tree shown: 
        [ (3, '4‐2‐1'), (4, '8‐5‐2‐1'), (4, '9‐5‐2‐1'), (2, '7‐1')] 
        '''
        list = []

        if self._root == None:
            return list

        # passing hList to collect value in each phase
        # hList is an mutable data structure, will track by reference
        # after recursion, hList will be filled in
        # default height = 1 if root is not None
        self._pathV3(self._root, 1, list)

        # just to format the list as paper's answer
        resultList = []
        for item in list:
            tuple_ = (item[0], "-".join(map(str, item[1])))
            resultList.append(tuple_)
            pass

        print('\npathV3: {}'.format(resultList))
        return resultList

    # construct a tree
    # wen can build an unique Binary Tree from preOrder/postOrder and inOrder
    def constructBinaryTree(self, preOrder, inOrder):
        pass

    # we could build an unique BST only from preOrder/postOrder/inOrder/levelOrder
    def _buildBSTfromPreorder(self, L):
        """
        [L] is a list of number organized as a pre-order traversal of a BST.

        Rebuild and return the BST from [L].
        """
        # Your Part (a) solution here

        if L == []:
            return None

        root = TreeNode(L[0], L[0])

        n = len(L)

        # find the index of the boundary of left subtree and right subtree
        idx = 0
        for i in range(1, n):
            if L[i] < L[0]:
                idx += 1

        root.leftT = self._buildBSTfromPreorder(L[1:idx + 1])
        root.rightT = self._buildBSTfromPreorder(L[idx + 1:n])

        return root

    def buildBSTfromPreorder(self, L):
        """
        Just a wrapper to call the actual recursive implementation.

        Note: Calling this method destroy current content of BST.
        """
        self._root = self._buildBSTfromPreorder(L)
        self._size = len(L)

    def _buildBSTfromRandomlist(self, L):
        n = len(L)

        for i in range(0, n):
            self.insert(L[i], L[i])

    def _buildBSTfromSortedList(self, L):
        """
        Internal helper method to build a BST from sorted list
        """
        # Your Part (b) solution here

        if L == []:
            return None

        n = len(L)

        rootIdx = n // 2

        root = TreeNode(L[rootIdx], L[rootIdx])

        root.leftT = self._buildBSTfromSortedList(L[0:rootIdx])
        root.rightT = self._buildBSTfromSortedList(L[rootIdx + 1:])

        return root  # modify accordingly

    def buildBalancedBST(self, L):
        """
        [L] is a list of numbers in random order.

        Build and return a balanced BST from [L].
        """

        # Your Part (b) solution here.

        self._buildBSTfromRandomlist(L)
        sortedList = self.traversal(Traversal.IN)
        self._root = self._buildBSTfromSortedList(sortedList)

def main():
    bt = BSTRef()

    bt.insert(5, "Five")
    bt.insert(3, "Three")
    bt.insert(1, "One")
    bt.insert(8, "Eight")
    bt.insert(4, "Four")
    bt.insert(7, "Seven")
    bt.insert(9, "Nine")
    bt.insert(2, "Two")
    bt.insert(6, "Six")

    print(bt.traversal(Traversal.PRE))
    print(bt.traversal(Traversal.IN))
    print(bt.traversal(Traversal.POST))
    print(bt.traversal(Traversal.LEVEL))

    bt.prettyPrint()

    print("Min = "+str(bt.findMinElement()))


    bt.pathSum()

    bt.prettyPrint()

    bt.delete(3)
    bt.delete(8)

    bt.prettyPrint()

    flippedTree = bt.flipTree()

    print('\nFlipped Tree')
    bt._prettyPrint(flippedTree, 0)

    print('\nbuildBSTfromPreorder')
    bt2 = BSTRef()
    bt2.buildBSTfromPreorder([5, 3, 1, 2, 4, 8, 6, 7, 9])
    bt2.prettyPrint()

    print('\nbuildBalancedBST')
    bt3 = BSTRef()
    bt3.buildBalancedBST([2, 4, 7, 8, 1, 5, 6, 3, 9])
    bt3.prettyPrint()

    print('\n')
    bt.prettyPrint()
    bt.pathV2()
    bt.pathV3()

if __name__ == "__main__":
    main()
