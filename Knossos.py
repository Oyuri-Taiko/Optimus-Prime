import numpy as np

labRow = int(input("Rzędy: "))
labColumn = int(input("Kolumny: "))
lab = np.ones((labRow, labColumn), dtype=int)
print("\n")

lab[1:-1,1:-1] = 0
  
for x in lab:
  for y in x:
    if y == 1:
      print("X", end = "")
    else:
      print(" ", end ="")
  print()
input()