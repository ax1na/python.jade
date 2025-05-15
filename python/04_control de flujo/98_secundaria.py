# jade rojas
# 09-04-2025

edad = int(input("Ingrese su edad: "))

while edad < 14 or edad > 17:
    print("To Be Determinated")
    edad = int(input("Ingrese su edad (14-17): "))
else:
    if edad == 14:
        print("Estudiante de primer año")
    elif edad == 15:
        print("Estudiante de segundo año")
    elif edad == 16:
        print("Estudiante de tercer año")
    elif edad == 17:
        print("Estudiante de cuarto año")