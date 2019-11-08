
# # private function
# def __binary_search_recursion_core(array, target, start, end):
#     # mid= (end-start)//2 + start
#     mid = (end + start) // 2

#     if target>array[mid]:
#         return __binary_search_recursion_core(array,target, mid+1, end)
#     elif target<array[mid]:
#         return __binary_search_recursion_core(array,target,0,mid-1)
#     elif target == array[mid]:
#         return mid
    
#     return -1

# def binary_search_recursion(array, target):
#     return __binary_search_recursion_core(array, target, 0, len(array)-1)

# def binary_search_iteration(array, target):
#     # using start and end two indices to squeeze the searching area
#     # until start >= end 

#     length = len(array)
#     start = 0
#     end = length - 1

#     while end > start :
#         # mid = (end - start) // 2 + start
#         mid = (end + start) // 2

#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
        
#     return -1

# [2,3,4,6] 2
def binary_search_insert_index(array, target):
    length = len(array)
    insert_index = 0
    start = 0   
    end = length - 1
    
    if length == 0 :
        return 0

    if target>=array[end]:
        insert_index = end+1
    elif target<=array[start]:
        insert_index = start
    else:
        # is in the middle
        # find the position 
        while end>=start  :
            mid = (start+end)//2

            if target>=array[end]:
                insert_index = end+1
                break
            elif target<=array[start]:
                insert_index = start
                break
            
            if end == start:
                insert_index = end+1
                break

            if target == array[mid]:
                insert_index = mid+1
                break
            
            if end-start == 1:
                insert_index = end
                break
            
            if target>array[mid]:
                start=mid+1
            else:
                end=mid-1

    return insert_index
    
def binary_search_insert(array):
    sortedArr = array[:-1];
    target = array[-1]
    index = binary_search_insert_index(sortedArr, target)
    sortedArr.insert(index, target)
    print(sortedArr)
    return sortedArr

testArr1 = [4,5,6,8,9]
target1 = 5.5
# print("binary_search_iteration: {}".format(binary_search_iteration(testArr1, target1)))
# print("binary_search_recursion: {}".format(binary_search_recursion(testArr1, target1)))
print(binary_search_insert_index(testArr1, target1))