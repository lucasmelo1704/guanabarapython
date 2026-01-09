#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# Ask the user to enter an integer number
number = int(input('Enter a number: '))

# Show the conversion options to the user
print('Choose one conversion option:')
print('[1] Convert to BINARY')
print('[2] Convert to OCTAL')
print('[3] Convert to HEXADECIMAL')

# Ask the user to choose an option
option = int(input('Which option do you want? '))

# Check if the option is binary
if option == 1:
    print('The value {} in BINARY is: {}'.format(number, bin(number)))

# Check if the option is octal
if option == 2:
    print('The value {} in OCTAL is: {}'.format(number, oct(number)))

# Check if the option is hexadecimal
if option == 3:
    print('The value {} in HEXADECIMAL is: {}'.format(number, hex(number)))

# Show a message if the option is not valid
else:
    print('Enter a valid option')