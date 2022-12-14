'''2. Determinar si un numero es o no es primo'''

def primo():
    numero = int(input("introduce un numero: "))
    a = 1
    b = 0

    while a <= numero:
        if numero % a == 0:
            b = b + 1
        a = a + 1
    if b == 2:
        print("el numero ingresado es un numero primo")
    else:
        print("el numero ingresado NO es un numero primo")

print(primo())