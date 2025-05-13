#jade  rojas
#03-04-25

altura  = int(input("cusl es tu altura (cm)?"))
#creacion de una variable para solicitar informacion el usuario
creditos = int(input("cuantos creditos tienes?"))
if altura >= 137 and creditos >= 10:
    print("disfruta tu viaje")

elif altura < 137 and creditos >= 10:
    print("no tienes la altura suficiente para subir|")

elif creditos < 10 and altura >= 137:
    print("no tienes suficiente credito")


else:
    print("no tienes la altura ni los creditos que necesarios para subir ")