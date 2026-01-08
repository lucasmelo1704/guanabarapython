#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Ask the user to enter a number
number = int(input('Enter a number: '))

# Get the rest of the division by 2
result = number % 2

# Check if the result is equal to 1
if result == 1:
    print('This number is even')
else:
    print('This number is odd')