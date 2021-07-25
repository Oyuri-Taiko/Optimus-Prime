import array

labRow = int(input("Rzędy: "))
labColumn = int(input("Kolumny: "))
lab = [[0]*labColumn]*labRow
print("\n")

for x in lab:
  for y in x:
    if y == 0:
      print("X", end = " ")
    else:
      print(" ", end = " ")
  print()
input()