print("Ingrese un numero para saber si es perfecto o triangular")
num = int(input())
divisores = []
suma = 0
n = num/2
for x in range(1, num):
    if num % x == 0:
        divisores.append(x)

print("Los divisores de ", num, "son: ", divisores)

for x in divisores:
    suma = suma + x

if suma == num:
    print("El numero cumple con la propiedad y es un numero perfecto")
else:
    print("El numero ingresado no cumple con la propiedad y no es un numero perfecto")
    print()

print("-"*60)

for x in range(0, num):
    suma = suma + x
    if num == suma:
        print("El numero ingresado cumple con la propiedad y es un numero triangular")
        break
    else:
        print("El numero ingresado no cumple con la propiedad y no es un numero triangular")
        break

print("-"*70)

Vct = [0,0]
for x in range (0, num):
    Vct.append(0)

Vct[0] = 0
Vct[1] = 1
for x in range (2,num+1):
	Vct[x]= Vct[x-1]+Vct[x-2]

for x in Vct:
    if num == x:
        print("El numero ingresado pertenece a la serie de fibonacci")

