'''llenar una lista de tamaño aleatorio entre 10 y 25 elementos. llene la lista co numeros laeatorios, solicit al usuario un numero
para buscar en la lista . diga cuantas veces està y en que posicion esta y si  o esta entonces agreguelo al fianl de la lista'''
import random

vector = []
lista = random.randint(10, 25)
cont = 0
posicion = ""

for i in range(lista):
    vector.append(round(random.random()*100))
print(vector)
numero = int(input("ingrese un numero"))

for i in range(lista):
    if numero == vector:
        posicion += str[i] + " "
        cont += 1
if cont == 0:
    vector.append(numero)
    print("el numero se agrgo al final de la lista")
    print(vector)

