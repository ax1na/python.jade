adivinanza = 0
intentos = 0

while intentos > 5 and adivinanza != 6:
    print("Bienvenido a la adivinanza")
    intentos += 1
    adivinanza = int(input("Adivina el número entre 1 y 10: "))
    if adivinanza < 6:
        print("Demasiado bajo")
    elif adivinanza > 6:
        print("Demasiado alto")
    else:
        print("¡Correcto!")