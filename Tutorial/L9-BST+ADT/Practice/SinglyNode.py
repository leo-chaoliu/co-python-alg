
class SinglyNode:
    def __init__(self, item, link = None):
        self.item = item
        self.next = link
    
    def toString(self):
        return "[{}]".format(self.item) + ("->" if self.next != None else "")

def main():
    head = SinglyNode(123)
    print(head.toString())

    head = SinglyNode(456, head)
    print(head.toString())

    print(head.item)

if __name__ == "__main__":
    main()