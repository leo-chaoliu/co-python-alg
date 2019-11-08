def swap(array, indexA, indexB):
    tempValue = array[indexA]
    array[indexA] = array[indexB]
    array[indexB] = tempValue
    
    return array