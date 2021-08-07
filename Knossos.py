import random
import time
import os

## Functions
def populateLab():
	for i in range(0, labHeight):
		line = []
		for j in range(0, labWidth):
			line.append(unvisited)
		lab.append(line)

# Set starting point and add walls around
def setStartingPoint():	# Randomize starting point and set it a cell
	global starting_labHeight
	global starting_labWidth
	starting_labHeight = int(random.random()*labHeight)
	starting_labWidth = int(random.random()*labWidth)
	if (starting_labHeight == 0):
		starting_labHeight += 1
	elif (starting_labHeight == labHeight-1):
		starting_labHeight -= 1
	if (starting_labWidth == 0):
		starting_labWidth += 1
	elif (starting_labWidth == labWidth-1):
		starting_labWidth -= 1


def setStartingWalls():
	lab[starting_labHeight][starting_labWidth] = cell
	walls.append([starting_labHeight - 1, starting_labWidth]) 
	walls.append([starting_labHeight, starting_labWidth - 1])
	walls.append([starting_labHeight, starting_labWidth + 1])
	walls.append([starting_labHeight + 1, starting_labWidth])

	# Denote walls in lab
	lab[starting_labHeight-1][starting_labWidth] = 'w'
	lab[starting_labHeight][starting_labWidth - 1] = 'w'
	lab[starting_labHeight][starting_labWidth + 1] = 'w'
	lab[starting_labHeight + 1][starting_labWidth] = 'w'


# Check which random wall was selected
def checkWalls():
	look = Point (rand_wall.x, rand_wall.y)
	if (rand_wall.y != 0): # left
		if look.left(lab) == 'u' and look.right(lab) == 'c':
			return 'Left'

	if (rand_wall.x != 0): # upper
		if look.up(lab) == 'u' and look.down(lab) == 'c':
			return 'Top'
		
	if (rand_wall.x != labHeight-1): # bottom
		if look.down(lab) == 'u' and look.up(lab) == 'c':
			return 'Bottom'

	if (rand_wall.y != labWidth-1): # right
		if look.right(lab) == 'u' and look.left(lab) == 'c':
			return 'Right'
		
	return 'Invalid'

def buildWall(wall):
	look = Point (rand_wall.x, rand_wall.y)
	if wall == 'Right':
		if look.right(lab) != 'c':
			lab[rand_wall.x][rand_wall.y + 1] = 'w'
		if ([rand_wall.x, rand_wall.y + 1] not in walls):
			walls.append([rand_wall.x, rand_wall.y + 1])
	elif wall == 'Down':
		if look.down(lab) != 'c':
			lab[rand_wall.x + 1][rand_wall.y] = 'w'
		if ([rand_wall.x + 1, rand_wall.y] not in walls):
			walls.append([rand_wall.x + 1, rand_wall.y])
	elif wall == 'Up':	
		if look.up(lab) != 'c':
			lab[rand_wall.x - 1][rand_wall.y] = 'w'
		if ([rand_wall.x - 1, rand_wall.y] not in walls):
			walls.append([rand_wall.x - 1, rand_wall.y])
	elif wall == 'Left':
		if look.left(lab) != 'c':
			lab[rand_wall.x][rand_wall.y - 1] = 'w'
		if ([rand_wall.x, rand_wall.y - 1] not in walls):
			walls.append([rand_wall.x, rand_wall.y - 1])

# Find number of surrounding cells
def surroundingCells(rand_wall):
	look = Point (rand_wall.x, rand_wall.y)
	s_cells = 0
	if look.up(lab) == 'c':
		s_cells += 1
	if look.down(lab) == 'c':
		s_cells += 1
	if look.left(lab) == 'c':
		s_cells +=1
	if look.right(lab) == 'c':
		s_cells += 1

	return s_cells


def fillLab():
	global rand_wall
	test = (walls[int(random.random()*len(walls))-1])
	rand_wall = Point(test[0], test[1])  # Pick a random wall
	selectedWall = checkWalls() # Check which wall was chosen at random
	
	if selectedWall != 'Invalid':
		s_cells = surroundingCells(rand_wall)	
		if (s_cells < 2):
			# Denote the new path	
			lab[rand_wall.x][rand_wall.y] = 'c'

			if (rand_wall.y != labWidth-1) and selectedWall != 'Left':	# Mark right cell as wall
				buildWall('Right')

			if (rand_wall.x != labHeight-1) and selectedWall != 'Top':	# Mark bottom cell as wall
				buildWall('Down')

			if (rand_wall.x != 0) and selectedWall != 'Bottom':	# Mark upper cell as wall
				buildWall('Up')

			if (rand_wall.y != 0) and selectedWall != 'Right':	# Mark left cell as wall
				buildWall('Left')

			for wall in walls:	# Delete random wall from the wall list
				if (wall[0] == rand_wall.x and wall[1] == rand_wall.y):
					walls.remove(wall)
	for wall in walls:
		if (wall[0] == rand_wall.x and wall[1] == rand_wall.y):
			walls.remove(wall)


# Creating starting and ending point
def setExits():
	for i in range(0, labWidth):
		if (lab[1][i] == 'c'):
			lab[0][i] = 'c'
			start.append(0)
			start.append(i)
			break
	for i in range(labWidth-1, 0, -1):
		if (lab[labHeight-2][i] == 'c'):
			lab[labHeight-1][i] = 'c'
			end.append(labHeight-1)
			end.append(i)
			break
	

def labBuilder():
	populateLab()
	setStartingPoint()
	setStartingWalls()

	while (walls):
		fillLab()
	
	swapCells('u', 'w') # Mark the remaining unvisited cells as walls
	setExits()


# Print
def printLab():
	print('\n')
	for x in lab:
		for y in x:
			if y == 'c':
				print(" ", end = "")
			elif y == 'w':
				print("█", end = "")
			elif y == 'p':
				print("▒", end = "")
			elif y > 0:
				print("·", end = "")
			else:
				print("", end = " ")
		print()	


# Animated print
def animatedPrint():
	time.sleep(0.1)
	os.system('cls')
	printLab()


# Search for the path start-end
def findPath(step):
	for i in range(len(lab)):
		for j in range(len(lab[i])):
			if lab[i][j] == step:
				if lab[i-1][j] == 0:
					lab[i-1][j] = step + 1
				if lab[i][j-1] == 0:
					lab[i][j-1] = step + 1
				if lab[i+1][j] == 0:
					lab[i+1][j] = step + 1
				if lab[i][j+1] == 0 :
					lab[i][j+1] = step + 1


# Highlight the shortest route
def tracePath(step):
	i, j = end
	step = lab[i][j]
	while step > 0:
		look = Point (i, j)
		lab[i][j] = 'p'
		if look.up(lab) == step-1:
			i, j = i-1, j
		elif look.left(lab) == step-1:
			i, j = i, j-1
		elif look.down(lab) == step-1:
			i, j = i+1, j
		elif look.right(lab) == step-1:
			i, j = i, j+1
		step -= 1
		animatedPrint()

def labSolver():
	swapCells('c', 0) # Change cells for the sake of tracing path
	lab[start[0]][start[1]] = 1

	while lab[end[0]][end[1]] == 0: # Finding possible paths to the end
		global currentStep
		currentStep += 1
		findPath(currentStep)
		animatedPrint()
	
	tracePath(currentStep) # Backtracking the shortest path


# Swapping data 
def swapCells(x, y):
	for i in range(0, labHeight):
		for j in range(0, labWidth):
			if (lab[i][j] == x):
				lab[i][j] = y		



## Main code
wall = 'w'
cell = 'c'
unvisited = 'u'
currentStep = 0
labHeight = int(input("Rzędy: "))
labWidth = int(input("Kolumny: "))
lab = []
walls = []
start = []
end = []
print("\n")

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def up(self, array):
		return array[self.x - 1][self.y]
	def down(self, array):
		return array[self.x + 1][self.y]
	def left(self, array):
		return array[self.x][self.y - 1]
	def right(self, array):
		return array[self.x][self.y + 1]

labBuilder()

printLab()

labSolver()

input()