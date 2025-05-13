#jader ojas
#10-3-25
pistas = ("Puerta Roja",221,"Londres",3.14,"Watson",7,"Moriarty")

print("🔎 ¡Bienvenido, detective Holmes!")
print("📜 Se ha encontrado una serie de pistas misteriosas...")
print("🗝️ Pistas encontradas:", pistas)
#📌 Analisis de pistas
print("/n 🕵️ Analizando las pistas")
#Respuestas
print(pistas[0])
print(pistas[6])
print(len(pistas))
print("Londres"in pistas)
a,b,c,d,e,f,g = pistas
print(a,b,c)
pistas2 = ("Vestido rojo","Cuchillo","22:34")
Nuevas_Pistas = pistas + pistas2
print(Nuevas_Pistas)
print(pistas.index("Watson"))
print(pistas.count(7))

print("/n 🕵️ Felicitaciones, detective. ¡Has resuelto el analisis inicial de las pistas")
print("🔐 Ahora, sigue con las deducciones para resolver el misterio")