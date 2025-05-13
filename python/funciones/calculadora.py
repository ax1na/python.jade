#jade rojas
#16-4-25

def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Error: no se púede dividir entre cero"
    return a / b

def potencia(a, b):
    return a ** b 

print("suma: 5 + 3 = ", sumar(5, 3))
print("resta:  10 - 4 = ", restar(10, 4))
print("multiplicacion: 6 * 7 = ", multiplicar(6, 7))
print("division: 20 / 4 = ", dividir(20, 4))
print("potencia: 2 ^ 3 = ", potencia(2, 3))