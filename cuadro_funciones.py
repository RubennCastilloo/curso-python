# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    ruben = turtle.Turtle()

    make_square(ruben)

    turtle.mainloop()

def make_square(ruben):
    length = int(raw_input('Tamaño de cuadrado: '))

    for i in range(4):
        make_line_and_turn(ruben, length)

def make_line_and_turn(ruben, length):
    ruben.forward(length)
    ruben.left(90)


if __name__ == '__main__':
    main()
