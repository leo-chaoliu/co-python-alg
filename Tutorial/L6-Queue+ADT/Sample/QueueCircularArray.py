from abc import ABC, abstractmethod     #Abstract Base Class
from SinglyNode import SinglyNode
from QueueBase import QueueBase
import ctypes

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- Queue ADT implemented using Python List 
    - Circular Array approach

- Basic documentation only

"""
class QueueCircularArray(QueueBase):
    """ Queue ADT implemented as Circular Array """
    MAXSIZE = 50    #arbitrarily chosen as example

    #Constructor
    def __init__(self):
        """Constructor. Create a static array of MAXSIZE."""
        self._items = (QueueCircularArray.MAXSIZE * ctypes.py_object)()
        self._size = 0
        self._front = 0
        self._back = QueueCircularArray.MAXSIZE -1

    def getFront(self):
        """ Return the front item of queue. None if queue is empty."""
        if not self.isEmpty():
            return self._items[self._front]
        else:
            return None
    
    def enqueue(self, newItem):
        """ Enqueue (i.e. add) [newItem] to the end of queue.
            Return True if enqueue is successful. False otherwise.
        """
        if self._size == QueueCircularArray.MAXSIZE:      
            return False
        else:	
            self._back = (self._back + 1 ) % QueueCircularArray.MAXSIZE
        self._items[self._back] = newItem
        self._size += 1

        return True


    def dequeue(self):
        """ Dequeue (i.e. remove) the front item from queue.
        
            Return True if an item has been dequeued. False otherwise.
        """
        if not self.isEmpty():
            self._front = ( self._front+1 ) % QueueCircularArray.MAXSIZE
            self._size -= 1
            return True
        else:
            return False
        
    def size(self):
        """ Return size of the Queue, i.e. number of items in queue."""
        return self._size
    
    def isEmpty(self):
        """ Return True if Queue is empty. False otherwise"""
        return self._size == 0

def main():
    q = QueueCircularArray()

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