'''llenar una lista de tamaño aleatorio entre (10, 25) elementos, llene la lista con numeros aleatorios, muestre cuales
y cuantos son primos'''
import random

vec = []
rango = random.randint(10, 25)
for i in range(rango):
    vec.append(round(random.random() * 100))
print("lista es: ", vec)

for i in vec:
    n = 1
    cont = 0
    while (i <= n):
        if i % n == 0:
            cont += 1
        n += 1
    if not cont > 2 or i <= 1:
        print("el numero", i, "es primo")