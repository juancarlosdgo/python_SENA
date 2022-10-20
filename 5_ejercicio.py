dia = input('Introduce un dia: ')
mes = input('Introduce un mes: ')
año = input('Introduce un año: ')
 
if dia == 30 and mes == 4 and mes == 6 and mes == 9 and mes == 11:
    mes = mes + 1
    dia = dia + 1
 
if dia == 31 and mes == 1 and mes == 3 and mes == 5 and mes == 7 and mes == 8 and mes == 10 and mes == 12:
	mes = mes + 1
	dia = dia + 1
 
if dia == 28 and mes == 2:
	mes = mes + 1
	dia = dia + 1
 
if dia == 1 and mes == 13:
	año = año + 1
 
else:
	año = año
 
 
print('El dia siguiente es ', dia  , '/' , mes , '/' , año)