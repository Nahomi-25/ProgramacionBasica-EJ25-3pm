menuPrincipal = f"""
\r \v
#####################################################################
##                                                                 ##
##              1.- Dado                                           ##
##              2.- Moneda                                         ##
##              3.- Cerrar                                         ## 
##                                                                 ##
#####################################################################
"""

BanderaMenuPrincipal = True

while BanderaMenuPrincipal:
    print(menuPrincipal)
    oPrincipal = input("Introduzca una opción: ")
    if oPrincipal=="1":
        import random
        min= 1
        max = 6
        respuesta = "si"
        while respuesta == "si" or respuesta=="Si":
            print("El valor del dado es:")
            print(random.randint(min,max))
            respuesta= input("¿Deseas seguir jugando?")
    elif oPrincipal=="2":
        import random
        respuesta = "si"
        while respuesta == "si" or respuesta=="Si":
            print("El lado de la moneda es:")
            print(random.choice(["cara","cruz"]))
            respuesta= input("¿Deseas seguir jugando?")
    else:
        BanderaMenuPrincipal = False




