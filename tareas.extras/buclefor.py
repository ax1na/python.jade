#jade rojas
#4-04-25

for i in range(101):
    print(i)

for i in range(2, 501, 2):
    print(i)

for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

suma = 0 
for i in range(0, 50001, 2):
    suma += i
print("la suma total de los numeros pares del 0 al 500,000 es:", suma)
 
for i in range(2025, 0, -3):
    print(i)

numinicial = 3
numfinal = 10
multiplo = 2

for i in range(numinicial, numfinal, numfinal + 1):
    if i % multiplo == 0:
        print(i)