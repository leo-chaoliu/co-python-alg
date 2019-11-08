#Our own stack / queue implementations
from StackList import StackList	#can use the linked list version
from QueueLinkedList import QueueLinkedList #can choose the circular array version


"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- Simple demonstraction of Stack and Queue

- Basic documentation only

"""

def isPalindrome( input ):
	""" Check whether [input] is a Palindrome.

		Return True if the [input] is a Palindrome. False otherwise.
	"""
	s = StackList()
	q = QueueLinkedList()

	for ch in input:
		s.push(ch)
		q.enqueue(ch)
	
	while not s.isEmpty():
		if s.getTop() != q.getFront():
			return False
		
		s.pop()
		q.dequeue()

	return True

 
def main():

	userInput = input("Enter a string: ")

	print(userInput,end='')
	if isPalindrome(userInput):
		print(" IS a Palindrome!")
	else:
		print("is NOT a Palindrome!")


if __name__ == "__main__":
    main()

