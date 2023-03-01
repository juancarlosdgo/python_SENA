class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre, self.__documento

    def setNombre(self,nombre):
        self.__nombre=nombre, self.__documento

ob=Persona('Maria', 1012444700)
print(ob.getNombre())
ob.setNombre('Ana', 1012444702)
print(ob.getNombre())
#print(type(ob))

