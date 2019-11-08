"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- Basic documentation only

"""

def fibonacciI( n ):
    """ Iterative Fibonacci Function

        Returns Fib( n ).
    """
    if n <= 2:
        return 1
    
    prev1 = prev2 = 1
    for i in range(3, n+1):
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur

    return cur        

def fibonacci( n ):
    """ Recursive Fibonacci Function

        Returns Fib( n ).
    """
    if n <= 2:
        return 1
   
    return fibonacci(n-1) + fibonacci(n-2)
    

def main():
    #read user input
    userInput = int(input("N? [>0]:"))

    print("Recursive Fibonacci(%d) = %d"%(userInput, fibonacci(userInput)))
    print("Iterative Fibonacci(%d) = %d"%(userInput, fibonacciI(userInput)))

    
if __name__ == "__main__":
    main()

