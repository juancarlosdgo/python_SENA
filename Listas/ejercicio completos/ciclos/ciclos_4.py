'''Determinar cuales son los múltiplos de 5 comprendidos entre 1 y N.'''


def multiplo():

    numero = int(input("ingresa un numero y averigua si es multiplo de 5."))
    n = 1
    c = 0

    while n <= numero:
        if numero % 5 == 0:
            c += 1
        n += 1
        if c == 1:
            print(numero,  "es multiplo de 5")
        else:
            print(numero, "no es multiplo de 5")
        break

print(multiplo())