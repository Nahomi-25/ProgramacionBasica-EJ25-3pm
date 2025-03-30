#Ejercicio 1: Análisis de Texto con Diccionarios y Conjuntos
 #Desarrolla un programa que analice un texto ingresado por el usuario y determine:
 #- El número total de palabras en el texto.
 #- La cantidad de palabras únicas, utilizando un conjunto para evitar repeticiones.
 #- La frecuencia de cada palabra usando un diccionario donde la clave sea la palabra y el valor la cantidad de veces que aparece.
 # - La palabra más frecuente y cuántas veces aparece."


def _analisis_(texto):
    palabras = texto.split()
    nump = len(palabras)
    palu = set(palabras)
    numpalu = len(palu)
    numcp = dict()
    for palabra in palabras:
        if palabra in numcp:
            numcp[palabra]+=1
        else:
            numcp[palabra]=1
    palabra_mas_repetida = max(numcp, key=numcp.get)
    num_mas_grande = numcp[palabra_mas_repetida]
    print("Hay", nump, "palabras en el texto.")
    print("Hay",numpalu, "palabras únicas")
    print("la frecuencia de las palabras son:", numcp)
    print("La palabra más frecuente es:", palabra_mas_repetida, "apareciendo", num_mas_grande, "veces en el texto")


texto = input("Introduzca texto")
print(_analisis_(texto))


