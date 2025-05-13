# jade rojas
# 09-04-2025

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("="*65)
print(" "*10, "⭐🎩 Bienvenido al el Sombrero Seleccionador 🎩⭐", " "*10)
print("="*65)
print("\nP1) ¿Te gusta más el amanecer o el atardecer?")
print("1. Amanecer")
print("2. Atardecer")

respuesta_1 = int(input("\nElige 1 o 2: "))

while respuesta_1 != 1 and respuesta_1 != 2:
    print("Entrada incorrecta. Por favor, elige 1 o 2.")
    respuesta_1 = int(input("Elige 1 o 2: "))
else: 
    if respuesta_1 == 1:
        gryffindor += 1
        ravenclaw += 1
    elif respuesta_1 == 2:
        hufflepuff += 1
        slytherin += 1

print("\n","-"*65)
print("\nP2) Cuando muera, quiero que la gente me recuerde como:")
print("1. El bueno")
print("2. El grandioso")
print("3. El sabio")
print("4. El valiente")

respuesta_2 = int(input("\nElige 1, 2, 3 o 4: "))

while respuesta_2 != 1 and respuesta_2 != 2 and respuesta_2 != 3 and respuesta_2 != 4:
    print("Entrada incorrecta. Por favor, elige 1, 2, 3 O 4")
    respuesta_2 = int(input("Elige 1, 2, 3 o 4: "))
else: 
    if respuesta_2 == 1:
        hufflepuff += 2
    elif respuesta_2 == 2:
        slytherin += 2
    elif respuesta_2 == 3:
        ravenclaw += 2
    elif respuesta_2 == 4:
        gryffindor += 2

print("\n","-"*65)
print("\nP3) ¿Qué tipo de instrumento complace más a tu oído?")
print("1. El violín")
print("2. La trompeta")
print("3. El piano")
print("4. El tambor")

respuesta_3 = int(input("\nElige 1, 2, 3 o 4: "))

while respuesta_3 != 1 and respuesta_3 != 2 and respuesta_3 != 3 and respuesta_3 != 4:
    print("Entrada incorrecta. Por favor, elige 1, 2, 3 O 4")
    respuesta_3 = int(input("Elige 1, 2, 3 o 4: "))
else: 
    if respuesta_3 == 1:
        slytherin += 4
    elif respuesta_3 == 2:
        hufflepuff += 4
    elif respuesta_3 == 3:
        ravenclaw += 4
    elif respuesta_3 == 4:
        gryffindor += 4

puntos = {
    "Gryffindor": gryffindor,
    "Ravenclaw": ravenclaw,
    "Hufflepuff": hufflepuff,
    "Slytherin": slytherin
}

casa_ganadora = max(puntos, key=puntos.get)
print("\n","-"*65)

if casa_ganadora == 'Gryffindor':
    print(f"\nEl Sombrero Seleccionador te ha asignado a: Gryffindor 🦁")
elif casa_ganadora == "Ravenclaw":
    print(f"\nEl Sombrero Seleccionador te ha asignado a: Ravenclaw 🐦‍⬛")
elif casa_ganadora == "Hufflepuff":
    print(f"\nEl Sombrero Seleccionador te ha asignado a: Hufflepuff 🦡")
elif casa_ganadora == "Slytherin":
    print(f"\nEl Sombrero Seleccionador te ha asignado a: Slytherin 🐍")

print("\n","-"*65)