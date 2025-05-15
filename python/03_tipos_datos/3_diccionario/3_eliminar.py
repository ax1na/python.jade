#jade rojas
# 22-04-2025

# Eliminar elementos de un diccionario

diccionario = {'nombre': "Alonso", 'edad': 17, 'ciudad': "Santiago"}
print(diccionario) # {'nombre': 'Alonso', 'edad': 17, 'ciudad': 'Santiago'}
print(type(diccionario)) # <class 'dict'>

# Eliminar un elemento del diccionario
del diccionario['nombre']
print(diccionario) # {'edad': 17, 'ciudad': 'Santiago'}
print(type(diccionario)) # <class 'dict'>
print(diccionario['nombre']) # KeyError: 'nombre'