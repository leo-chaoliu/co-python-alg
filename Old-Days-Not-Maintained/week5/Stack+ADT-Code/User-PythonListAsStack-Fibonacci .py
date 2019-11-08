
#Our own stack implementations

def main():
    mystack = []
    
    #Initialize the first two fibonacci numbers
    mystack.append( 1 )
    mystack.append( 1 )

    for i in range(10):
        prev1 = mystack[-1]
        mystack.pop()
        prev2 = mystack[-1]

        cur = prev1 + prev2
        
        mystack.append( prev1 )
        mystack.append( cur )
        
        print(cur)

if __name__ == "__main__":
    main()

