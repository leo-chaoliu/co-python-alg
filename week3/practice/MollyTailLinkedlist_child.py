
from MollyLinkLinkedlist import SinglyNode, LinkLinkedList 

class TailLinkedList(LinkLinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def _Traversal(self,position):
        return super()._Traversal(position)

    def insert(self,newPtr,position):
        # Insertion case 1: Empty Linked List
        # self.size += 1
        # self.head = newPtr

        # Inserttion case 2: Head of linked list 
        # case 1 & 2 can be combined using case 2 code
        if position == 1:
            self.size += 1
            cur =self.head
            newPtr.next = cur
            self.head = newPtr
            if self.tail == None:
                self.tail = self.head
                                
            # Insertion Case 3: End of Linked list 
        elif position==self.size+1:
            cur = self.tail 
            cur.next = newPtr
            self.tail = newPtr
            self.size += 1

        # Insertion case 4: Kth position (middle)
        else:
            prt = self._Traversal(position-1)
            cur = prt.next
            newPtr.next = cur
            prt.next = newPtr
            self.size +=1

 
    def toString(self):
        return super().toString()



def main():
    newPtr1 = SinglyNode("Harry Potter 1")
    newPtr2 = SinglyNode("Harry Potter 2")
    newPtr3 = SinglyNode("Harry Potter 3")
    cll = TailLinkedList()
    cll.insert(newPtr1,1)
    cll.insert(newPtr2,2)
    cll.insert(newPtr3,2)
    print(cll.toString())
  
if __name__ == "__main__":
    main()




    


    


