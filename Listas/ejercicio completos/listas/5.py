'''llenar un alista de tamañpo aleatorio entre (10, 25) elemntos. llene la lista con numeros aleatorios encuentre la suma
y el promedio d los numeros de la lista'''
import random

vector = []
sum = 0
prom = 0
ran = random.randint(10, 25)

for i in range(ran):
    vector.append(round(random.random() * 100))
    sum += vector[i]
    prom + sum // ran
print("el rango es: ", ran)
print("los elemtos de la lista son: ", vector)
print("la suma de los elemtos de la  lista es: ", sum)
print("el promedio de los elemtos de la lista son: ", prom)