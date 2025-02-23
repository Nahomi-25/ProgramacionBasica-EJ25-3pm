contactos = {}
nombre = input("Ingrese nombre de contacto")
numero = input("Ingrese numero de contacto")
correo = input("Ingrese correo de contacto")
contactos [nombre] = (numero,correo)
print("Lista de contactos")
for nombre in contactos:
    print(nombre,contactos [nombre] [0], contactos [nombre][1])