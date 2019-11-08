import helper

def insertion_sort(array):
    n = len(array)
    
    sortedCount = 1

    while sortedCount <= n:

        # compare all the number from the left sorted array 0->sortedCount-1
        for i in range(0, sortedCount):
            if array[i] > array[sortedCount]:
                helper.swap(array, i, sortedCount)


    pass