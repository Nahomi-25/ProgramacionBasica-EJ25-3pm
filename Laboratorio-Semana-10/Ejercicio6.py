#Ejercicio 6: Sistema de Gestión de Vehículos
#Crea una clase Vehiculo con los siguientes atributos y métodos:
#Atributos: marca, modelo, año y precio.
#Método para mostrar la información del vehículo.
#Crear subclases Automovil y Motocicleta con atributos adicionales como número de puertas o cilindrada

class Vehículo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self. modelo = modelo
        self.año = año
        self. precio = precio
    def __info__(self):
        return "Marca:", self.marca, "Modelo:", self.modelo, "Año:", self.año, "Precio:", self.precio
class Automovil(Vehículo):
        def __init__(self, marca, modelo, año, precio, numpuertas):
            super().__init__(self, marca,año,precio)
            self.nummpuertas = numpuertas
        def __info__(self):
            infobasica = super().__info__()
            return infobasica, "Numero de puertas:", self.nummpuertas

class Automovil(Motocicleta):
        def __init__(self, marca, modelo, año, precio, cilindrada):
           super().__init__(self, marca,año,precio)
           self.cilindrada = cilindrada
        def __info__(self):
            infobasica = super().__info__()
            return infobasica, "Numero de puertas:", self.cilindrada