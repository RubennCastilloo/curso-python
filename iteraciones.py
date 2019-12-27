# -*- coding: utf-8 -*-

def iterar_num():
    for i in range(30):
        if i % 3 == 0:
            print(i)
        elif i == 22:
            break
def iterar_elevar_cuadrado():
    for i in range(30):
        if i % 3 == 0:
            print(i**2)
        elif i == 22:
            break

def letter():
    r = 'ferrocarril'
    for letter in r:
        print(letter)

def run():
    pregunta = int(raw_input('Elige una funcion [1] iterar_num() o [2] iterar_elevar_cuadrado() o [3] Para ciclo for con letras: '))

    if pregunta == 1:
        iterar_num()

    if pregunta == 2:
        iterar_elevar_cuadrado()
    
    if pregunta == 3:
        letter()

    if (pregunta != 1) and (pregunta != 2) and (pregunta != 3):
        print("No has seleccionado una opcion valida") 

if __name__ == '__main__':
    run()
