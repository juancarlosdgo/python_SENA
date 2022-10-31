'''n número de hasta 9 dígitos e imprimirlo en orden contrario'''

n = int(input("ingrese un numero de 9 digitos: "))
c = 0

while n > 0:
    c += 1
    n //= 10
    print("ingresaste el numero: ", c)

    continue

print(input("enter para continuar: "))

r = 0

while n != 0:
    c = n % 10
    r *= 10 + c
    n //= 10
print(r)
