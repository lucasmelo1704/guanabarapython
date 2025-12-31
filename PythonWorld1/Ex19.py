#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

student1 = input("Enter the name of student 1: ")
student2 = input("Enter the name of student 2: ")
student3 = input("Enter the name of student 3: ")
student4 = input("Enter the name of student 4: ")

students = [student1, student2, student3, student4]

chosen_student = choice(students)

print("The chosen student is:", chosen_student)