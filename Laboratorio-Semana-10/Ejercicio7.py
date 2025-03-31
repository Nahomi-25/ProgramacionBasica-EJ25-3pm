#Ejercicio 7: Ordenamiento y Búsqueda
#Implementa un programa que realice lo siguiente:
#Genere una lista de números aleatorios.
#Ordene la lista usando el algoritmo de Quicksort.
#Permita al usuario buscar un núumero en la lista usando búsqueda binaria.
#El programa debe mostrar la lista antes y después del ordenamiento y los resultados de la búsqueda.

import random
def _Quicksort_(lista):
    if len(lista) <= 1: 
        return lista
        #verificamos que los elementos en la lista sean mayores a 1
    inicial = lista[0]
    menor = [n for n in lista[1:] if n <= inicial]
    mayor = [n for n in lista[1:] if n > inicial]
    return _Quicksort_(menor) + [inicial] + _Quicksort_(mayor)
#a partir del primer dato de la lista definimos los que son mayores y menores guardando cada uno en una lista segun su valor
#Una vez ya se almacenaron los numeros mayores y menores unimos los datos en una sola lista
def busqueda_binaria(lista, valor):
    inicio = 0
    fin = len(lista)-1
    while inicio <= fin:
        medio= (inicio+fin)//2
        if valor == lista[medio]:
            return medio
        elif lista[medio] > valor:
            inicio = medio + 1
        else:
            final= medio - 1
    return None
#como la lista ya esta ordenada, la busqueda binaria va sumar los extremos y obtener el valor medio, lo va comparar con el valor deseado y va repetir el proceso hasta legar al numero indicado
lista = [random.randint(-20,20) for _ in range(10)]
print (lista)
nuevalis= _Quicksort_(lista)
print("Lista ordenada:", nuevalis)
valor = int(input("Introduzca el número a buscar"))          
resultado = busqueda_binaria(nuevalis, valor)
if resultado is not None:
    print("El número se encuentra en la posición", resultado)
else:
    print("El número no se encuentra en la lista.")
