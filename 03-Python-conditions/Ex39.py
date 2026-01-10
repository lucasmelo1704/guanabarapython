#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Import the date class to work with dates
from datetime import date

# Get the current year
date = date.today().year

# Ask the user for the birth year
birth_year = int(input('What year were you born? '))

# Calculate the age using the current year
age = date - birth_year

# Show the age, birth year, and current year
print('Who is {} years old was born in {} in the current year of {}'.format(age, birth_year, date))

# Check if the age is exactly 18
if age == 18:
    print('You must enlist immediately.')

# Check if the age is less than 18
elif age < 18:
    years_left = 18 - age
    print('It is not time to enlist yet.')
    print('You need to enlist in {} years.'.format(years_left))

# Check if the age is greater than 18
elif age > 18:
    years_late = age - 18
    print('You are late to enlist.')
    print('You should have enlisted {} years ago.'.format(years_late))