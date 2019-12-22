# -*- coding: utf-8 -*-

def dolares_pesos(ammount):
    dolar_to_mex = 0.053

    return dolar_to_mex * ammount

def pesos_dolares(ammount):
    mex_to_dolar = 18.94

    return mex_to_dolar * ammount

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos mexicanos a dolares o dolares a pesos mexicanos.')
    print('')

    question = int(raw_input('Elige la moneda a convertir [1] Peso a dolar o [2] Dolar a peso: '))
    if question == 1:
    
        ammount = float(raw_input('Ingresa la cantidad de pesos mexicanos que quieres convertir: '))
    
        result = dolares_pesos(ammount)
        print('')
        print('#### ${} pesos mexicanos son ${} dolares ####'.format(ammount, result))
        print('')

    if question == 2:
        ammount = float(raw_input('Ingresa la cantidad de dolares que queres convertir: '))
    
        result = pesos_dolares(ammount)
        print('')
        print('#### ${} dolares son ${} pesos mexicanos ####'.format(ammount, result))
        print('')
    elif (question != 1) and (question != 2):
        print('No se ha seleccionado un valor valido')

if __name__ == '__main__':
    run()