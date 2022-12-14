'''Calcular el máximo de números positivos introducidos por teclado,'''
mayor = 0
menor = 0
 
while True:
    num = input('ingrese un número: ')
    if num == 'hecho' : break
    try:
        num = int(num)
    except:
        print("Valor inválido")
        continue
    if num > menor and num < mayor:
        menor = num
    if num > mayor :
        mayor = num
 
print('Máximo es', mayor)
print('Mínimo es', menor)