from LinkedList import LinkedList, SinglyNode

# keep an additional reference to the last node
# reduce access last node TC O(n) to O(1) by using additional space
# append will benefit for this

# suitable base data structure for stack or queue
class TailedLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def __str__(self):
        return "TailedLinkedList: head: {0}, size: {1}, tail: {2}".format(self.head, self.size, self.tail)

    # benefit functions
    # override    
    def append(self, node):
        # super().append(node)
        # self.tail = node
        cursor = self.head

        if cursor == None:
            self.head = node
            self.tail = node
        else:
            # point current tail to the node
            self.tail.next = node
            
            # update tail pointing
            self.tail = node

        self.size += 1

    
def test_cases():
    node1 = SinglyNode("Harry Potter 1")
    node2 = SinglyNode("Harry Potter 2")
    node3 = SinglyNode("Harry Potter 3")
    node4 = SinglyNode("Harry Potter 4")

    tll = TailedLinkedList()
    tll.append(node2)
    tll.append(node4)

    # linkedList.insert(node1, 1)
    # linkedList.insert(node3)
    print(tll)
    pass

if __name__ == "__main__":
    test_cases()
    
