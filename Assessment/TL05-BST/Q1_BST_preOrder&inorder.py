import BSTMod

def construct_BinaryTree(preOrder,inOrder):
    # preOrder and inOrder are both Python list
    if preOrder==[]:
        return None

    root = BSTMod.TreeNode(preOrder[0],preOrder[0])

    idx = inOrder.index([preOrder[0]])

    root.leftT = self.construct_BinaryTree(preOrder[1:idx+1],inOrder[0:idx])
    root.rightT = self.construct_BinaryTree(preOrder[idx+1:],inOrder[idx+1:])

    return root


def main():

    bt = construct_BinaryTree(L1, L2)
    L1 = [8,7,5,28,4,9,18,17,16]
    L2 = [5,7,4,28,9,8,18,16,17]
    
    result = BSTMod.Traversal(Traversal.PRE)

    print(result)

if __name__ == "__main__":
    main()
