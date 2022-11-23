'''toca crear un diccionario intentando recrear el funcionamiento de 
spotify, hay 2 formas de hacerlo:
1. Agregando una cancion y a esa cancion agregar artista, duracion y genero (Que es el caso de este codigo)
2. Agregando un artista y dentro el genero, la cancion y dentro de la cancion otro diccionario en donde vaya como
tal el nombre de la cancion y su respectiva duracion Sin importar el metodo, hay que agregar funciones para que el 
usuario inserte:
La cancion o artista, la info de la cancion o el artista, que pueda buscar un artista, que pueda buscar una cancion,
que pueda eliminar un artista o cancion dependiendo de la forma elegida para hacer, mostrar la cancion mas corta y
mostrar la cancion mas larga
A continuacion, el programa "Spotify"'''

import os

play = {}

def musica(play):
    cancion = input("ingrese el nombre de la cancion: ")
    play.update({cancion:{}})
    return play

def musicInfo(play):
    cancion = input("ingrese el nombre del autor: ")
    if cancion not in play:
        print("no se encontrò")
        return play
    
    else:
        artista = input("agregar el nombre del artista: ")
        duracion = input("agregar el tiempo de duracion de la cancion: ")
        genero = input("agregar el genero al cual pertenece la cncion: ")
        album = input("agregar el albun al cual pertenece la cancion: ")
        lanzamiento = input("agrega fecha de lanzamiento de la cancion: ")
        play.update({cancion:{"artista":artista, "duracion":duracion, "genero":genero, "albun": album, "lanzamiento":lanzamiento}})
        return play

def buscarMusic(play):
    buscar=input('¿Que cancion desea buscar?: ')
    for i in sorted(play.keys()):
        if buscar==i:
            print(buscar,'ya se encuentra en play list',play[i]['duracion'])
            return None
    print('Error,  el nombre que inreso no se encuentra, ingrese el nombre primero')

def eliminar(play):
    buscar=input('¿Que cancion desde elminiar?: ') #Input
    for i in sorted(play.keys()):
        if buscar==i: 
            del play[i]
            print(buscar,'Se eliminò correctamente') 
            return play

    print('La cancion no se encuentra en el archivo, ingrese el nombre primero')

def mayor (play):
    mayor_ = dict
    mayor_v = 0
    for i in (play.keys):
        minutos = play[i]["duracion"][0]
        minutos += play[i]["duracion"][1]
        segundos = play[i]["duracion"][3]
        segundos += play[i]["duracion"][4]
        segundos = int(segundos) + int(minutos) * 60
        if mayor_v <= segundos:
            mayor_v = segundos
            mayor = i
    print("la cancio mas larga de la lista es la de: ", mayor)

def menor(play):
    menor=dict
    menor_valor=9e99999 
    for i in (play.keys()):
        minutos=play[i]['duracion'][0]
        minutos+=play[i]['duracion'][1] 
        segundos=play[i]['duracion'][3] 
        segundos+=play[i]['duracion'][4] 
        segundos= int(segundos)+int(minutos)*60 
        if menor_valor>=segundos:
            menor_valor=segundos 
            menor=i
    print('La cancion mas corta es',menor)

while True:
    os.system ("cls")
    pedir=int(input('Bienvenido al menu \n Presione 1 para agregar una cancion \n Presione 2 para agregar informacion detallada a una cancion ya agregada \n Presione 3 para buscar un artista \n Preione 4 para buscar una cancion \n Presione 5 para eliminar una cancion \n Presione 6 para mostrar todo lo agregado \n Presione 7 para mostrar la cancion mas larga \n Presione 8 para mostrar la cancion mas corta \n Presione 9 para finalizar el programa: '))
    if pedir==1: 
        (musica(play))
    elif pedir==2: 
        (musicInfo(play))
    elif pedir==3: 
        (buscarMusic(play))
    elif pedir==4:
        (buscarMusic(play))
    elif pedir==5:
        (eliminar(play))
    elif pedir==6:
        print('Todas las canciones con su informacion respectiva agregada son las siguientes:',play) #Imprime el diccionario
    elif pedir==7:
        mayor(play)
    elif pedir==8:
        menor(play)
    elif pedir==9:
        break 
    else:
        print('El numero no es valido')
    os.system('pause')