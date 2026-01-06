#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

# Ask the user for the trip distance
distance = float(input('What is the trip distance? '))

# Check if the distance is 200 km or less
if distance <= 200:
    # Calculate price for short trips
    price = distance * 0.50
else:
    # Calculate price for long trips
    price = distance * 0.45

# Format the price with two decimal places and replace dot with comma
formatted_price = f'{price:.2f}'.replace('.', ',')

# Show the final trip price
print('The trip price is R${}'.format(formatted_price))
