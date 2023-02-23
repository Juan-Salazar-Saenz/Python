# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Built-in 

ciudad = 'Bogota'
print(ciudad)
print(ciudad[3:]) 

print(ciudad.upper()) #vuelve todo myúscula
print(ciudad.lower()) #vuelve las letras minúsculas
print(ciudad.swapcase())

ciudad = ciudad.swapcase()
print('La variable {} cambió de caso'.format(ciudad))
print(f'La variable {ciudad} cambió')

print('Bogota' == 'bogota')
es_igual = 'Bogota' == 'Bogota'
millon = 10000000

ciudades = ['Bogota','Pereira']
ciudades.append(['Medellin','Cali'])
ciudades.append('Cali')
print(ciudades)
print(ciudades[0])

