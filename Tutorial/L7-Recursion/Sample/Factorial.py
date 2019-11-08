def factorialI( k ):
    """ Iterative Factorial function.

        Returns k!
    """    
    result = 1
    for i in range(2, k+1 ):
        result *= i
    return result


def factorial( k ):
    """ Recursive Factorial function.

        Returns k!
    """  
    if k == 0:
        return 1
    
    return k * factorial(k-1)

def main():
    #read user input
    userInput = int(input("Enter a non-negative integer:"))

    print("Recursive Factorial %d = %d" % (userInput, factorial(userInput)))

    print("Iterative Factorial %d = %d" % (userInput, factorialI(userInput)))


if __name__ == "__main__":
    main()

