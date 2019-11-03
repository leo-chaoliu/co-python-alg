class SinglyNode:
    def __init__(self,item,link = None):
        self.item = item
        self.next = link

    def toString(self):
        pass
        

class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.pointer = None
        self.size = 0

    def _Traversal(self,position):
        # travel to key-in position 
        ptr = self.pointer

        if position == 0:
            return self.tail
        
        for i in range (1,position): # test later
            # To handle special case (1 item only) 
            if ptr.next == None:
                return ptr
            else:
                ptr = ptr.next
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
            self.pointer = self.head

            if self.tail == None:
                self.tail = self.head
                self.tail.next = self.head
                                               
            # Insertion Case 3: End of Linked list 
        elif position==self.size+1:
            cur = self.tail 
            cur.next = newPtr
            self.tail = newPtr
            self.tail.next = self.head


            self.size += 1

        # Insertion case 4: Kth position (middle)
        else:
            prt = self._Traversal(position-1)
            cur = prt.next
            newPtr.next = cur
            prt.next = newPtr
            self.size +=1

    # def countCircle(self):
    #     cur = self.head
    #     while cur.head != self.head:
    #         cur = current.head
    
    def remove(self,position):
        # protection if 
        # if position == 0 or position > self.size:
        #     print("position == 0 or position > self.size, {0}, {1}".format(position, self.size))
        #     return False
        # detele head item

        removed_value = None

        prev = self._Traversal(position-1)
        print("prev node: {}", prev.item)
        cur = prev.next 
        
        if cur == self.head:
            cur = self.head
            removed_value = cur.item

            self.head = cur.next
            self.pointer = self.head
            self.tail.next = self.head

        # delete end item
        elif cur == self.tail:
            prev = self._Traversal(position-1)
            removed_value = prev.next.item

            prev.next = self.head
            self.tail = prev
            self.pointer = self.head
        # delete Kth position item 
        else:
            prev = self._Traversal(position-1)
            cur = prev.next
            removed_value = cur.item

            prev.next = cur.next
            self.pointer = prev.next
            
        self.size -=1

        return removed_value
        

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
    tll = CircularLinkedList()
    tll.insert(newPtr1,1)
    tll.insert(newPtr2,2)
    tll.insert(newPtr3,2)
    tll.remove(3)
    print(tll.toString())
  
if __name__ == "__main__":
    main()




    


    


