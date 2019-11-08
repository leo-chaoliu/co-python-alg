def move( From, To):
    print("Move from pole %s to pole %s" % (From, To))

def tower(N, Src, Dst, Tmp):
    """ Print the instruction to solve tower of hanoi with [N] discs.
        
        [Src], [Dst] and [Tmp] are the names of the poles.
    """
    if N == 1:
        move( Src, Dst)
    else:
        tower(N-1, Src, Tmp, Dst)
        move(Src, Dst)
        tower(N-1, Tmp, Dst, Src)
    
def main():
    #read user input
    userInput = int(input("How many discs? [>0]: "))

    tower(userInput, 'A', 'B', 'C')

if __name__ == "__main__":
    main()

