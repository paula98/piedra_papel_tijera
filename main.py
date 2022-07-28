import random


def maquina():
    machine = random.choice(['piedra', 'papel', 'tijera'])
    return machine


def usuario():
    user = input('piedra, papel o tijera? ')
    return user


def juego():
    machine = maquina()
    user = usuario()
    while machine == user:
        print('La máquina dijo: ', machine)
        print('Empate. Vuelve a intentar.')
        user = usuario()
        machine = maquina()
    if machine == 'piedra' and user == 'papel' or machine == 'tijera' and user \
            == 'piedra' or machine == 'papel' and user == 'tijera':
        print('La máquina dijo: ', machine)
        print('Ganaste')
    else:

        print('La máquina dijo: ', machine)
        print('Perdiste')


juego()
