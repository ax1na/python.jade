#jade rojas
#21-4-25

def auto_servicio(opcion):
    print("\n--- MENÚ ---")
    print("1. 🍔 Hamburguesa")
    print("2. 🍕 Pizza")
    print("3. 🌭 Hot Dog")
    print("4. 🍟 Papas fritas")
    print("5. 🥤 Refresco")
    print("-----------")
    
    if 1 <= opcion <= 5:
        if opcion == 1:
            print("\nHa seleccionado: 🍔 Hamburguesa")
        elif opcion == 2:
            print("\nHa seleccionado: 🍕 Pizza")
        elif opcion == 3:
            print("\nHa seleccionado: 🌭 Hot Dog")
        elif opcion == 4:
            print("\nHa seleccionado: 🍟 Papas fritas")
        elif opcion == 5:
            print("\nHa seleccionado: 🥤 Refresco")
    else:
        print("Error: Seleccione un número válido del menú")

# Solicitar input fuera de la función
opcion = int(input("Seleccione un número del menú: "))
auto_servicio(opcion)

