# -*- coding: utf-8 -*-

def ciclo_while():
    i = 0
    while i < 10:
        print(i)
        i += 1

def infinite_loop():
    j = 0
    while j >= 0:
        print(j)
        j += 1

def run():
    pregunta = int(raw_input('Elige una funcion [1] ciclo_while() o [2] infinite_loop() Se cierra con CTRL + C: '))

    if pregunta == 1:
        ciclo_while()

    if pregunta == 2:
        infinite_loop()

    if (pregunta != 1) and (pregunta != 2):
        print("No has seleccionado una opcion valida") 

if __name__ == '__main__':
    run()
