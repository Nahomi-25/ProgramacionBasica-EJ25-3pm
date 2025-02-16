menuPrincipal = f"""
\r \v
#####################################################################
##                                                                 ##
##              1.- Grados Celsius a Farenheit                     ##
##              2.- Grados Celsius a Kelvin                        ##
##              3.- Grados Farenheit a Celsius                     ##
##              4.- Grados Farenheit a Kelvin                      ##
##              5.- Grados Kelvin a Celsius                        ##
##              6.- Grados Kelvin a Farenheit                      ##
##              7.- Cerrar                                         ## 
##                                                                 ##
#####################################################################
"""


BanderaMenuPrincipal = True

while BanderaMenuPrincipal:
    print(menuPrincipal)
    oPrincipal = input("Introduzca una opción: ")
    grados = int(input("Introduzaca grados"))
    if oPrincipal == '1':
        respuesta = (1.8*grados) + 32
        print("Los", grados, "grados Celsius son", respuesta, "Farenheit")
    elif oPrincipal == '2':
       respuesta = grados + 273.15
       print("Los", grados, "grados Celsius son", respuesta, "Kelvin")
    elif oPrincipal == "3":
        respuesta = (grados - 32)/1.8
        print("Los", grados, "Farenheit son", respuesta, "grados Celsius")
    elif oPrincipal == "4":
        respuesta = ((grados - 32)/1.8) + 273.15
        print("Los", grados, "Farenheit son", respuesta, "Kelvin")
    elif oPrincipal == "5":
        respuesta = grados - 273.15
        print("Los", grados, "Kelvin son", respuesta, "grados Celsius")
    elif oPrincipal =="6":
        respuesta = ((grados - 273.15)*1.8) + 32
        print("Los", grados, "Kelvin son", respuesta, "Farenheit")
    else:
        BanderaMenuPrincipal = False