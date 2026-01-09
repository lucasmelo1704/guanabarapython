#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

number = int(input('Enter a value: '))

double = number * 2
triple = number * 3
square_root = number ** (1/2)

print("The value {} has:\n"
      "Double = {}\n"
      "Triple = {}\n"
      "Square root = {:.2f}".format(number, double, triple, square_root))