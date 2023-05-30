# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


numeros = [1,2,3,4,5]
print('numeros[0]:', numeros[0])
print('numeros[-1]:', numeros[-1])
numeros[0] = 10
print('numeros:', numeros)

letras = ['a','b','c','d']
print('letras;',letras)
letras[2]=54
print('letras:',letras)

contador = 0
while contador < 10 :
    if contador !=9:
      print(contador, end='-')
    else:
     print (contador, end='')
    contador += 1
print('\n======================================')

for i in range(10) :
      print ( i )
print('\n======================================')

for item in [ 1,45,78, ' a ' , [ 3,5 ] ] :
      print ( item )
print('\n======================================')

for letra in ' minha string ' :
     print ( letra )
print('\n======================================')
