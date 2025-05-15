#jade rojas
# 26-04-2025

contador = 0
while contador < 10:
    print("Contador:", contador)
    contador += 1
else:
    print("Contador ha alcanzado el límite de 10")
    print("Fin del programa")

contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
    if contador == 4:
        print("Contador ha alcanzado el límite de 4")
        break
    print("Fin del programa")

contador = 0
while contador < 5:
    print("Contador:", contador)
    if contador == 3:
        print("Contador ha alcanzado el límite de 3")
        continue
    contador += 1