#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

name = str(input('Enter your name: ')).strip()

print('Hello {}! How are you?'.format(name))