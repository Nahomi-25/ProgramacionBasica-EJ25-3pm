Oracion = input("Escribe la oración")
Oracion = Oracion.replace(" ","")
a = Oracion
b = str(Oracion)[::-1] 
if a == b:
    print ("Si es palíndromo")
else:
    print ("No es palíndromo")

    

