'''llene una lista con la serie de fibonacci, la cantidad de elementos de la lista. la debe igresar le usuario, minimo debe tener 
5 elementos y maximo 20'''
import random

vector = []
au = True
a = 0
b = 1
c = 1

while au:
    rango = int(input("ingrese un numero"))
    if range >= 5 and range <= 20:
        au = False
    else:
        print("el numero no se encuentra en el rango")

for i in range(rango):
    c = a + b
    a = b 
    b = c
    vector.append(c)
print("la lista es ", vector)