'''llenar una lista de tamaño aleatorio entre (10, 25) elementos, llene la lista con numeros aleatorios. de cada elemnto de la lista diga 
si el elemnto esta por encima del promedio, debajo del promedio o es igual alpromedio de todos los numeros de la lista'''

import random
vec = []
ran = random.randint(10, 25)
sum = 0
prom = 0
cont = 0

for i in range(ran):
    vec.append(round(random.random() * 100))
    sum+= vec[i]
    prom = sum // ran
print("el rango de la lista es: ", ran)
print("los valores de la lsita son: ", vec)
print("el promedio de los valores es: ", prom)

for n in range(ran):
    if n < prom:
        print(n, "es menor al promedio")
    elif n > prom:
        print(n, "es mayor al promedio")
    elif n == prom:
        print(n, "es igual al promedio")