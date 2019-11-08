class SinglyNode():
    def __init__(self, item, link = None):
        self.item = item
        self.next = link

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    

def printLL(node):
    # iterative thinking
    # cur = node

    # for i in range(linkedList.size):
    #     print(cur.item)
    #     cur = cur.next
    # pass

    # base case
    if node == None:
        return

    # reduced problem
    # winding
    print(node.item)

    printLL(node.next)
    
    # unwinding
    print(node.item)

    # general solution

def countIf(head, target):
    if head == None:
        return 0
    
    head_value = head.item 
    head = head.next

    ans = countIf(head,target)

    if head_value == target:
        ans += 1

    return ans
    
   

    pass

def main():
    node1 = SinglyNode(0)
    node2 = SinglyNode(0)
    node3 = SinglyNode(0)

    ll = LinkedList()
    ll.head = node1
    ll.head.next = node2
    ll.head.next.next = node3
    ll.size = 3

    # printLL(ll.head)
    print(countIf(ll.head, 2))

    pass

main()

