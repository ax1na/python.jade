menu = [
        "1. Hamburguesa con queso",
        "2. Papas fritas",
        "3. Refresco",
        "4. Helado",
        "5. Ensalada",
        "6. Batido",
        "7. Café",
        "8. Agua",
    ]
def obtener_articulo(n: int):
    print(menu[n-1])

def bienvenida():
    print("Bienvenido a Auto Servicio MacDonals")
    print("Por favor, elija una opción del menú:")

    for item in menu:
        print(item)
    
    n = int(input("Ingrese el número del artículo que desea: "))
    while n < 1 or n > len(menu):
        print("Número inválido. Por favor, elija un número del menú.")
        n = int(input("Ingrese el número del artículo que desea: "))
    print("Usted ha elegido el artículo número:", n)
    obtener_articulo(n)

bienvenida()