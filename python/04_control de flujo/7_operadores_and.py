# jade rojas
# 26-04-2025

# Importamos el módulo random
import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")

# Elegir un elemento aleatorio de una lista
colores = ['rojo', 'azul', 'verde', 'amarillo']
color_aleatorio = random.choice(colores)
print(f"Color aleatorio: {color_aleatorio}")

# Barajar una lista de elementos
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Lista barajada: {numeros}")

# Generar un número flotante aleatorio entre 0 y 1
numero_flotante = random.random()
print(f"Número flotante aleatorio entre 0 y 1: {numero_flotante}")

# Generar un número flotante aleatorio en un rango específico
numero_flotante_rango = random.uniform(1.5, 5.5)
print(f"Número flotante aleatorio entre 1.5 y 5.5: {numero_flotante_rango}")