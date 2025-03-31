# Ejercicio 4: Calculadora de Estad´ ısticas
# -Crea una funci´on que reciba una lista de n´ umeros y devuelva:
# -Promedio, mediana y desviaci´on est´andar.
# -Debe permitir un número arbitrario de argumentos usando *args.
# -Utilizar funciones lambda para c´alculos simples como la media.
# -El programa debe solicitar al usuario una lista de n´ umeros y mostrar los resultados.


#Con una sola definición hacemos los calculos, usando arg ya que no conocemos cuantos datos se nos rpoporciona
#guardamos los datos en una lista para poder manipularlos mejor
def _estadistica_(*args):
    numeros= list(args)
    prom = (lambda num: sum(num)/len(num))(numeros)
    #usamos lambda para ahorrar tiempo en la suma
    num_o=sorted(numeros)
    cantidad = len(num_o)
    if cantidad % 2==1:
        mediana = num_o[cantidad//2]
    else:
        mediana = (num_o[(cantidad//2)-1] + num_o[(cantidad//2)])/2 
    paso1 = (lambda num: sum((num - prom)**2 for num in num)/len(num))(numeros)
    desviación = (paso1)**1/2
    return prom, mediana, desviación


datos = input("Introduzca los números a analizar")
data = [float(num) for num in datos.split()]
prom, mediana, desviacion = _estadistica_(*data)
print("Promedio", prom, "Mediana:", mediana, "Desviación:", desviacion)


