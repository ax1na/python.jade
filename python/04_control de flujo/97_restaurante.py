# jade rojas
# 09-04-2025

rating = float(input("Ingrese la calificación del restaurante ⭐⭐⭐⭐⭐ (0-5): "))

while rating < 0 or rating > 5:
    print("Calificación inválida. Debe estar entre 0 y 5.")
    rating = float(input("Ingrese la calificación del restaurante ⭐⭐⭐⭐⭐ (0-5): "))
else:
    print(f"Calificación válida: {rating}", "⭐"*(5-int(rating)))
    if rating > 4.5 and rating <= 5:
        print("Extraordinario")
    elif rating > 4 and rating <= 4.5:
        print("Excelente")
    elif rating > 3 and rating <= 4:
        print("Bueno")
    elif rating > 2 and rating <= 3:
        print("Regular")
    else:
        print("Pesimo")