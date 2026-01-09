#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

opposite = float(input('Enter the length of the opposite side: '))
adjacent = float(input('Enter the length of the adjacent side: '))

hypotenuse = ((opposite ** 2) + (adjacent ** 2)) ** 0.5

print('Right triangle: opposite side = {}, adjacent side = {} → hypotenuse = {:.2f}'.format(opposite, adjacent, hypotenuse))