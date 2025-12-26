#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

money = float(input("Enter the amount in BRL: R$ "))

dollar = money / 5.54

print("With R${:.2f}, you can buy ${:.2f}.".format(money, dollar))