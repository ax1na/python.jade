#jade rojas
#2-04-25
#Canción de elefantes que se balanceaban

numero = int(input("¿Cuántos elefantes quieres que se balanceen? "))

for i in range(1, numero + 1):
    if i == 1:
        print(f"{i} elefante se balanceaba sobre la tela de una araña,")
    else:
        print(f"{i} elefantes se balanceaban sobre la tela de una araña,")
    print("como veían que resistía fueron a llamar a otro elefante.")