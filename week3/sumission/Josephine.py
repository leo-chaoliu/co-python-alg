"""
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
        pass    #replace with your code

    def chosenOne(self, K):
        """ Return a list of princes in the order they are removed.

            e.g. [2, 4, 3, 1] with N = 4, K = 2, the last prince is the chosen one.
        """
        return []   #replace with your code

    def toString(self):
        """ Can print out some information for debugging purpose. 
            Not part of the evaluation.
        """
        return ""
        



def main():

    #A simple main so that you can easily test your own Josephine
    
    N = int(input("N = "))
    K = int(input("K = "))

    j = Josephine(N)
    print(j.toString())

    print(j.chosenOne(K))


if __name__ == "__main__":
    main()