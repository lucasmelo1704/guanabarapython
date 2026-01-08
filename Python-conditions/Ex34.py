#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# Ask the user to type the payment value
payment = float(input("What is your payment? R$"))

# Check if the payment is greater than 1250.00
if payment > 1250.00:
    # Calculate the new payment with 10% increase
    new_value = payment * 1.10
else:
    # Calculate the new payment with 15% increase
    new_value = payment * 1.15

# Format the final value with two decimal places
formatted_value = '{:.2f}'.format(new_value).replace('.', ',')

# Show the new payment value on the screen
print('Your new payment is R${}'.format(formatted_value))