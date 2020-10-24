import csv
from classEmail import Email
if __name__=='__main__':
    nombre=input("Bienvenido ingresa tu nombre: \n")
    correo=input("Ingresa tu direccion de correo: \n")
    while((correo.count("@")!=1) or (correo.count(".")==0)):
        print("Direccion de correo incorrecta, vuela a intentarlo")
        correo=input('Ingresa tu direccion de correo: \n')
    Contraseña=input("Ingresa tu contraseña: \n")
    correo=correo.split("@");
    idcuenta=correo[0]
    otrosdatos=correo[1].split(".",1)  
    dominio=otrosdatos[0]
    tipo=otrosdatos[1]
    cuenta=Email(idcuenta,dominio,tipo,Contraseña)
    c=cuenta.retornaEmail()
    print("Estimado {} te enviaremos tus mensajes a la dirección {} ".format(nombre,cuenta.retornaEmail()))
    
    print("A continuación ingresa tu contraseña para modificarla, de lo contrario ingresa n")
    Contraseña=input("Contraseña actual o n: ")
    while(Contraseña!="n"):    
       if (Contraseña==cuenta.getContraseña()):
            print("Ingresa la nueva contraseña")
            Contraseña=input("Contraseña nueva: ")
            cuenta.modificarContraseña(Contraseña)
            print("Se modifico la contraseña ")
            Contraseña="n"
       else:
           print("Contraseña incorrecta")
           Contraseña=input("Contraseña actual o n: ")
           
    busqueda=input("Ingresa un dominio para buscar el mas usado dentro de un archivo \n")
    lista=[]
    otrosdatos=[]
    archivo=open("correos.csv")
    reader=csv.reader(archivo,delimiter=" ")
    for fila in reader: 
        correo=fila[0].split("@");
        idcuenta=correo[0]
        otrosdatos=correo[1].split(".",1)
        dominio=otrosdatos[0]
        tipo=otrosdatos[1]
        cuenta=Email(idcuenta,dominio,tipo)    
        lista.append(cuenta)
    archivo.close()
    contador=0
    for correo in lista:
        if(correo.getDominio()==busqueda):
            contador+=1
    print("La cantidad de veces que aparece el dominio indicado es :",contador)
    print("funcion de test:")
    cuenta.testEmail()
