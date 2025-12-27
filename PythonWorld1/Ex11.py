#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

width = float(input('Enter a width: '))
height = float(input('Enter a height: '))

area = width * height
paint = area / 2

print('The area is {:.2f} m²'.format(area))
print('It will take {:.2f} L of paint to cover it'.format(paint))