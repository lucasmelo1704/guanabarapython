#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

city = input('What is the name of your city? ').strip()
city_upper = city.upper()

print(city_upper[:5] == 'SANTO')