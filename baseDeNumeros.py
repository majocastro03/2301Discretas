def bs(num, base):
    if num == 0:
        return residuos
    else:
        c = num//base
        r = num % base
        residuos.append(r)
        bs(c, base)

def invertir_lista(lista):
    for i in range(1, len(lista)+1, 1):
        invertida.append(lista[-i])
    return invertida

a = int(input("Ingrese el numero: \n"))
print("-"*30)
b = int(input("Ingrese la base en la que lo desea: \n"))
print("-"*50)
residuos = []
invertida = []
bs(a, b)
invertir_lista(residuos)

print("La expresion en base", b, "del numero ", a, "es: ",  invertida)
