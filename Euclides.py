"""Retorna el máximo común divisor de a y b usando el algoritmo de Euclides"""


def extended(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        r, x, y = extended(b, a % b)
        print("y", y)
        print("x", x)
        print("r", r)
        print("-"*80)
        return (r, y, x - (a // b) * y)


def mcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        c = a//b
        print(a, " = ", b, "(", c, ")", "+", r)
        r = a - b*c
        return mcd(b, r)


def mcm(a, b):
    return a*b / mcd(a, b)


a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
print("-"*80)
print("El maximo comun divisor entre ", a, "y", b, "es: ", mcd(a, b))
print(extended(a, b))
print("El minimo comun multiplo entre ", a, "y", b, "es:", mcm(a, b))
