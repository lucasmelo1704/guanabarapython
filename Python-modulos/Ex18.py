#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angle = float(input('Enter the angle: '))
rad = radians(angle)

sine = sin(rad)
cosine = cos(rad)
tangent = tan(rad)

print('Sine: {:.2f}'.format(sine))
print('Cosine: {:.2f}'.format(cosine))
print('Tangent: {:.2f}'.format(tangent))