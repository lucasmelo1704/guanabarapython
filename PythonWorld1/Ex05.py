#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

number = int(input('Enter a number to know its predecessor and successor: '))

predecessor = number - 1
successor = number + 1

print('You entered the number \033[32m{}\033[m and its predecessor and successor are \033[32m{}\033[m and \033[32m{}\033[m respectively.'.format(number, predecessor, successor))