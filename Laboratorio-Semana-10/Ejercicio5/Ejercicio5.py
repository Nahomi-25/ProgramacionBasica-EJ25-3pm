#Crea un módulo de Python llamado conversor.py que contenga funciones para
# convertir:
# Kilómetros a millas.
# Celsius a Fahrenheit.
# Litros a galones.
# Luego, crea un programa principal que importe el módulo y permita al usuario realizar conversiones.




menuPrincipal = f"""
\r \v
#####################################################################
##                                                                 ##
##              1.- Kilómetros a millas.                           ##
##              2.- Grados Celsius a Fahrenheit                    ##
##              3.- Litros a galones                               ##
##              4.- Cerrar                                         ## 
##                                                                 ##
#####################################################################
"""


BanderaMenuPrincipal = True

while BanderaMenuPrincipal:
    print(menuPrincipal)
    oPrincipal = input("Introduzca una opción: ")
    if oPrincipal == '1':
        u = float(input("Introduzca los kilómetros: "))
        import Conversor
        print("Las millas son",Conversor.km_a_millas(u))
    elif oPrincipal == '2':
        u = float(input("Introduzca los grados Celsius: "))
        import Conversor
        print("Los farhenheit son:", Conversor.celsius_a_fahrenheit(u))
    elif oPrincipal == '3':
        u = float(input("Introduzca los litros: "))
        import Conversor
        print("Los galones son:", Conversor.litros_a_galones(u)) 
    else:
        BanderaMenuPrincipal = False
