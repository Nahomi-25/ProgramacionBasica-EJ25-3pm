#Ejercicio 1: Análisis de Texto con Diccionarios y Conjuntos
 #Desarrolla un programa que analice un texto ingresado por el usuario y determine:
 #- El número total de palabras en el texto.
 #- La cantidad de palabras únicas, utilizando un conjunto para evitar repeticiones.
 #- La frecuencia de cada palabra usando un diccionario donde la clave sea la palabra y el valor la cantidad de veces que aparece.
 # - La palabra más frecuente y cuántas veces aparece."


def _analisis_(texto):
    palabras = texto.split()
    nump = len(palabras) 
    #hacemos una lista con cada palabra del texto y con la función len() contamos los elementos, lo que nos da como resultado el número de palabras del texto
    palu = set(palabras)
    numpalu = len(palu)
    #en la variable "palu" (por PALabras Unicas) con la funcion set() creamos conjuntos de una sola palabra
    #con la función len() contamos los conjuntos que se crearon de una sola palabra
    numcp = dict()
    for palabra in palabras:
        if palabra in numcp:
            numcp[palabra]+=1
        else:
            numcp[palabra]=1
    #en la vatiable numcp (NUMero de Cada Palabra) creamos un diccionario
    #use un for y un if para hacer un contador de cada vez que aparece cada palabra en el texto, así se almacena en el diccionario
    palabra_mas_repetida = max(numcp)
    num_mas_grande = numcp[palabra_mas_repetida]
    #Con la función max() para encontrar la palabra más repetida 
    #y buscamos el valor de la palabra poniendola en el diccionario numcp
    print("Hay", nump, "palabras en el texto.")
    print("Hay",numpalu, "palabras únicas")
    print("la frecuencia de las palabras son:", numcp)
    print("La palabra más frecuente es:", palabra_mas_repetida, "apareciendo", num_mas_grande, "veces en el texto")
    #Al final mostramos los resultados


texto = input("Introduzca texto")
resultado= _analisis_(texto)

