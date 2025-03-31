#Ejercicio 8: Implementación de Mergesort
#Implementa el algoritmo de Mergesort para ordenar una lista de números ingresada por el usuario. El programa debe mostrar la lista antes y después del ordenamiento



def _Mergesort_(valores):
    #Primero contamos los valores que se nos dieron y verificamos qeu sean mayores a uno para evitar un bucle sin salida
    if len(valores)>1:
        mitad = (len(valores))//2
        parte1 = valores [mitad:]
        parte2 = valores [:mitad]
        #Se divide en dos los valores totales distribuyendo en dos partes los valores
        _Mergesort_(parte1)
        _Mergesort_(parte2)
#El algoritmo va dividiendo en dos cada parte dada hasta recducirla al máximo
        i=j=k=0

        while i<len(parte1) and j<len(parte2):
            if parte1[i] < parte2[j]:
                valores[k] = parte1[i]
                i+=1
            else:
                valores[k] = parte2[j]
                j += 1
            k += 1
        while i < len(parte1):
                valores[k] = parte1[i]
                i += 1
                k += 1
        while j < len(parte2):
                valores[k] = parte2[j]
                j += 1
                k += 1
#con los sigos while se comparan los numeros de la parte 1 y la parte dos para definirles un lugar y si quedan numeros los vuelve a comparar al final segun la posición y lo mismo se hace con la otra parte



valores = input("Introduzca los números a analizar")
valores = [float(num) for num in valores.split()]
#el split nos ayuda a separar los numeros
print(valores)
_Mergesort_(valores)
print(valores)

