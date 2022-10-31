'''Cuáles y cuántos son los números primos comprendidos entre 1 y 1000'''

from math import sqrt
contar = 0
for i in range(1, 1000):
    m = int(sqrt(i))
    for j in range(2, m+1):
        if i % j == 0:
            break
    else:
        print(i)
        contar += 1
print("Un total de% d números primos" % contar)