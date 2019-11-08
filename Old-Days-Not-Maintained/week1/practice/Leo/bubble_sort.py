import helper

def bubble_sort(array):
    # using two indices 
    # find the max in each iteration and put to the end
    length = len(array)

    # stop condition: when the max couter == length -1

    # i as the sorted counter
    for i in range(0,length-1):
        # pair compare and move forword
        # will get the max every time, which will be sorted
        # only need length-1 number to be sorted
        for j in range(length-1-i):
            # i number has been sorted
            if(array[j] > array[j+1]):
                helper.swap(array, j, j+1)
    
    return array

print(bubble_sort([4,8,6,5,9,7]))

        