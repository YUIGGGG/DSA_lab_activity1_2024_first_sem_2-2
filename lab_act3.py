rows = int(input("Number of rows"))


for n in range(0,rows):
    for i in range(0, rows - n - 1):
        print (" ", end="")
    for j in range(0, i + 1):
        print("* ", end="")
    print()