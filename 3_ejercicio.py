num = int(input("ingresa un numero entre el o y el 9999: "))

if num < 0 and num > 9999:
    print("error el numero ingresado no se encuentra en el rango")
else:
    if num < 10:
        print("el numero tine 1 digito")
    elif num < 100 and num > 10:
        print("el numero tine 2 digitos")
    elif num < 1000 and num > 100:
        print("el numero tiene 3 digitos")
    elif num < 10000 and num > 1000:
        print("el numero tiene 4 digitos")
