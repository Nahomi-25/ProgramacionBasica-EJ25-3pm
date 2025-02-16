nombre= ["Maria", "Carmen", "Juan", "Alejandro", "Miguel"]
apellido = ["León", "Castillo", "Ruiz", "Perez", "Córtez"]
C = int(input("Ingrese cantidad de nombres"))
for _ in range(C):
    import random
    name = random.choice(nombre)
    secname = random.choice(apellido)
    print(name, secname)
