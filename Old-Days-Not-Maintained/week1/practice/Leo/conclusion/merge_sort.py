import math

def merge_sort_recurtion(array):
    n = len(array)
    merge_sort_recurtion_common(array, 0, n-1)
    pass

def merge_sort_recurtion_common(array, start, end):
    # recursion base condition
    # divide until only one element left, then verse it back
    if start == end:
        return

    mid = (start + end) // 2
    
    merge_sort_recurtion_common(array, start, mid)
    merge_sort_recurtion_common(array, mid+1, end)
    
    merge_using_list(array, start, mid, end)

    pass

def merge_using_list(array, start, mid, end):
    '''merge two sorted array'''
    # cannot use the same arrayt to swap, it will caused the sorted array breaks
    # we use an extra list to store it temperary
    # space complexity O(n) using list
    # stable but not a in-place algorithm
    result = []

    if start<0:
        start = 0

    # left sorted part : st
    # art -> mid
    leftPointer = start

    # right sorted part: mid+1 -> end
    rightPointer = mid+1

    # move pointer respectly -> O(n) complexity
    while leftPointer<=mid and rightPointer<=end:
        if array[leftPointer]<array[rightPointer]:
            result.append(array[leftPointer])
            leftPointer +=1
        else:
            result.append(array[rightPointer])
            rightPointer +=1

    # append the rest to result
    while leftPointer<=mid:
        result.append(array[leftPointer])
        leftPointer +=1

    while rightPointer<=end:
        result.append(array[rightPointer])
        rightPointer +=1

    # replace the value from result to array
    for i in range(start, end+1):
        array[i] = result[i-start]

    pass

def merge_sort_iteration(array):
    n = len(array)
    for temp in range(1,(n-1)//2-1):
            i = 2 ** (temp-1)
            
            # if temp == 1:
                #  i = 1

            for j in range(1, n-1, i):
                merge_using_list(array, j-i, (i+j)//2, _min(i+j, len(array)-1))

def _min(a, b):
    if a>=b:
        return a
    else: 
        return b

# array = [4, 8, 6, 5, 9]
# merge_sort_iteration(array)
# print(array)
