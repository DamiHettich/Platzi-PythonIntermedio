def divisor(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
        num = input('Ingresa un nr: ')
        assert num.isnumeric(), 'Debes ingresar un número'
        assert num>0, 'Debes ingresar un número positivo'
        print(divisor(num))
        


if __name__ == "__main__":
    run()