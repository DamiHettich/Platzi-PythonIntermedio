

def regular_loop():
    """Create a function that gives the squares of the first 100 numbers that are not divisible by 3
    """
    squares = []
    for i in range(1,101):
        if i%3!=0:
            squares.append(i**2)
    print(squares)

def list_comprehension():
    squares = [i**2 for i in range(1,101) if i%3!=0]
    print(squares)

if __name__ == "__main__":
    regular_loop()
    list_comprehension()


# THE GENERAL STRUCTURE IS:
# [element_transf for element in iterable if condition]