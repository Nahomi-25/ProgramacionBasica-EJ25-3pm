Anio = int(input("Ingresa el año"))
if (Anio % 4 == 0 and Anio % 100 != 0) or (Anio % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")