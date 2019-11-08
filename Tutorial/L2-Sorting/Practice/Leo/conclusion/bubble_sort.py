import helper

def bubble_sort(array):
    n = len(array)

    # i represent how many number has been sorted to the end
    # at most need to sort n-1 numbers, n-1 times
    for i in range(0, n-1):
        # no need to compare i largest numbers
        for j in range(0, n-1-i):
            # compare current pos with its next
            # move the bigger to end
            if array[j]>array[j+1]:
                helper.swap(array, j, j+1)

array = [4,8,6,5,9,7,0]
bubble_sort(array)
print(array)
