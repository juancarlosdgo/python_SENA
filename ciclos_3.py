'''Determinar si un número es o no es perfecto.'''

def perfecto():
    numero = int(input('1ingrese un numero: '))
    i= 1
    suma = 0

    while i <= numero:
        if numero % i == 0:
            suma = suma + 1
        i = i + 1
    if suma == numero:
        print("el numero ingresado SI es un numero perfecto")
    else:
        print("el numero ingresado NO es un numero perfecto")

print(perfecto())
