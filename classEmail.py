class Email():
    __idcuenta=""
    __dominio="" 
    __tipodedominio="" 
    __contraseña=""
    def __init__(self,idcuenta="",dominio="",tipodedominio="",contraseña=""):
        if ((type(idcuenta)==str)&(type(dominio)==str)&(type(tipodedominio)==str)&(type(contraseña)==str)):
            self.__idcuenta=idcuenta
            self.__dominio=dominio
            self.__tipodedominio=tipodedominio
            self.__contraseña=contraseña
        else:
            print("tipo incorrecto en algun parametro")
    def retornaEmail(self):
        return self.__idcuenta + "@" + self.__dominio +"."+self.__tipodedominio
    def getDominio(self):
        return self.__dominio
    def crearCuenta(self,correo=" "):
        if type(correo==str):    
            return "se creo cuenta para correo: "+correo
        else:
            print("tipo incorrecto")
    def modificarContraseña(self,contraseña):
         if type(contraseña==str):
             self.__contraseña=contraseña
         else:
             print("tipo incorrecto")
    def testEmail(self):
        prueba=Email("pepe",234,5,"sess")
        prueba2=Email(11,"gmail","com",2345)
        prueba3=Email("pablo","edu","ar","pablo123")
        prueba4=Email()
        print(prueba4.retornaEmail())
        print("Dominio prueba2:",prueba2.getDominio())
        print("prueba3 contraseña: ",prueba3.getContraseña())
    def getContraseña(self):
        return self.__contraseña
