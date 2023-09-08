
def pattern1():
    for i in range(4):
        for j in range(4):
            print('*', end="")
        print()

# pattern1()

def pattern2():
    for i in range(4):
        for j in range(i+1):
            print('*', end="")
        print()

# pattern2()


def pattern3():
    for i in range(4,0,-1):
        for j in range(i):
            print('*', end="")
        print()

# pattern3()

def print_pattern(rows):
    for i in range(rows, 0, -1):
        # Print leading spaces
        for j in range(rows, i, -1):
            print(" ", end="")

        # Print asterisks
        for k in range(1, i + 1):
            if k < i:
                print("* ", end="")
            else:
                print("*", end="")

        # Move to the next line
        print()

    for i in range(2, rows + 1):
        # Print leading spaces
        for j in range(rows, i, -1):
            print(" ", end="")

        # Print asterisks
        for k in range(1, i + 1):
            if k < i:
                print("* ", end="")
            else:
                print("*", end="")

        # Move to the next line
        print()

# Call the function with the number of rows you want
print_pattern(4)

