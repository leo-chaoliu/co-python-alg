from SinglyNode import SinglyNode

"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)

- Use the Linked List from List ADT lecture

- Basic documentation only

"""

class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
    
    def traverse(self, index):
        if index < 1 or index > self._size:
            return None
        
        ptr = self._head
        for i in range(1, index):
            ptr = ptr.next
        return ptr
        
    def insert(self, item, index):
        if index < 1 or index > self._size+1:
            return

        newPtr = SinglyNode(item) #Create a new node
        if index == 1:
            newPtr.next = self._head
            self._head = newPtr
        else:
            prev = self.traverse(index-1)
            newPtr.next = prev.next
            prev.next = newPtr  
        self._size += 1

    def delete(self, index):
        if index < 1 or index > self._size:
            return
        
        if index == 1:
            cur = self._head
            self._head = self._head.next
        else:
            prev = self.traverse(index-1)
            cur = prev.next
            prev.next = cur.next
        #In language with no auto garbage collection
        # need to dispose of the memory used by node
        # referred by cur
        self._size -= 1

    def _printLL(self, n):
        if n != None:
            self._printLL(n.next)
            print("%d " %(n.item),end='')
    
    def print(self):
        """ Driver method to start the recursive printing."""
        self._printLL(self._head)

    def toString(self):
        ptr = self._head
        str = "Size[{:d}] | ".format(self._size)
        while ptr != None:
            str += ptr.toString()
            ptr = ptr.next
        return str

def main():
    l = SinglyLinkedList()

    l.insert(100,1)
    l.insert(200,2)
    l.insert(50,1)
    l.insert(300, 4)
    l.insert(75,2)
    l.insert(250, 5)
 
    l.print()


if __name__ == "__main__":
    main()