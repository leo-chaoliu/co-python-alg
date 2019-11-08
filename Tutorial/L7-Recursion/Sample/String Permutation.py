"""
For IT5003 - by SYJ 

Version 1.0 (2019 September)
- Basic documentation only

"""
def permutate( str ):
    """ Return all permutation of [str] as a list of strings."""
    if len(str) <= 1:
        return [str]
    
    result = []
    for idx in range(len(str)):
        letter = str[idx]
        leftover = str[:idx]+str[idx+1:]
        for substr in permutate(leftover):
            result.append(letter+substr)
    
    return result
   
def main():
    #read user input
    #note that the number of permutations is N!, where N is number of characters
    userInput = input("Enter a word: ")

    print(permutate(userInput))
    
if __name__ == "__main__":
    main()

