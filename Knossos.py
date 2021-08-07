import random
import time
import os

## Functions

# Check which random wall was selected

def checkWalls():
	if (rand_wall[1] != 0): # left
		if (lab[rand_wall[0]][rand_wall[1]-1] == 'u' and lab[rand_wall[0]][rand_wall[1]+1] == 'c'):
			return 1

	if (rand_wall[0] != 0): # upper
		if (lab[rand_wall[0]-1][rand_wall[1]] == 'u' and lab[rand_wall[0]+1][rand_wall[1]] == 'c'):
			return 2
		
	if (rand_wall[0] != labHeight-1): # bottom
		if (lab[rand_wall[0]+1][rand_wall[1]] == 'u' and lab[rand_wall[0]-1][rand_wall[1]] == 'c'):
			return 3

	if (rand_wall[1] != labWidth-1): # right
		if (lab[rand_wall[0]][rand_wall[1]+1] == 'u' and lab[rand_wall[0]][rand_wall[1]-1] == 'c'):
			return 4
		
	return 5


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


# Search for the path start-end
def findPath(x):
	for i in range(len(lab)):
		for j in range(len(lab[i])):
			if lab[i][j] == x:
				if lab[i-1][j] == 0:
					lab[i-1][j] = x + 1
				if lab[i][j-1] == 0:
					lab[i][j-1] = x + 1
				if lab[i+1][j] == 0:
					lab[i+1][j] = x + 1
				if lab[i][j+1] == 0 :
					lab[i][j+1] = x + 1


# Highlight the shortest route
def tracePath(x):
	i, j = end
	x = lab[i][j]
	lab[end[0]][end[1]] = 'p'
	printLab()
	while x > 1:
		time.sleep(0.1)
		if lab[i - 1][j] == x-1:
			i, j = i-1, j
		elif lab[i][j - 1] == x-1:
			i, j = i, j-1
		elif lab[i + 1][j] == x-1:
			i, j = i+1, j
		elif lab[i][j + 1] == x-1:
			i, j = i, j+1
		x -= 1
		lab[i][j] = 'p'
		os.system('cls')
		printLab()


# Swapping data 
def swapCells(x, y):
	for i in range(0, labHeight):
		for j in range(0, labWidth):
			if (lab[i][j] == x):
				lab[i][j] = y		


# Find number of surrounding cells
def surroundingCells(rand_wall):
	s_cells = 0
	if (lab[rand_wall[0]-1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (lab[rand_wall[0]+1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (lab[rand_wall[0]][rand_wall[1]-1] == 'c'):
		s_cells +=1
	if (lab[rand_wall[0]][rand_wall[1]+1] == 'c'):
		s_cells += 1

	return s_cells


## Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
currentStep = 0
labHeight = int(input("Rzędy: "))
labWidth = int(input("Kolumny: "))
lab = []
start = []
end = []
print("\n")

# Denote all cells as unvisited
for i in range(0, labHeight):
	line = []
	for j in range(0, labWidth):
		line.append(unvisited)
	lab.append(line)

# Randomize starting point and set it a cell
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

# Mark it as cell and add surrounding walls to the list
lab[starting_labHeight][starting_labWidth] = cell
walls = []
walls.append([starting_labHeight - 1, starting_labWidth]) 
walls.append([starting_labHeight, starting_labWidth - 1])
walls.append([starting_labHeight, starting_labWidth + 1])
walls.append([starting_labHeight + 1, starting_labWidth])

# Denote walls in lab
lab[starting_labHeight-1][starting_labWidth] = 'w'
lab[starting_labHeight][starting_labWidth - 1] = 'w'
lab[starting_labHeight][starting_labWidth + 1] = 'w'
lab[starting_labHeight + 1][starting_labWidth] = 'w'

while (walls):
	rand_wall = walls[int(random.random()*len(walls))-1]  # Pick a random wall
	selectedWall = checkWalls() # Check which wall was chosen at random
	
	if selectedWall !=5:
		s_cells = surroundingCells(rand_wall)	
		if (s_cells < 2):
			# Denote the new path	
			lab[rand_wall[0]][rand_wall[1]] = 'c'

			if (rand_wall[1] != labWidth-1) and selectedWall != 1:	# Mark right cell as wall
				if (lab[rand_wall[0]][rand_wall[1]+1] != 'c'):
					lab[rand_wall[0]][rand_wall[1]+1] = 'w'
				if ([rand_wall[0], rand_wall[1]+1] not in walls):
					walls.append([rand_wall[0], rand_wall[1]+1])

			if (rand_wall[0] != labHeight-1) and selectedWall != 2:	# Mark bottom cell as wall
				if (lab[rand_wall[0]+1][rand_wall[1]] != 'c'):
					lab[rand_wall[0]+1][rand_wall[1]] = 'w'
				if ([rand_wall[0]+1, rand_wall[1]] not in walls):
					walls.append([rand_wall[0]+1, rand_wall[1]])

			if (rand_wall[0] != 0) and selectedWall != 3:	# Mark upper cell as wall
				if (lab[rand_wall[0]-1][rand_wall[1]] != 'c'):
					lab[rand_wall[0]-1][rand_wall[1]] = 'w'
				if ([rand_wall[0]-1, rand_wall[1]] not in walls):
					walls.append([rand_wall[0]-1, rand_wall[1]])

			if (rand_wall[1] != 0) and selectedWall != 4:	# Mark left cell as wall
				if (lab[rand_wall[0]][rand_wall[1]-1] != 'c'):
					lab[rand_wall[0]][rand_wall[1]-1] = 'w'
				if ([rand_wall[0], rand_wall[1]-1] not in walls):
					walls.append([rand_wall[0], rand_wall[1]-1])

			for wall in walls:	# Delete random wall from the wall list
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
	


swapCells('u', 'w') # Mark the remaining unvisited cells as walls
setExits() # Set entrance and exit

printLab()

swapCells('c', 0) # Change cells for the sake of tracing path
lab[start[0]][start[1]] = 1

# Finding possible paths to the end
while lab[end[0]][end[1]] == 0:
	time.sleep(0.1)
	currentStep += 1
	findPath(currentStep)
	os.system('cls')
	printLab()
	
tracePath(currentStep) # Backtracking the shortest path

input()