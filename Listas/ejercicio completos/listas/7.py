'''llenar una lista de tamaño aleatorio entre (10, 25) elementos. llene la lista con numeros aleatorios y encuentre
la mediana de los numeros de la lista'''
import random

vec = []
ran = random.randint(10, 25)

for i in range(ran):
    vec.append(round(random.random() * 100))
print("la lista sin ordenar es:", vec)

vec.sort()
print("la lista ordenada es:", vec)

mitad = int(ran // 2)
if ran % 2 == 0:
    mediana = (vec[mitad - 1] + vec[mitad])//2
else:
    mediana = vec[mitad]
print("la longitud del vector es: ", ran)
print("la mediana del vector es: ", mediana)