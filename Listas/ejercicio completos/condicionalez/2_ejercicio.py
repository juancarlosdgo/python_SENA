n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
n3 = int(input("ingrese el tercer numero: "))

if n1 == n2 and n2 == n3:
    print("son todos iguales")
elif n1 != n2 and n1 != n3:
    print("ninguno es igual")
else:
    print("solo 2 son iguales")
