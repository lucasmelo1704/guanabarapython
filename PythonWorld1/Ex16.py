#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

number = float(input("Type a number: "))
number_trunc = trunc(number)

print("The number as integer is {}".format(number_trunc))   