import random
tam=random.randint(10,25)
vector=[]
for i in range(tam):
    vector.append(round(random.random()*100))
print(vector)
print(vector.__len__())
cont=0
cant=0
var1=0
var2=0

for i in range(tam):
    if vector[i]%2==0:
        """print(vector[i] ,'es par')"""
        cont+=1
        var1+=vector[i]
    else:
        """print(vector[i] ,'es impar')"""
        cant+=1
        var2+=vector[i]
        
"""print('la cantidad total de pares fue ',cont, '\nla cantidad de impares fue ',cant)
print('la suma de los pares es ',var1,'\nla suma de los impares es ',var2)
print('el promedio de pares ',var1//cont, '\nel promedio de los impares: ',var2//cant)
print('la suma de los pares ',)"""
print('la suma de los pares es ',var1)
print('el promedio de los impares es ',var2//cant)