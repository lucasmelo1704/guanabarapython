#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = int(input('Enter a angule here: '))
radian = radians(angulo)
sine = sin(radian)
cosine = cos(radian)
tangent = tan(radian)

print('The sine is {:.2f}\nThe cosine is {:.2f}\nThe tangent is {:.2f}'.format(sine, cosine, tangent))