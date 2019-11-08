from LinkedList import SinglyNode

# derived feature to goto next in sequence
# able to go prev node in sequence
class DoublyNode(SinglyNode):
    def __init__(self, item, prev, next_):
        super().__init__(next_)
        self.prev = prev

    def __str__(self):
        return "[DoublyNode: item: {0}, prev: {1}, next: {2}]".format(
            self.item, 
            self.prev.item if self.prev else self.prev,
            self.next.item if self.next else self.next)

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

        pass

    def insert(self,index):
        pass

    def traverseTo(self, index):
        super()._
        pass
    
