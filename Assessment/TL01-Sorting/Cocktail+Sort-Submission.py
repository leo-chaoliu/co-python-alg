import math

"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- For Lab 

"""

def swapElement(array, x, y):
    """
    swap array[x] with array[y]
    """
    #print("swap {:d} with {:d}".format(x, y))
    temp = array[x]
    array[x] = array[y]
    array[y] = temp


def bubbleSort(array, nPos, nPass):
    """
    Modified bubble sort on array:
    - stop after [nPass] 
    - sort up to and includes index [nPos]
    """

    # keep nPos+1 number to sort only
    n = nPos + 1 

    for i in range(n-1, 0, -1):
        number_of_passed = n-1-i

        if number_of_passed == nPass:
                break

        for j in range (1, i+1):
            if array[j-1] > array[j]:
                swapElement(array, j, j-1) 

def cocktailSort(array, nPos, nPass):
    """
    Cocktail sort on array:
    - stop after [nPass] 
    - sort up to and includes index [nPos]
    """

    length = nPos + 1
    
    for i in range(length):
        if i == nPass:
            break

        for j in range(length-1):
            if array[j+1] < array[j]:
                swapElement(array, j, j+1)

        for k in range(length-1-(i+1), 0, -1):
            if array[k] < array[k-1]:
                swapElement(array, k, k-1)         
 
def main():

    array = [283, 1560, 2150, 1061, 123, 2154, 222, 4]

    print("Before:", end='')
    print(array)

    #change the sort algorithm to test
    # sort = bubbleSort
    sort = cocktailSort

    #Uncomment ONE of the following sort() statement to test
    
    #this sort everything
    # sort(array, len(array)-1, len(array))

    #this do one round of the algorithm
    # sort(array, len(array)-1, 1)

    #this do two rounds of the algorithm
    sort(array, len(array)-1, 2)

    #this do three rounds
    #sort(array, len(array)-1, 3)

    #this sort the first four items 
    # sort(array, 3, 4)

    #this sort the first four items but 2 rounds only
    # sort(array, 3, 2)

    print("After :", end='')
    print(array)

if __name__ == "__main__":
    main()