'''llenar una lista de tamaño aleatorio entre 10 y 25 elementos
llene la lista con numeros laeatorios. ordenar ese arreglo de menor a mayor (algoritmo de burbuja)'''
import random
vector = []
rango = random.randint(10,25)
inter = True

for i in range(rango):
    vector.append(round(random.random() * 100))
    if rango[i] %2 == 0:
        print()
while inter:
    inter = False
    for i in range(len(vector) - 1):
        if vector[i]>vector[i+1]:
            vector[i],vector[i+1]=vector[i+1],vector[i]
            inter = True