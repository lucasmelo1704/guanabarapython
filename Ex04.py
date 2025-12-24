#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

something = input('Type something: ')

print('The primitive type is {}'.format(type(something)))
print('Only spaces? {}'.format(something.isspace()))
print('Is it a number? {}'.format(something.isnumeric()))
print('Is it alphabetic? {}'.format(something.isalpha()))
print('Is it alphanumeric? {}'.format(something.isalnum()))
print('Is it uppercase? {}'.format(something.isupper()))
print('Is it lowercase? {}'.format(something.islower()))
print('Is it capitalized? {}'.format(something.istitle()))