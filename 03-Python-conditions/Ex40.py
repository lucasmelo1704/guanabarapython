"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO"""

# Ask the user to type the first grade and convert it to float
grade1 = float(input("Enter the first grade: "))

# Ask the user to type the second grade and convert it to float
grade2 = float(input("Enter the second grade: "))

# Calculate the average of the two grades
average = (grade1 + grade2) / 2

# Check if the average is less than 5
if average < 5:
    # Show the average with 2 decimal places
    print("Your grade is {:.2f}.".format(average))
    # Show the result
    print("Result: FAILED.")

# Check if the average is less than 7
elif average < 7:
    # Show the average with 2 decimal places
    print("Your grade is {:.2f}.".format(average))
    # Show the result
    print("Result: RECOVERY.")

# If none of the conditions above are true
else:
    # Show the average with 2 decimal places
    print("Your grade is {:.2f}.".format(average))
    # Show the result
    print("Result: APPROVED.")