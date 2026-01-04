#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

# Ask the user for the car speed
speed = float(input('Enter your car speed (km/h): '))

# Calculate the fine amount (only valid if speed is over 80)
fine_amount = (speed - 80) * 7

# Check if the speed is over the limit
if speed > 80:
    print('You were fined R${:.2f}'.format(fine_amount))
else:
    print('You were driving at the correct speed.')