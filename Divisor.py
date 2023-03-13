N = []
op = 1
pares = []
impares = []
residuo0 = []
residuo1 = []
residuo2 = []
residuo3 = []
divisor = int(input("Ingrese el numero"))
while(op ==1):
    n = int(input("Ingresa el digito de la lista \n"))
    N.append(n)
    op = int(input("Si deseas ingresar otro numero digita 1 \n"))
for x in N:
    if x % divisor == 0:
        pares.append(x)
    else:
        impares.append(x)
print("Los numeros pares, cuyo residuo al momento de dividirlos en 2 es 0 son: ")
print("-"*60)
print(pares, "\n")
print("Los numeros impares cuyo residuo al dividirlos en 2 no es 0 son: ")
print("-"*60)
print(impares, "\n")
for x in N:
    if x % divisor == 0:
        residuo0.append(x)
    elif x % divisor == 1:
        residuo1.append(x)
    elif x % divisor == 2:
        residuo2.append(x)
print("Los numeros cuyo residuo al divirlos en 3 es cero son: ")
print("-"*50)
print(residuo0)
print("Los numeros cuyo residuo al divirlos en 3 es uno son: ")
print("-"*50)
print(residuo1)
print("Los numeros cuyo residuo al divirlos en 3 es dos son: ")
print("-"*50)
print(residuo2)