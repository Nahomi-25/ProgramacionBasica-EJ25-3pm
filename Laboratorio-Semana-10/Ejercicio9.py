#Ejercicio 9: Implementación de Múltiples Paradigmas
# Desarrolla un programa que implemente diferentes paradigmas de programación
#Imperativa: Uso de estructuras de control como condicionales y bucles.
#Estructurada: Separar el código en funciones bien definidas.
#Modular: Crear diferentes módulos para funcionalidades específicas.
#Orientada a Objetos: Definir clases y objetos.
#El programa debe demostrar el uso de cada paradigma con ejemplos claros.

#El programa sera una calculadora que resulve ecuaciones cuadraticas

#Cree dos modulos, uno de operacines básicas y otro para resolver ecuaciones cuadraticas
import operaciones
class Calculadora:
    def __init__(self):
            self.resultado = 0
    def realizar_operacion(self, operacion, a, b):
        if operacion == "suma":
            self.resultado = operaciones.sumar(a, b)
        elif operacion == "resta":
            self.resultado = operaciones.restar(a, b)
        elif operacion == "multiplicacion":
            self.resultado = operaciones.multiplicar(a, b)
        elif operacion == "division":
            self.resultado = operaciones.dividir(a, b)
        else:
            self.resultado = "Operación no válida"
        return self.resultado
# Cree una clase que define cada operación y manda llamar el modulo de operaciones básicas
#Sigue un menu con las dos opciones de la calculadora
menuPrincipal = f"""
\r \v
#####################################################################
##                                                                 ##
##              1.-Resolver ecuaciones cuadráticas                 ##
##              2.- Calculadora básica                             ##
##              3.- Cerrar                                         ## 
##                                                                 ##
#####################################################################
"""


BanderaMenuPrincipal = True

while BanderaMenuPrincipal:
    print(menuPrincipal)
    oPrincipal = input("Introduzca una opción: ")
    if oPrincipal=="1":
        #la primera opcion manda llamar el modulo que resuleve ecuaciones cuadraticas
        a = int(input("Introduzca término cuadrático"))
        b = int(input("Introduzca término acompañado de la variable"))
        c = int(input("Introduzca término independiente"))
        import Algebra
        Algebra._Ec2_(a,b,c)
    elif oPrincipal=="2":
        #la segunda opcion manda a un segundo menu donde podemos elegir la operación a realizar. El algoritmo usa la clase del principio para resolver la operación.
        menusec = f"""
        \r \v
        #####################################################################
        ##                                                                 ##
        ##              1.-Sumar                                           ##
        ##              2.- Restar                                         ##
        ##              3.- Multiplicar                                    ##
        ##              4.- Dividir                                         ##
        ##              5.- Cerrar                                         ## 
        ##                                                                 ##
        #####################################################################
        """


        BanderaMenusec= True

        while BanderaMenusec:
            print(menusec)
            oPrincipal = input("Introduzca una opción: ")
            if oPrincipal=="1":
                a = int(input("Introduzca primer numero"))
                b = int(input("Introduzca segundo numero"))
                print(f"Resultado: {Calculadora.realizar_operacion("suma", a, b)}")
            elif oPrincipal=="2":
                a = int(input("Introduzca primer numero"))
                b = int(input("Introduzca segundo numero"))
                print(f"Resultado: {calculadora_consola.realizar_operacion('resta', a, b)}")
            elif oPrincipal=="3":
                a = int(input("Introduzca primer numero"))
                b = int(input("Introduzca segundo numero"))
                print(f"Resultado: {calculadora_consola.realizar_operacion('multiplicación', a, b)}")
            elif oPrincipal=="2":
                a = int(input("Introduzca primer numero"))
                b = int(input("Introduzca segundo numero"))
                print(f"Resultado: {calculadora_consola.realizar_operacion('división', a, b)}")
            else:
                BanderaMenusec = False
    else:
        BanderaMenuPrincipal = False
