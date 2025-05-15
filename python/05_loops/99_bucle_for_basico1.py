# Básico: imprime todos los números enteros del 0 al 100.

def basic_print(x: int):
    i = 1
    for i in range(x):
        print(i + 1)

print(basic_print(100))

# Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500

def multiples_of_2(x: int):
    for i in range(2, x + 1):
        if i % 2 == 0:
            print(i)

print(multiples_of_2(500))


# Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”

def vanilla_ice_counter(x: int):
    for i in range(1, x + 1):
        if i % 5 == 0 and i % 10 == 0:
            print("baby")
        elif i % 5 == 0:
            print("ice ice")
        else:
            print(i)

print(vanilla_ice_counter(100))

# Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).

def large_number_wow(x: int):
    sum = 0
    for i in range(0, x + 1):
        if i % 2 == 0:
            sum += i
    return sum

print(large_number_wow(500000))

# Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.

def reverse_3_counter(x: int, y: int, z: int):
    for i in range(x, y - 1, -3):
        print(i)

print(reverse_3_counter(2024, 1, 3))

# Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).

def dynamic_counter(x: int, y: int, z: int):
    for i in range(x, y + 1):
        if i % z == 0:
            print(i)

    
print(dynamic_counter(3, 10, 2))