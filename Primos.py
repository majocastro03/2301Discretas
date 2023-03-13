num = int(input(
    "Ingrese un numero para determinar su factorizacion y definir si es primo o compuesto.\n"))
print("-"*90)
n = 1
if num <= 2:
    print("El numero ingresado es menor o igual a 2, por lo que no es primo ni compuesto.")
    print("-"*50)
for i in range(2, num):
    if num % i == 0:
        print("El numero ingresado no cumple con la condicion de ser divisible en si mismo y en 1. Por lo que es un numero compuesto")
        print("-"*100)
        break
    else:
        print("El numero cumple con la condicion por lo que es un numero primo al ser divisible en 1 y en si mismo")
        print("-"*100)
        n = 0
        break


# La factorizacion como producto de primos
factores = []
for i in range(2, num):
    while num % i == 0:
        factores.append(i)
        num /= i
if n == 0:
    factores.append(1)
    factores.append(num)
print("La factorizacion como un producto de primos es: ", factores)
