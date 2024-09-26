rows = int(input("Number of rows"))


for n in range(0,rows):
    for i in range(0, rows - n - 1):
        print (" ", end="")
    for j in range(0, n + 1):
        print("* ", end="")
    print()

for n in range(0, rows - 1):
    for j in range(0, n + 1):
        print(" ", end="")
    for i in range(0, rows - n - 1):
        print("* ", end="")
    print()