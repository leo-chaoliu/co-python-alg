"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- Basic documentation only

"""

def binarySearch( array, target, low, high ):
    """ Recursive Binary Search.

        Return the index of [target] in [array], index[low...high]
    """
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if target > array[mid]:
        return binarySearch(array, target, mid+1, high)
    elif target < array[mid]:
        return binarySearch(array, target, low, mid-1)
    else:
        return mid

    

def main():
    #read user input
    array = [1,5,6,13,14,19,21,24,32]

    print(array)

    target = int(input("Enter target:"))
    loc = binarySearch(array, target, 0, len(array)-1)

    if loc != -1:
        print("Target can be found at %d"%loc)
    else:
        print("Target not found!")
    
if __name__ == "__main__":
    main()

