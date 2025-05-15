# jade rojas
# 16-04-2025


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def potenciar(a, b):
    return a ** b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def calcular(operacion, a, b):
    if operacion == 'suma':
        return sumar(a, b)
    elif operacion == 'resta':
        return restar(a, b)
    elif operacion == 'multiplicacion':
        return multiplicar(a, b)
    elif operacion == 'potencia':
        return potenciar(a, b)
    elif operacion == 'division':
        return dividir(a, b)
    else:
        raise ValueError("Operación no válida.")
    
print(calcular('suma', 5, 3)) 
print(calcular('resta', 5, 3))
p…