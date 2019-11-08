#region helpers
# private helper methods
def _swap_helper(array, indexA, indexB):
    print(array)

    tempValue = array[indexA]
    array[indexA] = array[indexB]
    array[indexB] = tempValue
    
    print(array)
    return array
#endregion

#region seleciton_sort
# idea
# select the max value in each loop
# put the max to the end until all sorted

def selection_sort_alg(array):
    #region explanation
    """
    # init
    length = len(array)
    sortedLength = 0

    # sort lenght-1 times will be enough
    while(sortedLength == length-1)

        every time select the first number as max_value, and keep its index as max_index

        # use an index cursor to move on, from 0 until reach the cursor = length-1-sortedlength-1 
            # compare the max value with the next value
            if array[cursor] > max_value
                copy the value to max and its index, to remember the max
            
            when cursor = length-1-sortedlength-1 
                swap the max and array[cursor]
            
            increase sortedLength 
    """
    #endregion

    print("staring")
    
    length = len(array)
    sortedLength = 0

    while( sortedLength < length - 1 ):
        max_index = 0
        max_value = array[0]

        # equal to: for(int i = 0; i<length-sortedLength; i++)
        for i in range(0, length-sortedLength):
            
            if(array[i] > max_value):
                max_index = i
                max_value = array[i]

            # index is the end of the checking list, swap max to the end
            if(i == length-sortedLength-1):
                # array will be affect after swapped by reference
                _swap_helper(array, i, max_index)

        sortedLength += 1
        print("i: {}, array: {}, sortedLength: {}".format(i, array, sortedLength))
    #endregion

#region insertion_sort
# idea
# holding all the number cards, and put first card on the table 
# put down(insert) the next card on the hand to the table

# more general
# holding all the cards in one hand
# choose the first one as sorted part
# put the next card to the sorted part by swapping
# repeat the last step until the end

def _insert_value_to_sorted_array(array, checking_index):
    # binary search
    length = len(array)
    value = array[checking_index]
    swich_index = 0

    # sorted length length // 2
    mid = (checking_index+1) // 2
    
    while(mid > 1):
        if(value >= array[mid-1]):
            # zoom to the right part
            mid = (length-mid) // 2
        else if(value < array[mid-1]):
            mid = mid // 2 

    _swap_helper(array, checking_index, mid)


def insertion_sort_alg(array):
    """
    """
    length = len(array)
    
    if(length <= 1):
        return array

    sorted_length = 1

    for i in range(1, length):
        
        if(array[i] < array[sorted_length-1]):
            # insert the value to sorted part
            _insert_value_to_sorted_array(array, i)
        sorted_length += 1


    #endregion


insertion_sort_alg([4,4,6,5,9,7])



   