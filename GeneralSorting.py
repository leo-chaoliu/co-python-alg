from random import *   #for randomly generating the StockItem

"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- For TL01
"""
class StockItem:
    def __init__(self, name, barcode, price, stock):
        self._name = name
        self._barcode = barcode
        self._price = price
        self._stock = stock
    
    def toString(self):
        return "[%s|barcode=%8s|$=%.2f|S=%d]"%(self._name, self._barcode, self._price, self._stock)

    def __eq__(self, other):
        return self._price == other._price
    
    # override less than <
    def __lt__(self, other):
        if other is None:
            return False
        return self._price < other._price
    # >
    def __gt__(self, other):
        if other is None:
            return False

        if self._price == other._price:
            return self._stock < other._stock
        
        return self._price > other._price

    # >= ge
    def __ge__(self, other):
        if other is None:
            return False
        
        if self._price == other._price:
            return self._stock <= other._stock
        
        return self._price >= other._price
    
def swapElement(array, x, y):
    """
    swap array[x] with array[y]
    """
    #print("swap {:d} with {:d}".format(x, y))
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

def insertionSort(array):
    """
    Insertion sort on array
    """
    n = len(array)
    for i in range (1, n):
        next = array[i]
        j = i-1
        while j >= 0 and array[j] > next:
            swapElement(array, j+1, j)
            j = j-1
        array[j+1] = next




def main():
    l = []
    for i in range(5):
        l.append(StockItem("Item"+str(i), randrange(10000,99999), randrange(100,10000)/10, randrange(500)))

    #add a few items with the same price for testing
    l.append(StockItem("Item5",12345, l[3]._price, 200))
    l.append(StockItem("Item6",12346, l[3]._price, 778))
    l.append(StockItem("Item7",12347, l[3]._price, 25))
    
    print("Before Sorting:")
    for it in l:
        print(it.toString())

    insertionSort(l)        #this will generate an error initially

    print("\nAfter Sorting:")
    for it in l:
        print(it.toString())



if __name__ == "__main__":
    main()