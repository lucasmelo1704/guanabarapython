#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random as rd

user_choice = int(input('Enter a number from 0 to 5: '))

computer_number = rd.randrange(0, 6)

if user_choice == computer_number:
    print('Congratulations, you win')
else:
    print('You lost, the number chosen by the computer was {}'.format(computer_number))