#Crie um programa que leia dois números e mostre a soma entre eles.

number1 = float(input('Enter a value: '))
number2 = float(input('Enter another value: '))
plus = number1 + number2

print('The sum of the number \033[32m{}\033[m and \033[32m{}\033[m results in the value of \033[32m{}\033[m.'.format(number1, number2, plus))