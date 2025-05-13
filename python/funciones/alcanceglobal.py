#jade rojas
#16-4-24

def sumar (x, y):
    respuesta = x = y

print(sumar(4,2))

#global

respuesta = 0

def sumar (x, y):
    global respuesta
    respuesta = x + y
    return respuesta
print(sumar(2,1))
