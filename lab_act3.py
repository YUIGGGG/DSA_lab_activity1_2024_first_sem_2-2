rows = int(input("Number of rows: "))

# Upper part of the diamond
for n in range(rows):
    for i in range(rows - n - 1):
        print(" ", end="")
    for j in range(n + 1):
        print("* ", end="")
    print()

# Lower part of the diamond
for n in range(rows - 1):
    for j in range(n + 1):
        print(" ", end="")
    for i in range(rows - n - 1):
        print("* ", end="")
    print()
