# lab generator -- Randomized Prim Algorithm

## Imports
import random
import time


## Functions

# Creating starting and ending point

def setEntrance():
	for i in range(0, labWidth):
		if (lab[1][i] == 'c'):
			lab[0][i] = 'c'
			start.append(i)
		
			break

def setExit():
	for i in range(labWidth-1, 0, -1):
		if (lab[labHeight-2][i] == 'c'):
			lab[labHeight-1][i] = 'c'
			end.append(i)
			break

## Prints

def printLab():
	for x in lab:
		for y in x:
			if y == 'c':
				print(" ", end = " ")
			else:
				print("X", end = " ")
		print()	

#Zwykły nie działa normalnie

def printSolvedLab(): 
	for i in range(len(lab)):
		for j in range(len(lab[i])):
			print(str(lab[i][j]).ljust(2),end=' ')
		print()

# Printing the shortest path
def ariadna():
	for x in lab:
		for y in x:
			if isinstance(y, int):
				print(" ", end = " ")
			elif y == 'w':
				print("X", end = " ")
			else:
				print("|", end = " ")
		print()	
##

		
# Finding the way to the end

def tezeusz(k):
	for i in range(len(lab)):
		for j in range(len(lab[i])):
			if lab[i][j] == k:
				if lab[i-1][j] == 0:
					lab[i-1][j] = k + 1
				if lab[i][j-1] == 0:
					lab[i][j-1] = k + 1
				if lab[i+1][j] == 0:
					lab[i+1][j] = k + 1
				if lab[i][j+1] == 0 :
					lab[i][j+1] = k + 1

# Swapping data 
def rubble(x, y):
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
k = 0
labHeight = int(input("Rzędy: "))
labWidth = int(input("Kolumny: "))
lab = []
start = [0]
end = [labHeight-1]
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
if (starting_labHeight == labHeight-1):
	starting_labHeight -= 1
if (starting_labWidth == 0):
	starting_labWidth += 1
if (starting_labWidth == labWidth-1):
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
	# Pick a random wall
	rand_wall = walls[int(random.random()*len(walls))-1] # rand_wall to lista [x,y] , walls to lista list [ [x,y], [x,y], ...] || rand_wall == [9,3] || rand_wall[0] = 9, rand_wall[1] = 3

	# Check if it is a left wall
	if (rand_wall[1] != 0):
		if (lab[rand_wall[0]][rand_wall[1]-1] == 'u' and lab[rand_wall[0]][rand_wall[1]+1] == 'c'):
			# Find the number of surrounding cells
			s_cells = surroundingCells(rand_wall)

			if (s_cells < 2):
				# Denote the new path
				lab[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (lab[rand_wall[0]-1][rand_wall[1]] != 'c'):
						lab[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])


				# Bottom cell
				if (rand_wall[0] != labHeight-1):
					if (lab[rand_wall[0]+1][rand_wall[1]] != 'c'):
						lab[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):	
					if (lab[rand_wall[0]][rand_wall[1]-1] != 'c'):
						lab[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
			

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check if it is an upper wall
	if (rand_wall[0] != 0):
		if (lab[rand_wall[0]-1][rand_wall[1]] == 'u' and lab[rand_wall[0]+1][rand_wall[1]] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				lab[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (lab[rand_wall[0]-1][rand_wall[1]] != 'c'):
						lab[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):
					if (lab[rand_wall[0]][rand_wall[1]-1] != 'c'):
						lab[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

				# Rightmost cell
				if (rand_wall[1] != labWidth-1):
					if (lab[rand_wall[0]][rand_wall[1]+1] != 'c'):
						lab[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check the bottom wall
	if (rand_wall[0] != labHeight-1):
		if (lab[rand_wall[0]+1][rand_wall[1]] == 'u' and lab[rand_wall[0]-1][rand_wall[1]] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				lab[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				if (rand_wall[0] != labHeight-1):
					if (lab[rand_wall[0]+1][rand_wall[1]] != 'c'):
						lab[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (lab[rand_wall[0]][rand_wall[1]-1] != 'c'):
						lab[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != labWidth-1):
					if (lab[rand_wall[0]][rand_wall[1]+1] != 'c'):
						lab[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)


			continue

	# Check the right wall
	if (rand_wall[1] != labWidth-1):
		if (lab[rand_wall[0]][rand_wall[1]+1] == 'u' and lab[rand_wall[0]][rand_wall[1]-1] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				lab[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				if (rand_wall[1] != labWidth-1):
					if (lab[rand_wall[0]][rand_wall[1]+1] != 'c'):
						lab[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != labHeight-1):
					if (lab[rand_wall[0]+1][rand_wall[1]] != 'c'):
						lab[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):	
					if (lab[rand_wall[0]-1][rand_wall[1]] != 'c'):
						lab[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Delete the wall from the list anyway
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
	


# Mark the remaining unvisited cells as walls
rubble('u', 'w')


# Set entrance and exit
setEntrance()
setExit()

# Print final lab
printLab()

input("\nCzas przez niego przejść \n")
print("Punkt początkowy to:", start)
print("Punkt końcowy to:", end, "\n")

rubble('c', 0)
lab[start[0]][start[1]] = 1

while lab[end[0]][end[1]] == 0:
    k += 1
    tezeusz(k)


i, j = end
k = lab[i][j]
while k > 1:
	if lab[i - 1][j] == k-1:
		i, j = i-1, j
		lab[i][j] = 'p'
		k-=1
	elif lab[i][j - 1] == k-1:
		i, j = i, j-1
		lab[i][j] = 'p'
		k-=1
	elif lab[i + 1][j] == k-1:
		i, j = i+1, j
		lab[i][j] = 'p'
		k-=1
	elif lab[i][j + 1] == k-1:
		i, j = i, j+1
		lab[i][j] = 'p'
		k -= 1	

lab[end[0]][end[1]] = 'p'
print("\n")
rubble('p', '|')
ariadna()

input()