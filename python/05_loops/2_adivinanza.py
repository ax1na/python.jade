
#jade rojas
#7-4-25

adivinanza =0
intentos = 0

while adivinanza != 6 and intentos > 5:
    adivinanza  = int(input("adivina el numero:"))
    intentos +=1
if adivinanza !=6:
    print("te quedaste sin intrentos")

else: 
    print("adivinaste")
