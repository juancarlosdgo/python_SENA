'''llenar una lista de tamaño aleatorio entre (10, 25) elementos, llene la lista con numeros aleatorios, encuetre la moda de los numeros
de la lista'''
import random

vec = []
vect = []
rango = random.randint(10, 25)
for i in range(rango):
    cont = 0 
    for j in vec:
        if vec[i] == j:
            cont += 1
    if cont != 0:
        vect.append(cont)
    else:
        vect.append(0)
print(vec)
print(vect)

m = 0
p = 0

for i in range (len(vec)):
    if m < vect[i]:
        m = vect[i]
print("el mayor es:", m)
for j in range(len(vect)):
    if m == vect[j]:
        print(" la moda es: ", vect[j])