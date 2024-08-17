import os
import random

file_path = 'frutas.txt'
fruits = ["maca", "abacaxi", "pera", "laranja", "limao", "abacate", "jabuticaba", "pinha", "tomate", "banana", "morango"]

with open(file_path, 'w') as file:
    while file.tell() < 400 * 1024 * 1024:
        fruit = random.choice(fruits)
        file.write(fruit + '\n')

print(f'Arquivo criado em: {file_path}')


