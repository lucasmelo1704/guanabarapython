#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Read three numbers from the user (lengths of the sides)
side1 = float(input('Enter the first side length: '))
side2 = float(input('Enter the second side length: '))
side3 = float(input('Enter the third side length: '))

# Check if the three sides can form a triangle
# A triangle is possible only if the sum of any two sides
# is greater than the third side
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    # If all conditions are true, it is a triangle
    print('These sides can form a triangle.')
else:
    # If any condition is false, it is not a triangle
    print('These sides cannot form a triangle.')