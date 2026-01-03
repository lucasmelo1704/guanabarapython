#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# Ask the user for their full name
full_name = input("What is your full name? ")

# Convert the name to uppercase
full_name_upper = full_name.upper()

# Check if the name contains 'SILVA'
has_silva = "SILVA" in full_name_upper

# Print the result
print(has_silva)