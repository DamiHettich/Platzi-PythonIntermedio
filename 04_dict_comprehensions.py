from math import sqrt
def first_n_squares_using_regular_loop(n):
    my_dict = {}
    for i in range(1,n+1):
        if i %3!=0:
            my_dict[i] = sqrt(i)
    print(my_dict)

def first_n_squares_using_dict_comprehension(n):
    my_dict = {i: sqrt(i) for i in range(1,n+1) if i%3!=0}
    print('\n' + my_dict)

if __name__ == "__main__":
    n = int(input("Ingresa un número: "))
    first_n_squares_using_regular_loop(n)
    first_n_squares_using_dict_comprehension(n)


# DICT COMPREHENSIONS STRUCTURE:
# {key:value for value in iterable if condition}