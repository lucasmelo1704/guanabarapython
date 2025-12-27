#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperature = float(input('Enter a temperature in ºC: '))
fahrenheit = (temperature * 1.8) + 32

print("The temperature of {}ºC is {}ºF".format(temperature, fahrenheit))
