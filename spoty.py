'''El programa mas complicado hasta el momento, toca crear un diccionario intentando recrear el funcionamiento de 
spotify, hay 2 formas de hacerlo:
1. Agregando una cancion y a esa cancion agregar artista, duracion y genero (Que es el caso de este codigo)
2. Agregando un artista y dentro el genero, la cancion y dentro de la cancion otro diccionario en donde vaya como
tal el nombre de la cancion y su respectiva duracion Sin importar el metodo, hay que agregar funciones para que el 
usuario inserte:
La cancion o artista, la info de la cancion o el artista, que pueda buscar un artista, que pueda buscar una cancion,
que pueda eliminar un artista o cancion dependiendo de la forma elegida para hacer, mostrar la cancion mas corta y
mostrar la cancion mas larga
A continuacion, el programa "Spotify"'''

import random

play = {}

def musica(olay):
    cancion = input("ingrese el nombre de la cancion: ")
    play.update({cancion:{}})
    return play

def musicInfo(play):
    cancion = input("ingrese el nombre del autor: ")
    if cancion not in play:
        print("no se encontrò")
        return play
    artista = input("agregar el nombre del artista: ")
    duracion = input("agregar el tiempo de duracion de la cancion: ")
    genero = input("agregar el genero al cual pertenece la cncion: ")
    album = input("agregar el albun al cual pertenece la cancion: ")
    lanzamiento = input("agrega fecha de lanzamiento de la cancion: ")
    
    else:
    play.update({cancion:{"artista":artista, "duracion":duracion, "genero":genero, "albun": album, "lanzamiento":lanzamiento}})
    return play

def buscarMusic(play):
    buscar=input('¿Que cancion desea buscar?: ')
    for i in sorted(play.keys()):
        if buscar==i:
            print(buscar,'ya se encuentra en play list',play[i]['duracion'])
            return None
    print('Error, La el nombre que inreso no se encuentra, ingrese el nombre primero')

def eliminar(play):
    buscar=input('¿Que cancion desde elminiar?: ') #Input
    for i in sorted(play.keys()):
        if buscar==i: 
            del play[i]
            print(,buscar,'Se eliminò correctamente') 
            return None
    print('La cancion no se encuentra en el archivo, ingrese el nombre primero')