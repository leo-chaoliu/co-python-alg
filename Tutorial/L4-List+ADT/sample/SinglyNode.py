
"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- Linked list node with a single next reference / pointer
- Used for many ADTs
- Basic documentation only

"""

class SinglyNode:
    def __init__(self, item, link = None):
        self.item = item
        self.next = link
    
    def toString(self):
        """Print the Node's item and a "->" if the next reference is valid."""
        return "[{}]".format(self.item) + ("->" if self.next != None else "")

def main():
    head = SinglyNode(123)
    print(head.toString())

    head = SinglyNode(456, head)
    print(head.toString())

    print(head.item)

if __name__ == "__main__":
    main()