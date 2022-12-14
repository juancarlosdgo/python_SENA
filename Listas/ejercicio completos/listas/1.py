'''llenar ua lista de tamaños aleatorio entre (10, 25) elementos. llene la lista con numumeros aleatorios. sume los pares y saque
el promedio de los impares'''

import random
l = []
par = 0
impar = 0
l1 = [random.randint(10, 25)]

for i in range(l1):
    l.append(round(random.random() * 100))
for i in range(l1):
    if l[l]%2 == 0:
        par += l[i]
    else:
        impar += l[i]
