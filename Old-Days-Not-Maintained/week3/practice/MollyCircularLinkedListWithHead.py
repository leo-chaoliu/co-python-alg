

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
        self.size = 0

    def isEmpty(self):
        """ Return True if List is empty. False otherwise"""
        return self.size == 0
    
  
    def getLength(self):
        """ Return size of the list, i.e. number of items"""
        return self.size

    def _traverse(self, index):
        """ Internal helper method. Return a reference to it. "index"-th item."""
                
        if index < 1 or index > self.size:
            return None 
        
        if index == self.size:
            return self.tail
        else:
            ptr = self.head

            for i in range(1,index):
                ptr = ptr.next

            return ptr

    def insert(self, index, newItem):
        """ Insert [newItem] at [index]
            - [index] ranges from [1... current length+1]

            Return True if item can be inserted. False otherwise.
        """
        if index < 0 or index > self.size+1:
            return False

        newNode = SinglyNode(newItem) 

        if index == 1:
            # check if empty
            if self.size == 0:
                self.head = newNode
                self.tail = newNode
            else:
                # if not empty
                newNode.next = self.head
                self.head = newNode
       
        elif index == self.size+1 :
            # if insert to the end
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
        
        else:
            # if insert to between
            prev = self._traverse(index-1)
            newNode.next = prev.next
            prev.next = newNode

        # print('inserted: {}'.format(newNode.item))
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
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        
        else:
            prev = self._traverse(index -1)
            cur = prev.next 
            prev.next = cur.next
           
            if index == self.size:
                self.tail = prev
                self.tail.next = self.head

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
        str_ = "Size[{}]".format(self.size)
        
        # protection if
        if self.head == None:
            return 
        
        # add the first node to print list
        str_ += self.head.toString()
        # add the rest node to print list
        ptr = self.head.next
        
        while ptr != self.head:
            str_ += ptr.toString() 
            ptr = ptr.next
        
        return str_

def main():
    l = CircularLinkedList()

    # print(l.toString())

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

    while l.getLength() > 0:
        l.remove(1)
    print(l.toString())


if __name__ == "__main__":
    main()
