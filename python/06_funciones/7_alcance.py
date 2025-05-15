# jade rojas
# 26-04-2025

# Variable global
mensaje = "Hola desde el ámbito global"

def mostrar_mensaje():
    # Variable local
    mensaje = "Hola desde mi casa"
    print(mensaje)  # Imprime el mensaje local

mostrar_mensaje()
print(mensaje)  # Imprime el mensaje global