import math
import Molly_Practice_Helper
    

## Practice Sorting

def selectionSort(array):
    n = len(array)
    
    for i in range(n-1,0,-1):
        maxIdx = i
       
        for j in range(0,i+1):
            
            if array[j] > array[maxIdx]:
                maxIdx = j
        Molly_Practice_Helper.swapElement(array,maxIdx,j)

def insertionSort(array):
    n = len(array)
    # for loop is to control that from 1 position until n-1 postion 
   
    for i in range(1,n):
        next = array[i] # next is the item to be inserted
        j = i-1
        # While loop is to find the right place to insert next=array[i]
       
        while j >= 0 and array[j]>next:
            Molly_Practice_Helper.swapElement(array,j+1,j)
            j = j-1
        
def bubbleSort(array):
    n = len(array)
    # for loop to control from n-1 postion until 1 position
   
    for i in range(n-1,0,-1):
        isSorted = True # Assume the array is sorted before the inner loop
        # findin the largest num and move to i position
       
        for j in range(1,i+1):
            
            if array[j-1] > array[j]:
                Molly_Practice_Helper.swapElement(array,j,j-1)
                isSorted = False # Any swapping will invalidate the assumption
        if isSorted:
            return  # If the flag remains true after the inner loop. means sorted

# To make mergeSort() consistent with other sorting algorithm (which take in only one array as parameter)
# Only to kick start the first recursive mergeSort() function with the right parameter

def mergeSortHelper(array):
    mergeSort(array,0,len(array)-1) 

def mergeSort(array,low,high):
    
    if low < high:
        mid = (low + high)//2

        mergeSort(array,low,mid)
        mergeSort(array,mid+1, high)
        merge(array,low,mid,high) # Conquer: merge the two sorted halves

def merge(array,low,mid,high):
    n = high - low + 1 
    left = low 
    right = mid + 1
    result = [] # result is a temporary array to store result
    print("Merge [{:d}-{:d}] with [{:d}-{:d}]".format(low, mid, right, high))
   
   # Normal Merging where both halves unmerged items
   
    while left <= mid and right <= high: 
       
        if array[left] <= array[right]:
            result.append(array[left])
            left = left + 1
       
        else:
            result.append(array[right])
            right = right +1 
    # remaining item are copied into result[]
   
    while left <= mid:
        result.append(array[left])
        left = left + 1 
   
    while right <= high:
        result.append(array[right])
        right = right + 1
    # Merged result are copied back into array[]
    
    for k in range(0,n):
        array[low+k] = result[k]

def quickSortHelper(array):
    """
    Quick sort wrapper so that this function takes in the same parameter with
    all other sorting functions.
    """
    quickSort(array, 0, len(array)-1)

def quickSort(array,low,high):
    """
    Quick sort on array[low..high]
    """
    if low < high :
        pivotIdx = partition(array,low,high)

        quickSort(array,low,pivotIdx-1)
        quickSort(array,pivotIdx+1,high)


def partition(array, i, j):
    """
    Partition function: User array[i] to partition array[i+1...j] into two subarrays. 
    Left array <= array[i], right array > array[i]
    Return index of array[i] after placing it at the end of left array
     """
    pivot = array[i]
    middle = i

    for k in range(i+1,j+1):
        if array[k] < pivot:
            middle = middle +1 
            Molly_Practice_Helper.swapElement(array,k,middle)
    
    Molly_Practice_Helper.swapElement(array,i,middle)

    return middle

# only suitable to sort numbers
def radixSort(array):
   # count how many digit of the largest number inside the array
    numDigit = int(math.log10(max(array))) + 1
   
    for power in [10**i for i in range(numDigit)]:
        digitBin = [[]for d in range(10)]
        # Organize all items in array into "bins" based on specific digit, as indicated by the power 
        distribute(array,digitBin,power)
        #Place items from the "bins" back into array, i.e. "concatenate" the group
        collect(digitBin,array)

def distribute(array,digitBin,power):
    """
    Distribute number in array into 10 subarrays based on the digit at power position.
    """ 
    for item in array:
        digit = (item//power)%10
        digitBin[digit].append(item)

    # print("Distribute [Power = {:d}]".format(power))
    # print(list(enumerate(digitBin,0)))

def collect(digitBin,array):
    """
    Collect number in from 10 subarrays into a single array.
    """
    startIdx = 0

    for eachBin in digitBin:
        array[startIdx:] = eachBin
        startIdx += len(eachBin)

    # print("Collect")
    # print(array)




## Copy from Leturer for testing 
def main():
    array1 = [2, 3, 5, 7, 11, 13, 17]
    array2 = [17, 13, 11, 7, 5, 3, 2]
    array3 = [11, 2, 5, 7, 3, 17, 13]
    array4 = [11, 2, 11, 2, 11, 2]
    array5 = [123, 2154, 222, 4, 283, 1560, 1061, 2150]

    #uncomment one of the following to test a specific sorting algorithm
    # sort = selectionSort
    # sort = insertionSort
    # sort = bubbleSort
    #sort = bubbleSortEarly
    # sort = mergeSortHelper
    # sort = quickSortHelper
    sort = radixSort

    #uncomment one or more sorting examples below
    # sort(array1)
    # print(array1)

    # sort(array2)
    # print(array2)

    # sort(array3)
    # print(array3)

    # sort(array4)
    # print(array4)

    sort(array5)
    print(array5)

if __name__ == "__main__":
    main()
                
        
