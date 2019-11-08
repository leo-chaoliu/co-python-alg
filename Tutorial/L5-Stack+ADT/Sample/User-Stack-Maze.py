from enum import Enum

#Our own stack implementations
from StackList import StackList
from StackLinkedList import StackLinkedList

"""
For IT5003 - by SYJ 

Version 1.0 (2019 October)
- Sample User Program: Maze Exploration using Stack ADT

- Basic documentation only

"""

class Direction(Enum):
	""" Enum to represent the move directions. 

		Each enum also encode the changes to the (row, column)
	"""
	UP = (-1, 0)
	LEFT = (0, -1)
	DOWN = (1, 0)
	RIGHT = (0, 1)
	

class Maze():
	""" A class to represent a Maze to be explored.	"""
	
	NSIZE = 24        #fixed maze size for simplicity
	def __init__(self, filename):
		""" Initialize the maze from a text file. 

			Expects a 24 x 24 characters matrix, using the following characters:
			- One 'S' (start point)
			- One 'E' (exit point)
			- '*' is blocked, i.e. wall, cannot pass through
			- '.' is a corridor, i.e. can pass through
		"""
		self._maze = []

		self._maze.append(['*' for i in range(Maze.NSIZE+2)])
		file = open(filename,'r')
		for line in file:
			row = [ch for ch in ('*'+line.rstrip()+'*')]

			#Locate start and end cells
			if 'S' in row:
				self._start = (len(self._maze),row.index('S'))

			if 'E' in row:
				self._end = (len(self._maze), row.index('E'))	
			#print(row)
			self._maze.append(row)
		file.close()
		self._maze.append(['*' for i in range(Maze.NSIZE+2)])

		#print(self._maze)
		print('Start: ',end='')
		print(self._start)
		print('End: ',end='')
		print(self._end)

		#Prepare the path
		self._path = StackList()
		self._path.push(self._start)

	def _mark(self, position, marker):
		""" Helper method to mark a cell with a specific character [marker]"""
		self._maze[position[0]][position[1]] = marker

	def _move(self, current, direction):
		""" Construct the new coordinator base on the current coordinate and direction"""
		return (current[0]+direction[0], current[1]+direction[1])

	def _cellContent(self, position):
		""" Return the cell content, i.e. the character at [position]. 

		    [position] is a tuple (row, column).
		"""
		return self._maze[position[0]][position[1]]

	def _getUnvisitedPath(self, cur):
		""" Return a posible unblocked and unvisited direction from the [cur] cell.

		    The direction is returned as a Direction Enum.
		"""
		for d in Direction:
			newCell = self._move(cur,d.value)
			
			dest = self._cellContent(newCell)
			print(newCell,end='')
			print(dest)

			if dest == '.' or dest == 'E':
				return d.value
		
		return None

	def canExplore(self):
		""" Return whether we can continue explore the maze.

			Return False if we exhausted all posibilites (i.e. trapped). True, otherwise.
		"""
		return not self._path.isEmpty()

	def reachExit(self):
		""" Return whether we have reached the (Exit Point) of the maze."""
		if not self.canExplore():
			return False
		
		return self._path.getTop() == self._end

		
	def moveOnce(self):
		""" Make a single move. 
		
			Assume that the maze can still be explored, i.e. canExplore() == True.
		"""
		curCell = self._path.getTop()

		print("Current at ",end='')
		print(curCell)

		direction = self._getUnvisitedPath(curCell)
		print(direction)

		if direction == None:
			self._path.pop()
			self._mark(curCell, 'X')
			moved = False
		else:
			newCell = self._move(curCell, direction)
			if self._cellContent(newCell) != 'E':
				self._mark(newCell, '>')
			self._path.push(newCell)
			moved = True
		
		return moved

	def display(self):
		""" Display the entire Maze."""
		for row in self._maze:
			print(''.join(row))



def main():
	filename = input("Enter Maze File:")

	maze = Maze(filename)
	maze.display()

	user = input("Press Enter to move:")
	while not maze.reachExit():
		maze.moveOnce()
		maze.display()
		user = input("Press Enter to move:")

	print("Exited form Maze! Phew!!")

if __name__ == "__main__":
    main()

