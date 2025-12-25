#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

grade_one = float(input('Enter the first grade: '))
grade_two = float(input('Enter the second grade: '))


arithmetic_mean = (grade_one + grade_two) / 2

print('The average of the grades {:.2f} and {:.2f} is {:.2f}.'.format(grade_one, grade_two, arithmetic_mean))