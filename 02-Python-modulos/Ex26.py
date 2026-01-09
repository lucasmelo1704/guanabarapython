#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# Ask the user to enter a phrase
phrase = input("Enter a phrase: ")

# Convert the phrase to lowercase
phrase_lower = phrase.lower()

# Count how many times the letter 'a' appears
count_a = phrase_lower.count('a')

# Find the first position of 'a'
first_position = phrase_lower.find('a')

# Find the last position of 'a'
last_position = phrase_lower.rfind('a')

print("The letter A appears {} times".format(count_a))

print("The first A appears at position {}".format(first_position + 1))

print("The last A appears at position {}".format(last_position + 1))