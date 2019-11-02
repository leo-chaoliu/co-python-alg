"""
For IT5003 Lab - by SYJ 

Version 1.0 (2019 October)
- Singly Node is reused from Linked List implementations.
"""

from MollyCircularLinkedlist import CircularLinkedList

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
            self.princes.insert(prince_i,i)

        pass    #replace with your code

    def chosenOne(self, K):
        """ Return a list of princes in the order they are removed.

            e.g. [2, 4, 3, 1] with N = 4, K = 2, the last prince is the chosen one.
        """
        result = []
        # K = K % self.princes.size

        while self.princes.size > 1:
            removed_value = self.princes.remove(K)
            print('removed_value: ', removed_value)
            result.append(removed_value)
        
        result.append(self.princes.head.item)

        return result   #replace with your code

    def toString(self):
        """ Can print out some information for debugging purpose. 
            Not part of the evaluation.
        """
        return self.princes.toString()
        



def main():

    #A simple main so that you can easily test your own Josephine
    
    # N = int(input("N = "))
    # K = int(input("K = "))

    j = Josephine(20)
    print(j.toString())

    print(j.chosenOne(1314))


if __name__ == "__main__":
    main()