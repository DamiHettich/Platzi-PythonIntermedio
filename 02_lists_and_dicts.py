def run():
    super_list = [
        {'firstname':'Damian', 'lastname':'Sepulveda'},
        {'firstname':'Felipe', 'lastname':'Ibarra'},
        {'firstname':'Trini', 'lastname':'Gomez'},
        {'firstname':'Sandra', 'lastname':'Munoz'}
    ]

    super_dict = {
        "nats":[1,2,3,4],
        "integers":[-2,-1,0,1,2],
        "floats":[0,1.45,10.45456,61.43268]
    }
    print('\nThis is a loop:')
    for key,value in super_dict.items():
        print(f"Los numeros {key} son por ejemplo: {value}")

    print('\nThis is another loop:')
    for item in super_list:
        fn = item.get('firstname')
        ln = item.get('lastname')
        print(f'{fn} , {ln}')


if __name__ == "__main__":
    run()