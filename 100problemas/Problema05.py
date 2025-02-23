def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  
        # Comprobamos hasta la raíz cuadrada de n
        if n % i == 0:
            return False
    return True

numero = int(input("Introduce un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
