"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais"""

# Read the first number from the user
first_number = int(input('Enter the first number: '))

# Read the second number from the user
second_number = int(input('Enter the second number: '))

# Check if the first number is greater than the second
if first_number > second_number:
    print('>>>TYPED VALUE: {}<<<'.format(first_number))
    print('The first typed value is greater.')

# Check if the second number is greater than the first
if second_number > first_number:
    print('>>>TYPED VALUE: {}<<<'.format(second_number))
    print('The second typed value is greater.')

# Check if both numbers are equal
if first_number == second_number:
    print('>>>TYPED VALUES: {}<<<'.format(first_number))
    print('The typed values are equal.')