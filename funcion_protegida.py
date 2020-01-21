# -*- coding: utf-8 -*-

def protected(func):
    
    def wrapper(password):

        if password == 'platzi':
            return func()
        else:
            print('Password Incorrecto')

    return wrapper

@protected
def protected_func():
    print('Tu password es correcto.')

if __name__ == "__main__":
    password = str(raw_input('Ingresa tu password: '))


    protected_func(password)