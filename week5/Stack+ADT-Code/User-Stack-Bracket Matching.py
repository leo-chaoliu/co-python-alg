#Our own stack implementations
from StackList import StackList
from StackLinkedList import StackLinkedList

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- Sample User Program: Bracket Matching using Stack ADT

- Basic documentation only

"""

def matchBracket( input ):
	""" Return true if the brackets in [input] matches."""
	openBrackets = ['(','[','{']
	closeBrackets = [')',']','}']
	bracketStack = StackList()
     
	
	for cur in input:
		if cur in openBrackets:	#cur is an open bracket
			idx = openBrackets.index(cur)
			bracketStack.push(closeBrackets[idx])
		elif cur in closeBrackets:
			if bracketStack.isEmpty() or \
				bracketStack.getTop() != cur:
				return False
			else:
				bracketStack.pop()
	
	return bracketStack.isEmpty()

 
def main():

	userInput = input("Enter a math expression:")
	if matchBracket(userInput):
		print("Bracket matched!")
	else:
		print("Bracket NOT matched!")


if __name__ == "__main__":
    main()

