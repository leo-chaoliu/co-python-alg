

class SinglyNode:
    def __init__(self, item, link=None):
        self.item = item
        self.next = link

    def toString(self):
        """Print the Node's item and a "->" if the next reference is valid."""
        return"{}".format(self.item) + ("->" if self.next != None else "")

class CircularLinkedList:
    
    def __init__(self):
        self.tail = None
        self.head = None # consider self.head = self.tail.next???
        # self.pointer = None 
        self.size = 0

    def isEmpty(self):
        """ Return True if List is empty. False otherwise"""
        return self.size == 0
    
  
    def getLength(self):
        """ Return size of the list, i.e. number of items"""
        return self.size

    def _traverse(self, index):
        """ Internal helper method. Return a reference to it. "index"-th item."""
                
        if index < 1 or index > self.size + 1:
            return None 
        
        ptr = self.head
        for i in range(1,index):
            ptr = ptr.next
        return ptr



    def insert(self, index, newItem):
        """ Insert [newItem] at [index]
            - [index] ranges from [1... current length+1]

            Return True if item can be inserted. False otherwise.
        """
        if index < 0 or index > self.size + 1:
            return False

        newItem = SinglyNode(newItem) 
        if index == 1:
            newItem.next = self.head
            self.head = newItem
       
        else:
            prev = self._traverse(index-1)
            newItem.next = prev.next
            prev.next = newItem

        self.size += 1

        return True
    
  
    def remove(self, index):
        """ Remove item at [index]
            - [index] ranges from [1... current length]

            Return True if item can be deleted. False otherwise.
        """
        if index < 1 or index > self.size:
            return False
        
        if index == 1: 
            self.head = self.head.next

        else:
            prev = self._traverse(index -1)
            cur = prev.next 
            prev.next = cur.next

        self.size -=1

        return True
    
   
    def retrieve(self, index):
        """ Return item if [index] is valid. None otherwise."""
        if index < 1 or index > self.size:
            return False
        
        cur = self._traverse(index)
        return cur.item
   
    
    def toString(self):
        """ Simple string representation of all items in list"""
        ptr = self.head
        str = "Size[{}]".format(self.size)
        while ptr != None:
            str += ptr.toString() 
            ptr = ptr.next
        
        return str



def main():
    l = CircularLinkedList()

    print(l.toString())

    l.insert(1, 100)
    l.insert(2, 200)
    l.insert(1, 50)
    l.insert(4, 300)
    l.insert(2, 75)
    l.insert(5, 250)
    print(l.toString())

    l.remove(1)
    print(l.toString())

    l.remove(l.getLength())
    print(l.toString())

    l.remove(3)
    print(l.toString())

    # while l.getLength() > 0:
    #     l.remove(1)
    # print(l.toString())


if __name__ == "__main__":
    main()
