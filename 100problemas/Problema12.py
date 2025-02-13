n1 =float(input("ingrese número"))
n2 =float(input("ingrese número"))
n3 =float(input("ingrese número"))
if n1>=n2 and n1>=n3:
    mayor = n1
elif n2>=n3 and n2>=n1:
    mayor=n2
else:
    mayor=n3
print ("El número mayor es:", mayor)