#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Ask the user to enter a year
year = int(input('Enter a year: '))

# Check if the year is divisible by 4
if year % 4 == 0:
    
    # Check if the year is divisible by 100
    if year % 100 == 0:
        
        # Check if the year is also divisible by 400
        if year % 400 == 0:
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    
    # If it is divisible by 4 but not by 100
    else:
        print("It is a leap year.")

# If the year is not divisible by 4
else:
    print("It is not a leap year.")
