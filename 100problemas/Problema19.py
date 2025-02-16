a= int(input("Introduzca el numero menor"))
b= int(input("Introduzca el numero mayor"))
c= int(input("Introduzca cantidad de números para generar"))
import random
numero = random.sample(range(a,b), c)
print(numero)