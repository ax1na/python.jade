# jade rojas
# 26-04-2025

# Ejemplo de uso de elif en Python

# Supongamos que queremos clasificar una calificación numérica
calificacion = int(input("Ingresa tu calificación (0-100): "))

if calificacion >= 90:
    print("Excelente, tienes una A.")
elif calificacion >= 80:
    print("Muy bien, tienes una B.")
elif calificacion >= 70:
    print("Bien, tienes una C.")
elif calificacion >= 60:
    print("Pasaste, tienes una D.")
else:
    print("Reprobaste, tienes una F.")

# Nota: elif se usa para evaluar múltiples condiciones de forma secuencial.
# Solo se ejecutará el bloque de código del primer elif que sea verdadero.