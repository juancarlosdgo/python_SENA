n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
n3 = int(input("ingrese el tercer numero: "))

menor = min(n1, n2, n3)
mayor = max(n1, n2, n3)
medio = (n1 + n2 + n3) - menor - mayor

if n1 != n2:
    print('el numero medio es: ', medio)
elif n2 != n3:
    print('el numero medio es: ', medio)
else:
    print('el numero no existe ' )