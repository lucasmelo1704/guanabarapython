#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Get three numbers from the user
number_one = float(input('Enter number one: '))
number_two = float(input('Enter number two: '))
number_three = float(input('Enter number three: '))

# Check if the first number is the biggest
if number_one > number_two and number_three:
    print('The value {} is the biggest.'.format(number_one))

# Check if the second number is the biggest
elif number_two > number_one and number_three:
    print('The value {} is the biggest.'.format(number_two))

# If none of the above, the third number is the biggest
else:
    print('The value {} is the biggest.'.format(number_three))