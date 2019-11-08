from abc import ABC, abstractmethod     #Abstract Base Class
from SinglyNode import SinglyNode
from QueueBase import QueueBase

"""
For IT5003 - by SYJ 

Version 1.1 (2019 October)
- Fixed dequeue size 1 bug

Version 1.0 (2019 October)
- Queue ADT implemented using Linked List 
    - Circular Linked List with tail (LastNode) approach

- Basic documentation only

"""

class QueueLinkedList(QueueBase):
    """ Queue ADT implemented as Circular Linked List """

    def __init__(self):
        """Constructor. Create a circular linked list."""
        self._lastNode = None
        self._size = 0

    def getFront(self):
        """ Return the front item of queue. None if queue is empty."""
        if not self.isEmpty():
            return self._lastNode.next.item   
        else:
            return None
    
    def enqueue(self, newItem):
        """ Enqueue (i.e. add) [newItem] to the end of queue.
            Return True
        """
        newNode = SinglyNode(newItem)
    
        if self._lastNode == None:
            newNode.next = newNode
            self._lastNode = newNode
        else:
            newNode.next = self._lastNode.next
            self._lastNode.next = newNode
            self._lastNode = newNode
        
        self._size += 1
        return True

    def dequeue(self):
        """ Dequeue (i.e. remove) the front item from queue.
        
            Return True if an item has been dequeued. False otherwise.
        """
        if not self.isEmpty():
            firstNode = self._lastNode.next
            self._lastNode.next = firstNode.next

            if self._size == 1:     #special case
                self._lastNode = None

            self._size -= 1
            return True
        else:
            return False
        
    def size(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0

def main():
    q = QueueLinkedList()

    print("Queue size = ",end='')
    print(q.size(), end='')   
    print(" | Queue empty = ",end='')
    print(q.isEmpty())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Enqueued 1, 2, 3| Front = ",end='')
    print(q.getFront())

    print("Dequeue result = ",end='')
    print(q.dequeue())
    
    print("Front = ",end='')
    print(q.getFront())
    
    print("Queue emtpy = ",end='')
    print(q.isEmpty())
    
    print("Queue size = ",end='')
    print(q.size())

    q.dequeue()
    q.dequeue()
    q.dequeue()
    print("Dequeued 3 times, Queue emtpy = ",end='')
    print(q.isEmpty())
    
    print("Front = ",end='')
    print(q.getFront())


if __name__ == "__main__":
    main()