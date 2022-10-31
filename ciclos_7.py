'''Calcular la operación de un numero X sin utilizar la función pow'''

n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese un numero: "))
resultado = 1

for i in range(1, n2 + 1):
    resultado *= n1
print(resultado)
