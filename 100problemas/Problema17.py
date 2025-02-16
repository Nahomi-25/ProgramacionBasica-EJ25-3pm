nombre = input("Introduzca nombre")
Names= ["Maria", "Carmen", "Juan", "Alejandro"]
print(Names)
Names.append(nombre)
print(Names)
n= Names.pop(0)
print("Se elimino", n)
print(Names)


Facultades = ["FOD", "FIME", "FCFM", "FIC"]
facu = input ("Introduzca facultad")
Facultades.append(facu)
print(Facultades)
n= Facultades.pop()
print("sacando elemento",n)
print(Facultades)