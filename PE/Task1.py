"""

For IT5003 PE - by SYJ 

- StackList is simplified (removed Base Class) for PE



"""



class StackList:

    """

    Stack ADT implementation using Python List, i.e. a dynamic array

    """

    def __init__(self):

        self._items = []



    def getTop(self):

        """ Return the top item of stack. None if stack is empty."""

        if not self.isEmpty():

            return self._items[-1]    #negative index = count from the end of list

        else:

            return None



    def push(self, newItem):

        """ Push (i.e. add) [newItem] on top of stack."""

        self._items.append(newItem)



    def pop(self):

        """ Pop (i.e. pop) [newItem] from top of stack."""

        if not self.isEmpty():

            self._items.pop()         #last item is removed

            return True

        else:

            return False



    def size(self):

        """ Return size of the Stack, i.e. number of items"""

        return len(self._items)

    

    def isEmpty(self):

        """ Return True if Stack is empty. False otherwise"""

        return len(self._items) == 0





def candyCrush( L ):

    """ L is a list of candies, represented as number [1..4]"""



    #Use only one stack s to solve the problem

    s = StackList()



    #your solution below, make sure s contains the crushed candies at the end

    



    s.push(L[0])

    n= len(L)

    for i in range(1,n):

            temp = s.getTop()

            if L[i] == temp:

                s.pop()

                r_value = L[i]%4 +1

                temp2 = s.getTop()



                if r_value ==temp2:

                    s.pop()

                    r_value2 = r_value%4 +1

                    s.push(r_value2)



                else:

                    s.push(r_value)



            else:

                s.push(L[i])





          



    output = s

            

     

    

    

    

    #do NOT modify the code below

    #place the content of stack s into output list to be returned.

    output = []

    while not s.isEmpty():

        output.append( s.getTop())

        s.pop()

    

    return output







def main():

    # print(candyCrush([4,3,2,1,1]))
    
    print(candyCrush([3,1,1,3]))
    print(candyCrush([4,3,2,1,1]))
    print(candyCrush([1,1]))






if __name__ == "__main__":

    main()

