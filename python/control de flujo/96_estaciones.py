#jade rojas
# 09-04-2025

mes = int(input("Ingrese el mes (1-12): "))

while mes < 1 or mes > 12:
    print("Mes inválido. Debe estar entre 1 y 12.")
    mes = int(input("Ingrese el mes (1-12): "))
else:
    if mes == 1 or mes == 2 or mes == 3:
        print("Invierno")
    elif mes == 4 or mes == 5 or mes == 6:
        print("Primavera")
    elif mes == 7 or mes == 8 or mes == 9:
        print("Verano")
    elif mes == 10 or mes == 11 or mes == 12:
        print("Otoño")