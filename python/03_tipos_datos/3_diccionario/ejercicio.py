# jade rojas
# 26-04-2025

# Ejercicio: Contar la frecuencia de palabras en un texto

# Paso 1: Solicitar al usuario que ingrese un texto
texto = input("Ingresa un texto: ")

# Paso 2: Dividir el texto en palabras
palabras = texto.split()

# Paso 3: Crear un diccionario para contar la frecuencia de cada palabra
frecuencia_palabras = {}

# Paso 4: Contar las palabras
for palabra in palabras:
    palabra = palabra.lower()  # Convertir a minúsculas para evitar duplicados por mayúsculas
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Paso 5: Mostrar el resultado
print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")