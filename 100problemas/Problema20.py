def busqueda_binaria(Lista, valor):
    inicio = 0
    fin = len(Lista)-1
    while inicio <= fin:
        medio= (inicio+fin)//2
        if valor == Lista[medio]:
            return medio
        elif Lista[medio] > valor:
            inicio = medio + 1
        else:
            final= medio - 1
    return None

Lista= [27, 34, 64, 32, 22, 59, 40, 60, 0, 53]
valor = int(input("Ingrese el número a buscar"))
resultado = busqueda_binaria(Lista, valor) 
if resultado is  None:
    print("El número",valor, "no fue encontrado")
else:
    print("El número",valor, "esta en el lugar",resultado)

def busqueda_lineal(lista, objetivo):
    for indice, valor in enumerate(lista):
        if valor==objetivo:
            return indice
    return None

lista= [82, 5, 64, 44, 86, 8, 16, 3, 53, 19]
objetivo = int(input("Ingrese el número a buscar"))
busqueda = busqueda_lineal(lista, objetivo)
if busqueda is None:
    print("El número",objetivo, "no fue encontrado")
else:
    print("El número",objetivo, "esta en el lugar", busqueda)




