from abc import ABC, abstractmethod     #Abstract Base Class

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- Implemented Queue (FIFO order) ADT:
    - Specification:  QueueBase Base Class
    - Implementations: 
        A. Python List - Circular Array (QueueCircularArray Class)
        B. LinkedList (QueueLinkedList Class)

- Basic documentation only

"""

class QueueBase(ABC):
    """
    Base class for Queue ADT
    """
    @abstractmethod
    def getFront(self):
        """ Return the front item of queue. None if queue is empty."""
        pass

    @abstractmethod
    def enqueue(self, newItem):
        """ Enqueue (i.e. add) [newItem] to the end of queue."""
        pass

    @abstractmethod
    def dequeue(self):
        """ Dequeue (i.e. remove) the front item from queue."""
        pass

    @abstractmethod
    def size(self):
        """ Return size of the Queue, i.e. number of items in queue."""
        pass
    
    @abstractmethod
    def isEmpty(self):
        """ Return True if Queue is empty. False otherwise"""
        pass

def main():
    q = QueueBase()

    #should fail as StackBase is an abstract class
    print(q.size())   
    print(q.isEmpty())


if __name__ == "__main__":
    main()