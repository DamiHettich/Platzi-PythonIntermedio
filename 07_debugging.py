def divisor(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input('Ingresa un nr: '))
        print(divisor(num))

    except ValueError:
        print('Debes ingresar un número')


if __name__ == "__main__":
    run() 