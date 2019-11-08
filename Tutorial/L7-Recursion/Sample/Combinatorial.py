"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- Basic documentation only

"""

def choose(k, n):
    """ Return ways to choose [k] items out of total [n] items.
    """ 
    if k > n:
        return 0

    if k == n or k == 0:
        return 1
    
    return choose(k - 1, n - 1) + choose(k, n - 1)


def main():
    #read user input
    N = int(input("Total items [N]: "))
    K = int(input("Number of choices [K]: "))
    
    print("%d choose %d = %d"%(N, K, choose(K, N)))




if __name__ == "__main__":
    main()

