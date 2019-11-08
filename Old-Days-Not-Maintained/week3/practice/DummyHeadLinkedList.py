from LinkedList import LinkedList, SinglyNode

# Insert/Remove the first node in linked list is a special case
# need to update the head reference

# maintain an extra node at the beginning of the list only to simplify the coding
class DummyHeadLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.head = SinglyNode()
        pass


