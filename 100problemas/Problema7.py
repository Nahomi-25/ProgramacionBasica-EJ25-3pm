def analizar_numero(n, m):
    if n % 2 == 0:
        print(f"{n} es un número par.")
    else:
        print(f"{n} es un número impar.")
    
    if n % m == 0:
        print(f"{n} es múltiplo de {m}.")
    else:
        print(f"{n} no es múltiplo de {m}.")

numero = int(input("Ingresa un número: "))
multiplo = int(input("Ingresa el número para verificar si es múltiplo: "))

analizar_numero(numero, multiplo)
