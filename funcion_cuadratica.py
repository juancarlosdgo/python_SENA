from math import sqrt

a = int(input("digite el coeficiente (cuadratico)"))
b = int(input("digite el coeficiente (lineal)"))
c = int(input("digite un numero"))

x1 = 0
x2 = 0

if ((b**2)-4*a*c) < 0:
    print("solucion con numeros omplejos")
else:
    x1 = (-b+sqrt(b**2 - (4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2 - (4*a*c)))/(2*a)
    print("la solucion de la ecuacion: ")
    print(x1)
    print(x2)
