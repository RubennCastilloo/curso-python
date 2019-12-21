# -*- coding: utf-8 -*-

def tipo_cambio(total):
    peso_mex_to_col = 145.97
    return peso_mex_to_col * total

def run():
    print('C A L C U L A D O R A  D I V I S A S  P Y T H O N 3')
    print('')
    print('Convierte de pesos mexicanos a pesos colombianos')
    print('')
    
    total = float(input('Ingresa la cantidad a convertir'))
    result = tipo_cambio(total)
    print('${} pesos mexicanos equivalen a ${} pesos colombianos'.format(total, result))

if __name__ == '__name__':
    run()
