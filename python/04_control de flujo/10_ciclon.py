# jade rojas
# 26-04-2025

velocidad_viento = int(input("Ingrese la velocidad del viento en km/h: "))

if velocidad_viento < 119:
    print("No es un ciclón, es una tormenta tropical.")
elif 119 <= velocidad_viento <= 153:
    print("Es un ciclón categoría 1.")
elif 154 <= velocidad_viento <= 177:
    print("Es un ciclón categoría 2.")
elif 178 <= velocidad_viento <= 208:
    print("Es un ciclón categoría 3.")
elif 209 <= velocidad_viento <= 251:
    print("Es un ciclón categoría 4.")
else:
    print("Es un ciclón categoría 5.")