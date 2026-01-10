#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

student1 = input("Enter the name of student 1: ")
student2 = input("Enter the name of student 2: ")
student3 = input("Enter the name of student 3: ")
student4 = input("Enter the name of student 4: ")

students = [student1, student2, student3, student4]

shuffle(students)

print("Presentation order:")
print(students)