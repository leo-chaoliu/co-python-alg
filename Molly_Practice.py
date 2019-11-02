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
    sort = mergeSortHelper
    #sort = quickSortHelper
    # sort = radixSort

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
                
        
