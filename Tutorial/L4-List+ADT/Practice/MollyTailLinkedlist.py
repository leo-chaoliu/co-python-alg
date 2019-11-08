class SinglyNode:
    def __init__(self,item,link = None):
        self.item = item
        self.next = link

    def toString(self):
        pass
        

class TailLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _Traversal(self,position):
        ptr = self.head
        for i in range (1,position): # test later
            if ptr.next == None:
                return ptr
            else:
                ptr = ptr.next
                return ptr
        return ptr

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
        result = ""
        cur=self.head
        for i in range(0,self.size):
            result += "{} -> ".format(cur.item)
            cur = cur.next
        return result



def main():
    newPtr1 = SinglyNode("Harry Potter 1")
    newPtr2 = SinglyNode("Harry Potter 2")
    newPtr3 = SinglyNode("Harry Potter 3")
    tll = TailLinkedList()
    tll.insert(newPtr1,1)
    tll.insert(newPtr2,2)
    tll.insert(newPtr3,2)
    print(tll.toString())
  
if __name__ == "__main__":
    main()




    


    


