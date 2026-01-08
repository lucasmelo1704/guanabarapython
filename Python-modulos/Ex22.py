'''Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

full_name = input('What is your full name? ').strip()

# Step 1: Uppercase and lowercase versions
name_upper = full_name.upper()
name_lower = full_name.lower()

# Step 2: Count letters without spaces
total_letters = len(full_name.replace(' ', ''))

# Step 3: Count letters in the first name
first_name_letters = len(full_name.split()[0])

# Output
print(full_name)
print(name_upper)   
print(name_lower)
print('Your name has {} letters.'.format(total_letters))
print('Your first name has {} letters.'.format(first_name_letters))
