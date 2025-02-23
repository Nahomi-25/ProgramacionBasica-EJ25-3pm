import statistics
num=input("Introduzca las edades separadas")
edades=[int(x) for x in num.split()]
media = statistics.mean(edades)
mediana=statistics.median(edades)
mod = statistics.mode(edades)
print("La media es:",media, ", la mediana es de:", mediana, "y la moda es:",mod)