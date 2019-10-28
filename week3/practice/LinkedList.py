class SinglyNode:
    def __init__(self, item, next_=None):
        self.item = item
        self.next = next_

    def __str__(self):
        return "[SinglyNode: item: {0}, next: {1}]".format(self.item, self.next.item if self.next else self.next)



class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, node):
        cursor = self.head

        if cursor == None:
            self.head = node
        else:
            # move to the last node
            while cursor.next != None:
                cursor = cursor.next

            cursor.next = node

        self.size += 1

    # index start from 1
    def insert(self, node, index=None):
        # default insert to the end
        if index == None or index < 1:
            index = self.size + 1

        # tell from affect head or not
        if index == 1:
            # fill in next attribute for the node
            node.next = self.head

            # update head attibute for the linkedList
            self.head = node
            pass
        else:
            # move the cursor to the index-1 position
            previousNode = self._traverseTo(index)
            node.next = previousNode.next
            previousNode.next = node
            pass

        self.size += 1

        pass

    # herper function to traverse to index-1 postion
    # return index-1 node
    def _traverseTo(self, index):
        if index < 2:
            return None

        if index >= self.size + 1:
            # traverse to the end
            # return the last node
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next

            print("Traversed to last node: {0}".format(last_node))
            return last_node

        # index >= 2
        # know where it start from 
        pre_node = self.head
        counter = 1

        # the last node: head.next = none
        while pre_node.next is not None:
            if counter == index - 1:
                break

            # move on until meet the index 
            pre_node = pre_node.next
            counter += 1

        print("Traversed to {0}th node: {1}".format(counter, pre_node))
        return pre_node

    def __str__(self):
        return "LinkedList: head: {0}, size: {1}".format(self.head, self.size)


def test_cases():
    node1 = SinglyNode("Harry Potter 1")
    node2 = SinglyNode("Harry Potter 2")
    node3 = SinglyNode("Harry Potter 3")
    node4 = SinglyNode("Harry Potter 4")

    linkedList = LinkedList()
    linkedList.append(node2)
    linkedList.append(node4)

    linkedList.insert(node1, 1)
    linkedList.insert(node3)
    print(linkedList)
    pass
# linkedList.traverse(8)


if __name__ == "__main__":
    test_cases()
   
