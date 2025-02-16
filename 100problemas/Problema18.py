a = int(input("Introduzca término cuadrático"))
b = int(input("Introduzca término acompañado de la variable"))
h = int(input("Introduzca término independiente"))
disc = float (b*b-4*a*h)
if disc<0:
    print("La solución es de números complejos")
else:
    sol_a= (-b + (disc)**1/2)/2*a
    sol_b= (-b - (disc)**1/2)/2*a
print ("Las soluciones son:", sol_a, "y", sol_b)

