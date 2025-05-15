# jade rojas
# 09-04-2025

print("Bienvenido al conversor de peso en planetas")
planetas = { "mercurio": 0.38, "venus": 0.91, "marte": 0.38, "jupiter": 2.34, "saturno": 1.06, "urano": 0.92 , "neptuno": 1.19 }
peso_terrestre = float(input("Ingrese su peso en kg: "))
for planeta, peso in planetas.items():
    print(f"{planeta.capitalize()}: {peso}")
numero_planeta = int(input("Ingrese el número del planeta (1-7): "))

def conversor_peso(peso_terrestre, numero_planeta):
    while numero_planeta < 1 or numero_planeta > 7:
        print("Número de planeta inválido. Debe estar entre 1 y 7.")
        numero_planeta = int(input("Ingrese el número del planeta (1-7): "))
    else:
        if numero_planeta == 1:
            peso_planeta = peso_terrestre * planetas["mercurio"]
            print(f"Su peso en Mercurio es: {peso_planeta:.2f} kg")
        elif numero_planeta == 2:
            peso_planeta = peso_terrestre * planetas["venus"]
            print(f"Su peso en Venus es: {peso_planeta:.2f} kg")
        elif numero_planeta == 3:
            peso_planeta = peso_terrestre * planetas["marte"]
            print(f"Su peso en Marte es: {peso_planeta:.2f} kg")
        elif numero_planeta == 4:
            peso_planeta = peso_terrestre * planetas["jupiter"]
            print(f"Su peso en Jupiter es: {peso_planeta:.2f} kg")
        elif numero_planeta == 5:
            peso_planeta = peso_terrestre * planetas["saturno"]
            print(f"Su peso en Saturno es: {peso_planeta:.2f} kg")
        elif numero_planeta == 6:
            peso_planeta = peso_terrestre * planetas["urano"]
            print(f"Su peso en Urano es: {peso_planeta:.2f} kg")
        elif numero_planeta == 7:
            peso_planeta = peso_terrestre * planetas["neptuno"]
            print(f"Su peso en Neptuno es: {peso_planeta:.2f} kg")

conversor_peso(peso_terrestre, numero_planeta)