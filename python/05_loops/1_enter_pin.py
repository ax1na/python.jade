#jade rojas
#07-04-2025
#me quede dormida

print("banco del 4°B")


pin = int(input("ingresa tu pin:"))

while pin != 1234:
    pin = int(input("pin incorrecto, ingresa tu pin nuevamente:"))

if pin == 1234:
    print("pin aceptado")
    print("bienvenido a tu cuenta")