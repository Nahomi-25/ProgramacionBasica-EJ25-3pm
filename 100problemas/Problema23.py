Fila=int(input("Ingrese el número de filas"))
Columna=int(input("Ingrese el número de columnas"))
matrix=[ ]
for Fila_position in range(Fila):
    Fila=[ ]
    for element in range (Columna):
        Fila.append(int(input(f"Introduce un elemento a la fila {Fila_position +1}, columna{element+1}: ")))
    matrix.append(Fila)
for Fila in matrix:
    print(Fila)

m=int(input("Ingrese el número de filas"))
n=int(input("Ingrese el número de columnas"))
matrix2=[ ]
for i in range(m):
    m =[ ]
    for j in range (n):
        m.append(int(input(f"Introduce un elemento a la fila {i +1}, columna {j+1}: ")))
    matrix2.append(m)
for m in matrix2:
    print(m)

menuPrincipal = f"""
\r \v
#####################################################################
##                                                                 ##
##              1.- Sumar                                          ##
##              2.- Resatar                                        ##
##              3.- Multiplicar por escalar                        ##
##              4.- Cerrar                                         ##
##                                                                 ##
#####################################################################
"""


BanderaMenuPrincipal = True

while BanderaMenuPrincipal:
    print(menuPrincipal)
    oPrincipal = input("Introduzca una opción: ")
    if oPrincipal == '1':
         if len(matrix) != len(matrix2) or len(matrix[0]) != len(matrix2[0]):
            print("Las matrices no tienen el mismo tamaño y no se pueden sumar.")
         else:
            matriz_suma = []
            for i in range(len(matrix)):
                fila_suma = []
                for j in range(len(matrix[1])):
                    fila_suma.append(matrix[i][j] + matrix2[i][j])
                matriz_suma.append(fila_suma)
            for fila_suma in matriz_suma:
               print(fila_suma)
    elif oPrincipal == '2':
        if len(matrix) != len(matrix2) or len(matrix[0]) != len(matrix2[0]):
            print("Las matrices no tienen el mismo tamaño y no se pueden restar.")
        else:
            matriz_resta = []
            for i in range(len(matrix)):
                fila_resta = []
                for j in range(len(matrix[1])):
                    fila_suma.append(matrix[i][j] + matrix2[i][j])
                matriz_resta.append(fila_resta)
            for fila_resta in matriz_resta:
               print(fila_resta)
    elif oPrincipal == '3':
        escalar= int(input("introduzca escalar"))
        matriz_resp = []
        for i in range(len(matrix)):
            fila_resp = []
            for j in range(len(matrix[1])):
                fila_resp.append(matrix[i][j]*escalar)
                matriz_resp.append(fila_resp)
        for fila_resp in matriz_resp:
           print(fila_resp)
    BanderaMenuPrincipal = False
