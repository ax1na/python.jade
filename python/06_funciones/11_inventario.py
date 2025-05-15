# jad erojas
# 26-04-2025

def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
def eliminar_producto(inventario, producto):
    if producto in inventario:
        del inventario[producto]
    else:
        print(f"El producto '{producto}' no existe en el inventario.")
def actualizar_cantidad(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] = cantidad
    else:
        print(f"El producto '{producto}' no existe en el inventario.")

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario actual:")
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad}")

inventario = {}

agregar_producto(inventario, "Manzanas", 10)
agregar_producto(inventario, "Naranjas", 5)

mostrar_inventario(inventario)

actualizar_cantidad(inventario, "Manzanas", 15)

eliminar_producto(inventario, "Naranjas")

mostrar_inventario(inventario)