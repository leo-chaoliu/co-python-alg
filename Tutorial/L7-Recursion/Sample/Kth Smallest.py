import random   #only for generating random list of numbers

"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- Basic documentation only

"""

def KthSmallest( array, k ):
    """ Return the [k]th Smallest item in [array].

        [k] is assumed to be between 1 to N (i.e. size of [array])
    """
    p = array.pop(-1)   #use the last element 
    left = []
    right = []

    for item in array:
        if item <= p:
            left.append(item)
        else:
            right.append(item)
    
    nLeft = len(left) + 1   # + 1 for the p itself

    if k == nLeft:
        return p
    
    if k < nLeft:
        return KthSmallest(left, k)
    
    return KthSmallest(right, k-nLeft)
   

def main():
    #get a random array with 10 values
    array = random.sample(range(20), 10)

    print(array)

    K = int(input("Enter Rank K: "))
    
    print("Item at rank [%d] is %d"%(K, KthSmallest(array, K) ))
    
if __name__ == "__main__":
    main()

