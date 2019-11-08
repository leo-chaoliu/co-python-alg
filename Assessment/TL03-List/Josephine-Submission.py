
"""
For IT5003 Lab - by SYJ 

Version 1.0 (2019 October)
- Singly Node is reused from Linked List implementations.
"""


class SinglyNode:
    def __init__(self, item, link = None):
        self.item = item
        self.next = link
    
    def toString(self):
        """Print the Node's item and a "->" if the next reference is valid."""
        return "[{}]".format(self.item) + ("->" if self.next != None else "")

class Josephine:
    def __init__(self, N):
        """ Initialize the circle of [N] princes. N > 0.
        
            Restriction: Must use circular linked list.
        """
        
        self.princes = CircularLinkedList() 
        for i in range(1, N+1):
            #Encapsulation
            prince_i = SinglyNode(i)
            self.princes.insert(i,prince_i)


    def chosenOne(self, K):
        """ Return a list of princes in the order they are removed.

            e.g. [2, 4, 3, 1] with N = 4, K = 2, the last prince is the chosen one.
        """
        result = []

        while self.princes.size > 1:
            k_mod = K % self.princes.size

            if k_mod == 0:
                k_mod = self.princes.size

            removed_value = self.princes.remove(K)
            print('removed_value: ', removed_value)
            result.append(removed_value)
        
        result.append(self.princes.pointer.item)

        return result   #replace with your code

    def toString(self):
        """ Can print out some information for debugging purpose. 
            Not part of the evaluation.
        """
        return self.princes.toString()
        
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
        self.pointer = None
        self.size = 0

    def isEmpty(self):
        """ Return True if List is empty. False otherwise"""
        return self.size == 0
    
    def getLength(self):
        """ Return size of the list, i.e. number of items"""
        return self.size

    def _traverse(self, index):
        """ Internal helper method. Return a reference to it. "index"-th item."""
                
        # if index < 1 or index > self.size:
        #     return None 
        
        # if index == self.size:
        #     return self.tail
        # else:
           
        ptr = self.pointer

        if index == 0:
            return self.tail

        for i in range(1,index):
            ptr = ptr.next

        return ptr

    def insert(self, index, newNode):
        """ Insert [newItem] at [index]
            - [index] ranges from [1... current length+1]

            Return True if item can be inserted. False otherwise.
        """
        if index < 0 or index > self.size + 1 :
            return False

        # newNode = SinglyNode(newItem) 

        if index == 1:
            # check if empty
            if self.size == 0:
                self.tail = newNode
                self.tail.next = newNode
                self.pointer = self.tail.next
            else:
                # if not empty
                head = self.tail.next
                newNode.next = head
                self.tail.next = newNode
                self.pointer = self.tail.next
       
        elif index == self.size+1 :
            # if insert to the end
            head = self.tail.next
            self.tail.next = newNode
            newNode.next = head
            self.tail = newNode

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
        # if index < 1 or index > self.size:
        #     return False
        
        # function scope variable 
        removed_value = None 

        prev = self._traverse(index-1)
        cur = prev.next
        
        if cur == self.tail.next: 
            if self.size == 1:
                removed_value = self.tail.item
                self.tail = None
            else:
                head = self.tail.next
                removed_value = head.item
                self.tail.next = head.next
                self.pointer = self.tail.next

        else:
            prev = self._traverse(index -1)
            cur = prev.next 
            removed_value = cur.item
            prev.next = cur.next
            self.pointer = prev.next
           
            if cur == self.tail:
                self.tail = prev

        self.size -=1

        return removed_value
    
   
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
        if self.tail == None:
            return 
        
        head = self.tail.next
        # add the first node to print list
        str_ += head.toString()
        # add the rest node to print list
        ptr = head.next
        
        while ptr != head:
            str_ += ptr.toString() 
            ptr = ptr.next
        
        return str_
        

def main():

    #A simple main so that you can easily test your own Josephine
    
    N = int(input("N = "))
    K = int(input("K = "))

    j = Josephine(N)
    print(j.toString())

    print(j.chosenOne(K))


if __name__ == "__main__":
    main()