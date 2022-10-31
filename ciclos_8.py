'''Algoritmo para hallar el m.c.d de dos números m y n por el algoritmo de Euclides.'''

n1 = int(input("ingrese un numero; "))
n2 = int(input("ingrese un numero: "))
re = n1 % n2

while True:
    if re == 0:
        print(n2)
    else:
        n1 = n2
        n2 = re
