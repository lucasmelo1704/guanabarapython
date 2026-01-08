#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

number = int(input('Enter a number from 0 to 9999: '))

thousands = number // 1000 % 10
hundreds  = number // 100 % 10
tens      = number // 10 % 10
units     = number % 10

print('{} - {} - {} - {}'.format(thousands, hundreds, tens, units))