#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Ask the user for the house price
house_price = float(input("What is the price of the house (R$)? "))

# Ask the user for their monthly salary
salary = float(input("What is your monthly salary (R$)? "))

# Ask how many years the user plans to pay the house
years = int(input("In how many years do you plan to pay it off? "))

# Calculate 30% of the user's salary (maximum allowed installment)
max_installment = salary * 0.30

# Calculate the monthly installment
monthly_payment = house_price / (years * 12)

# Check if the monthly payment fits within 30% of the salary
if monthly_payment <= max_installment:
    print(f"Monthly house payment: R${monthly_payment:.2f}")
    print(f"Maximum allowed installment (30% of salary): R${max_installment:.2f}")
    print("Loan approved: You can afford this house.")
else:
    print(f"Monthly house payment: R${monthly_payment:.2f}")
    print(f"Maximum allowed installment (30% of salary): R${max_installment:.2f}")
    print("Loan denied: You cannot afford this house.")