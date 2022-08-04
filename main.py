def sum(a, b):
    """
        Additionne deux nombres ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    """
    return a+b


try:
    number_1 = int(input('Nombre 1'))
    number_2 = int(input('Nombre 2'))
    print(f'{sum(number_1, number_2)}')
except ValueError:
    print('Merci de saisir un nombre')
