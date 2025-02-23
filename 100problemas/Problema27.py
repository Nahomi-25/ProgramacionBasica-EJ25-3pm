menuPrincipal = f"""
\r \v
#####################################################################
##                                                                 ##
##              1.-Metros a Kilómetros                             ##
##              2.- Kilómetros a metros                            ##
##              3.- Minutos a segundos                             ##
##              4.- Minutos a horas                                ##
##              5.- Cerrar                                         ## 
##                                                                 ##
#####################################################################
"""


BanderaMenuPrincipal = True

while BanderaMenuPrincipal:
    print(menuPrincipal)
    oPrincipal = input("Introduzca una opción: ")
    if oPrincipal=="1":
        metros= int(input("Introzuca metros"))
        respuesta= metros/1000
        print("Los", metros, "metros son", respuesta, "kilometros")
    elif oPrincipal=="2":
        kilometros = int(input("Introzuca los kilometros"))
        respuesta = kilometros*1000
        print("Los", kilometros, "kilometros son", respuesta, "metros")
    elif oPrincipal=="3":
        minutos = int(input("Introzuca los minutos"))
        print("Los", minutos, "minutos son", minutos*60, "segundos")
    elif oPrincipal=="4":
        minutos = int(input("Introzuca los minutos"))
        print("Los", minutos, "minutos son", minutos/60, "horas")
    else:
        BanderaMenuPrincipal = False
