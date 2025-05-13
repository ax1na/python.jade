#jade rojas
#28-4-25
#objetivo: pedir un numero al usurario y eviutar errores si escriben letras.
def pedir_numero():
    try:     
        numero = int(input("escribe un numero entero: "))
        print("gracias tu numero es:", numero)
    except ValueError: 
        print("eso no es un numero valido. intenta otrea vez")
        pedir_numero()

pedir_numero()
    
        