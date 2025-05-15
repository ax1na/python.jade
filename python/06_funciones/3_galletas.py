# jade rojas
# 26-04-2025

import random
def galleta_de_la_fortuna():
    mensajes = [
        "Hoy es un buen día para intentar algo nuevo.",
        "La suerte está de tu lado.",
        "El éxito llega a quienes trabajan duro.",
        "Una sorpresa agradable está en tu futuro.",
        "Confía en tus instintos, te guiarán bien.",
        "Algo maravilloso está por suceder.",
        "La paciencia es la clave del éxito.",
        "Hoy es el día perfecto para empezar de nuevo."
    ]
    return random.choice(mensajes)

if _name_ == "_main_":
    print("Tu galleta de la fortuna dice:")
    print(galleta_de_la_fortuna())