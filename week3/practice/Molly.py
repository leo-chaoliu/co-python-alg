class SinglyNode:
    def __init__(self,item,link = None):
        self.item = item
        self.next = link

    def toString(self):
        return "[Node: item: {0} next {1} next next: {2}".format(self.item, self.next.item, self.next.next.item)

class LinkLinkedList():
    def __init__(self):
        self.head = None
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
        
            # Insertion Case 3 & 4: End of Linked list & Kth Postion (Middle)
        elif position==self.size+1:
            prt = self._Traversal(position)
            newPtr.next = prt.next
            prt.next = newPtr
            # newPtr.next = prt.next
            self.size += 1
        else:
            prt = self._Traversal(position-1)
            cur = prt.next
            newPtr.next = cur
            prt.next = newPtr
            self.size +=1

    
    
    def toString(self):
        return "head : {}".format(self.head.toString())



def main():
    newPtr1 = SinglyNode("Harry Potter 1")
    newPtr2 = SinglyNode("Harry Potter 2")
    newPtr3 = SinglyNode("Harry Potter 3")
    ll = LinkLinkedList()
    ll.insert(newPtr1,1)
    ll.insert(newPtr2,2)
    ll.insert(newPtr3,2)
    print(ll.toString())

if __name__ == "__main__":
    main()




    


    


