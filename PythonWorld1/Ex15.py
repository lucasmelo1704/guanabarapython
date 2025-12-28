#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

days = int(input('How many days was it rented? '))
km = float(input('What distance was driven in Km: '))

price_days = days * 60
price_km = km * 0.15
final_price = price_days + price_km

print("The car was rented for {:.0f} days and drove {:.2f}km, resulting in a total of R${:.2f}".format(days, km, final_price))