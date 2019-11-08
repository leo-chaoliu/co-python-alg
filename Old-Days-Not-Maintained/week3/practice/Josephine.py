"""
For IT5003 Lab - by SYJ 

Version 1.0 (2019 October)
- Singly Node is reused from Linked List implementations.
"""

from MollyCircularLinkedListWithoutHeadWithPointer import CircularLinkedList

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
        



def main():

    #A simple main so that you can easily test your own Josephine
    
    # N = int(input("N = "))
    # K = int(input("K = "))

    j = Josephine(4)
    print(j.toString())

    print(j.chosenOne(777))


if __name__ == "__main__":
    main()