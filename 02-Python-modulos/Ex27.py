#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Ask the user for the full name
full_name = input("Enter your full name: ").strip()

# Get first and last name
first_name = full_name.split()[0].capitalize()
last_name = full_name.split()[-1].capitalize()

# Show results
print(
    "Full Name: {}\nFirst Name: {}\nLast Name: {}".format(
        full_name, first_name, last_name
    )
)