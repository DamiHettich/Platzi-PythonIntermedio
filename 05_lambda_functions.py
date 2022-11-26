# ANONYMOUS FUNCTIONS:
# lambda argumentos:expresion

# [::-1] entrega la inversa 
def palindrome_function(string):
    return string == string[::-1]
print(palindrome_function('ana'))

# a lambda function returns a function type 
palindrome_lambda = lambda string: string==string[::-1]
print('Then there is a lambda:')
print(palindrome_lambda('perrito'))

##################################################################

#1 FILTER THE DATA IN A LIST USING FILTER
nrs = [1,4,5,6,9,13,19,24]
odd_comprehension = [i for i in nrs if i%2!=0]

# la estructura de filter es (lambda function, iterable) y se debe convertir en lista
odd_filter = list(filter(lambda x:x%2 !=0, nrs))

print(f"Numeros impares usando filter: {odd_filter}")
print(f"Numeros impares según comprehension: {odd_comprehension}")


#2 APPLY A TRANSFORMATION TO ELEMENTS IN A LIST USING MAP
this = [1,2,3,4,5]
squares = list(map(lambda x: x**2, this))
print(squares)

#3 REDUCIR LOS VALORES A UN UNICO VALOR 
this = [1,2,3,4,5]
def product_of_list_using_for(input_list):
    final_product = 1
    for i in input_list:
        final_product = i*final_product
    print(final_product)

from functools import reduce
def product_of_list_using_for(input_list):
    print(reduce(lambda a, b: a*b, input_list))