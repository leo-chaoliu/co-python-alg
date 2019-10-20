def bubble_sort(array):
    # using two indices 
    # find the max in each iteration and put to the end
    for i in range(len(array)):
        
        for j in range(i+1, len(array)):
            if(array[i]>array[j]):
                helper.swap(array, i, j)

            j += 1
            i += 1

            if(i == len(array)-1):
                i = 0


bubble_sort([4,8,6,5,9,7])
