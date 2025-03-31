#Desarrolla un programa que permita gestionar contactos de la siguiente manera:
#Cada contacto debe ser almacenado como una tupla con nombre, número y correo.
# La agenda de contactos debe almacenarse en una lista.
#Debe permitir agregar nuevos contactos.
#Buscar contactos por nombre e imprimir sus detalles.
# Listar todos los contactos en orden alfab´ etico.

#creamos una función para cada acción
Lcontactos = []
def _agregar_(nombre, numero, correo):
    contacto = (nombre, numero, correo)
    Lcontactos.append(contacto)
    return Lcontactos

def _buscar_(nombre):
    for contacto in Lcontactos:
        if contacto [0].lower == nombre.lower:
            print(contacto[0],contacto[1],contacto[2])
        else:
            print("Contacto no encontrado")



menuPrincipal = f"""
\r \v
#####################################################################
##                                                                 ##
##              1.- Agregar contacto                               ##
##              2.- Buscar contacto                                ##
##              3.- Mostrar contactos                              ##
##              4.- Cerrar                                         ## 
##                                                                 ##
#####################################################################
"""
#Usamos un menu para saber que acción realizar
    
BanderaMenuPrincipal = True
while BanderaMenuPrincipal:
    print(menuPrincipal)
    oPrincipal = input("Introduzca una opción: ")
    if oPrincipal=="1":
        nombre = input("Ingrese nombre")
        numero = int(input("Ingrese el número"))
        correo = input ("Ingrese el correo")
        _agregar_(nombre, numero, correo)
        #mandamos llamar a la función necesaria en cada opción
    elif oPrincipal=="2":
        nombre = input("Ingrese nombre")
        _buscar_(nombre)
    elif oPrincipal=="3":
        Lcontactos.sort()
        for contacto in Lcontactos:
            print(contacto[0],contacto[1],contacto[2])
    else:
        BanderaMenuPrincipal = False



















