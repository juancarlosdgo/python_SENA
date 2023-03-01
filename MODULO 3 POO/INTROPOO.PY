class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre 
        self.__documento=documento
        #print('Constructor Activado')        

    def getNombre(self):
        try:
            return self.__nombre, self.__documento
        except:
            return "se ha presentado un error"

    def setNombre(self,nombre,documento):
        try:
            self.__nombre=nombre, self.__documento
        except:
            return "hay un error"
ob=Persona('Maria', 1012444700)
print(ob.getNombre())
ob.setNombre('Ana',32423423422)
print(ob.getNombre()) 
#print(type(ob))

class Aprendiz(Persona):
    def __init__(self,nombre,ficha,documento):
        Persona.__init__(self,nombre,documento)
        self.__nombre=nombre
        self.__ficha=ficha
        self.__documento=documento

    def getFicha(self):
        try:
            return self.__ficha
        except:
            return "ocurrio un error"
    
    def getall_1(self):
        try:
            return self.__nombre, self.__ficha, self.__documento
        except:
            return " ocurrio un error"

app=Aprendiz('Pedro',12345,1012444700)
#print(app.getFicha())
#print(app.getNombre())
print(app.getall_1())

