# merge two sorted array
def merge_two_sorted_array(arrayA, arrayB):
    result = []
    lenA = len(arrayA)
    lenB = len(arrayB)

    i = j = 0
    
    # O(n)
    while i<lenA and j<lenB:
        if arrayA[i]<arrayB[j]:
            result.append(arrayA[i])
            i += 1
        elif arrayA[i]>arrayB[j]:
            result.append(arrayB[j])
            j += 1
        else:
            result.append(arrayA[i])
            result.append(arrayB[j])
            i += 1
            j += 1
        pass

    if i==lenA:
        # extend the rest of B to result
        result.extend(arrayB[j:])
        pass
    else:
        result.extend(arrayA[i:])
        pass

    return result
    pass

# print(merge_two_sorted_array([1,4,5],[1,2,9,10]))

def merge_sort(array):
    # divide and sort
    if len(array) <= 1:
        return

    start = 0
    end = len(array)-1
    mid = len(array) // 2 - 1

    left = array[start: mid+1]
    right = array[mid+1: end+1]
    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_array(left, right)
    
    pass

def merge_sort_inner(array, start, end):
    if start == end:
        return 

    mid = (start+end) // 2
    
    merge_sort_inner(array, start, mid)
    merge_sort_inner(array, mid+1, end)

    pass

print(merge_sort([4,8,6,5,9,7]))