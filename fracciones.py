from fractions import Fraction

print("fracciones")

n1 = Fraction(input("introduce un numero fraccionario. ejemplo: 4/2: "))
print("tu numero es: ", n1)

n2 = Fraction(input("introduce otro numero fraccionario. ejemplo: 4/2: "))
print("tu numero es: ", n2)

print("el resultado de la suma es: ", (n1 + n2))
print("el resultado de la resta es: ", (n1 - n2))
print("el resultado de la multiplicacion es: ", (n1 * n2))
print("el resultado de la division es: ", (n1 / n2))