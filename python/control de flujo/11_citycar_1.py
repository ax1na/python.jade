# jade rojas
# 26-04-2025

# Solicitar altura y créditos al usuario
altura = int(input("Ingrese su altura en cm: "))
creditos = int(input("Ingrese la cantidad de créditos que tiene: "))

# Verificar si cumple los requisitos para subir a la atracción
if altura >= 137 and creditos >= 10:
    print("¡Disfruta el viaje!")
elif creditos >= 10:
    print("No eres lo suficientemente alto para viajar.")
elif altura >= 137:
    print("No tiene suficientes créditos.")
else:
    print("No has cumplido ninguno de los requisitos.")