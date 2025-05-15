#jade rojas 30/04

respuesta = input("¿Ya llegamos?")

while respuesta.lower() != "si":
    respuesta = input("¿Ya llegamos?")
    if respuesta.lower() == "si":
        print("¡Epaaaaaa!")
    else:
        print("No hemos llegado, sigue conduciendo.")