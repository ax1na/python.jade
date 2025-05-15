#jade rojas 30/04

import random

total = random.randint(1, 6) + random.randint(1, 6)

adivina = int(input("Adivina el numero de los dados (2-12): "))
while adivina != total:
    adivina = int(input("Adivina el numero de los dados (2-12): "))
print("Adivinaste el numero")