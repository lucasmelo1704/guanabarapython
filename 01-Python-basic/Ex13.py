#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input("Enter your previous salary: "))

increase = salary * 0.15
new_salary = salary + increase

print("Your salary of {:.2f} increased to {:.2f}".format(salary, new_salary))