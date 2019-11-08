#Our own stack implementations
from StackList import StackList
from StackLinkedList import StackLinkedList

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- Sample User Program: Tower of Hanoi game using Stack ADT

- Basic documentation only

"""

class TowerOfHanoi():
	""" Class representing a Tower of Hanoi puzzle game. """
	def __init__(self, nDiscs):
		""" Expects the [nDiscs] number of discs. 

			All discs will be placed on the first pole at the start.
		"""
		self._poles = [StackList() for i in range(3)]
		self._nDiscs = nDiscs
		for i in range(nDiscs,0,-1):
			self._poles[0].push(i)

	def move(self, src, dst):
		""" Move one disc from [scr] pole to [dst] pole. 
		
			[src] and [dst] are numbers [0..2]
		"""
		if src == dst:
			return True     #pretend we have moved
        
		if src < 0 or src > 2 or dst < 0 or dst > 2:
			return False	#illegal pole number

		if self._poles[src].isEmpty():
			return False		#no disc at the source pole
		
		srcDisc = self._poles[src].getTop()

		if (not self._poles[dst].isEmpty()) and \
			(srcDisc > self._poles[dst].getTop()) :
			return False		#destination pole has a larger disc
        
		#all checks passed, we can move safely
		self._poles[dst].push( srcDisc )
		self._poles[src].pop()

	def _displayPole(self, pole):
		copy = StackList()
		while not pole.isEmpty():
			disc = pole.getTop()
			print(disc)
			pole.pop()
			copy.push(disc)

		while not copy.isEmpty():
			pole.push(copy.getTop())
			copy.pop()
	
	def won(self):
		"""Check whether the puzzle has been solved. i.e. all discs in the last pole."""
		return self._poles[2].size() == self._nDiscs
	
	def display(self):
		"""
		Show the current state of the Tower of Hanoi game.

		Very simple (and not pretty). 
		"""
		for i in range(3):
			self._displayPole(self._poles[i])
			print("Pole "+ chr(ord('A')+i))
			print("------")

def main():
	toh = TowerOfHanoi(3)

	toh.display()

	srcPole = int(input("src pole [0,1,2; -1 dst exit]:"))
	dstPole = int(input("dst pole [0,1,2; -1 dst exit]:"))
	while srcPole >= 0 and dstPole >= 0 and not toh.won():
		if toh.move(srcPole, dstPole):
			print("Move Ok!")
		else:
			print("Illegal Move!")
		
		toh.display()
		if toh.won():
			print("Good work! Tower of Hanoi solved!")
		else:
			srcPole = int(input("src pole [0,1,2; -1 dst exit]:"))
			dstPole = int(input("dst pole [0,1,2; -1 dst exit]:"))



if __name__ == "__main__":
    main()

