#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Program to calculate product price with 5% discount')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

product_price = float(input('Enter product price: '))

discount = product_price * 0.05
new_price = product_price - discount

print('The product price with 5% discount is {:.2f}'.format(new_price))