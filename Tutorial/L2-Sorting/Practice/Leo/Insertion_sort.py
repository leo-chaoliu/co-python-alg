import helper
import binary_search

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        next = arr[i]

        # sortedStartIndex
        # compare backward with sorted part
        j = i-1

        while(j>=0 and arr[j] > next):
            helper.swap(arr, j+1, j)
            j -= 1
    
    return arr
    
def insertion_binary_sort(array):
    n = len(array)

    for i in range(1, n):
        next = array[i]

        # sortedStartIndex
        # compare backward with sorted part
        
        array[:i+1] = binary_search.binary_search_insert(array[:i+1])
    
    return array
# print(insertion_sort([4,8,6,5,9,7]))
print(insertion_binary_sort([4,8,6,5,9,7]))
        



