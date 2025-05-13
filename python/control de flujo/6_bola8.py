#jade rojas 
#31-03-25
#sueño total

import random 

def bola_magica():
    respuestas = [ 
        "si, definitivamente ✅",
        "contoda certeza, que si⭐",
        "sin lugar a dudas🔒",
        "respuesta confusa, intentalo de nuevo😐",
        "preguntalo nuevamente mas tarde⌚",
        "mejor no decirte ahora😬",
        "mis fuentes dicen que no❌",
        "el paronama no es muy favorable☁️",
        "muy dudoso.🤷‍♀️"
    ]

    pregunta = input("pregunta: ")

    respuesta = random.choice(respuestas)

    # print(f"pregunta: {pregunta}")
    print(f"magic 8 ball: {respuesta}")


bola_magica()