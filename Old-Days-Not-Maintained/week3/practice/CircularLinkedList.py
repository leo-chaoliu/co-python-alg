from TailedLinkedList import TailedLinkedList, LinkedList, SinglyNode

# we want to repeatly go through 1st to the last 
# Q?: what's the real usage of this feature?

# can base on tialed linked list
# keep track of the tail reference, 
# head = tail.next
class CircularLinkedList(TailedLinkedList):
    def __init__(self):
        super().__init__()
    

    def __str__(self):
        return "CircularLinkedList: head: {0}, size: {1}, tail: {2}".format(self.head, self.size, self.tail)


    def append(self, node):
        super().append(node)

        self.tail.next = self.head

    # check is head again 
    # check by size
    def goThroughRound(self, times):
        if self.tail is None:
            return

        head = self.tail.next

        for counter in range(1, times+1):
            print("Round: {0}".format(counter))
            cur_node = head
            
            # traverse from head to end
            # while cur_node.next is not head:

            # innerCounter = 1
            # while innerCounter <= self.size:
            #     print("{0} -> ".format(cur_node))
            #     cur_node = cur_node.next
            #     innerCounter +=1
            #     pass
            # pass

            while cur_node.next is not head:
                print("{0} -> ".format(cur_node))
                cur_node = cur_node.next
                pass
            
            # print the last cur_node
            print("{0} -> ".format(cur_node))

            pass

def test_cases():
    node1 = SinglyNode("Harry Potter 1")
    node2 = SinglyNode("Harry Potter 2")
    node3 = SinglyNode("Harry Potter 3")
    node4 = SinglyNode("Harry Potter 4")

    cll = CircularLinkedList()
    cll.append(node1)
    cll.append(node2)
    cll.append(node3)

    cll.goThroughRound(5)

    # linkedList.insert(node1, 1)
    # linkedList.insert(node3)
    # print(cll)
    pass


if __name__ == "__main__":
    test_cases()