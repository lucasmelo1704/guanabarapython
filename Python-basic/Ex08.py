#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

meters = float(input('Enter a value in meters: '))

centimeter = meters * 100
millimeter = meters * 1000

print('The value {:.2f} meters converted to centimeters is {:.2f} and to millimeters is {:.2f}.'.format(meters, centimeter, millimeter))