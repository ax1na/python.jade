#Jade rojas
#17-03-25
 
#insertar pósicion 
mi_lista = ["frutilla", "cereza", "guinda", "tuna", "kiwi"]
print(mi_lista[2])

mi_lista.append("arroz cosido")
print(mi_lista)

mi_lista.insert(2, "arroz cosido")
print(mi_lista)

mi_lista[4]="tomate frito"
print(mi_lista)

eliminado = mi_lista.pop(4)
print(mi_lista)

mi_lista.index("guinda")
print(mi_lista)

mi_lista.reverse()
print(mi_lista)
