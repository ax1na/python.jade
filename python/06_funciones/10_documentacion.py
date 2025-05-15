# jade rojas
# 26-04-2025

"""
Funciones en Python

Una función es un bloque de código reutilizable que realiza una tarea específica. 
Se define utilizando la palabra clave def seguida del nombre de la función y paréntesis.

Sintaxis básica:
def nombre_funcion(parametros):
    # Cuerpo de la función
    return valor

Ejemplos:
"""

# Ejemplo 1: Función sin parámetros ni retorno
def saludar():
    """Imprime un mensaje de saludo."""
    print("Hola, bienvenido a la clase de Python!")

# Llamada a la función
saludar()

# Ejemplo 2: Función con parámetros
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

# Llamada a la función
resultado = sumar(5, 3)
print(f"La suma es: {resultado}")

# Ejemplo 3: Función con valor por defecto
def saludar_persona(nombre="Alumno"):
    """Saluda a una persona con un nombre dado o un valor por defecto."""
    print(f"Hola, {nombre}!")

# Llamadas a la función
saludar_persona("Alonso")
saludar_persona()

# Ejemplo 4: Función con múltiples retornos
def operaciones_basicas(a, b):
    """Realiza suma, resta, multiplicación y división de dos números."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return suma, resta, multiplicacion, division

# Llamada a la función
suma, resta, multiplicacion, division = operaciones_basicas(10, 2)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")