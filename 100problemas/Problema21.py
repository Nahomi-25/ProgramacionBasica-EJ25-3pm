menuPrincipal = f"""
\r \v
#####################################################################
##                                                                 ##
##              1.- Cuadrado                                       ##
##              2.- Triangulo                                      ##
##              3.- Rectangulo                                     ##
##              4.- Círculo                                        ##
##              5.- Cerrar                                         ## 
##                                                                 ##
#####################################################################
"""


BanderaMenuPrincipal = True

menuSec = f"""
\r \v
#####################################################################
##                                                                 ##
##              1.- Área                                           ##
##              2.- Volumen                                        ##
##              3.- Cerrar                                         ## 
##                                                                 ##
#####################################################################
"""


BanderaMenuSec = True


while BanderaMenuPrincipal:
    print(menuPrincipal)
    oPrincipal = input("Introduzca una opción: ")
    if oPrincipal=="1":
        while BanderaMenuSec:
            print(menuSec)
            oSec = input("Introduzca una opción:")
            if oSec== "1":
                lado= int(input("Introduzca medida del lado"))
                print("El área es de:",lado*lado,"unidades cuadradas")
            elif oSec == "2":
                lado= int(input("Introduzca medida del lado"))
                print("El volumen del cubo es de:",lado*lado*lado,"unidades cúbicas")
            else:
                BanderaMenuSec = False
    elif oPrincipal=="2":
        while BanderaMenuSec:
            print(menuSec)
            oSec = input("Introduzca una opción: ")
            if oSec== "1":
                base = int(input("Introduzca medida de la base"))
                altura = int(input("Introduzca medida de la altura"))
                area = (base*altura)/2
                print("El área es de:",lado*lado,"unidades cuadradas")
            elif oSec == "2":
               radio = int(input("Introduzca medida del radio"))
               altura = int(input("Introduzca medida de la altura en las mismas unidades del radio"))
               volumenc = (3.1416*radio*radio*altura)/3
               print("El volumen del cono es de:",volumenc,"unidades cúbicas")
            else:
                BanderaMenuSec = False
    elif oPrincipal=="3":
        while BanderaMenuSec:
            print(menuSec)
            oSec = input("Introduzca una opción: ")
            if oSec== "1":
                base = int(input("Introduzca medida de la base"))
                altura = int(input("Introduzca medida de la altura"))
                area = base*altura
                print("El área es de:",area,"unidades cuadradas")
            elif oSec == "2":
               base = int(input("Introduzca medida de la base"))
               altura = int(input("Introduzca medida de la altura en las mismas unidades de la base"))
               ancho = int(input("Introduzca medida del ancho en las mismas unidades de la base"))
               print("El volumen del paralelepípedo es de:",base*altura*ancho,"unidades cúbicas")
            else:
                BanderaMenuSec = False
    elif oPrincipal=="4":
        while BanderaMenuSec:
            print(menuSec)
            oSec = input("Introduzca una opción: ")
            if oSec== "1":
                radio= int(input("Introduzca medida del radio"))
                area = 3.1416*radio*radio
                print("El área es de:",area,"unidades cuadradas")
            elif oSec == "2":
                radio= int(input("Introduzca medida del radio"))
                volumen= (4*3.1416*radio*radio*radio)/3
                print("El volumen del cubo es de:",volumen,"unidades cúbicas")
            else:
                BanderaMenuSec = False
    else:
        BanderaMenuPrincipal = False
        
    #elif oPrincipal=="2":
     #   base = input("Introduzca medida de la base")
      #  alt = input("Introduzca medida de altura en las mismas unidades de la base")
       # print ("El área del trángulo es:", base*altura/2, "unidades cuadradas")