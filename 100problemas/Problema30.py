def cuenta_atras(numero):
    numero-=1
    if numero>0:
        print(numero)
        cuenta_atras(numero)
    else:
        print("Fin")

cuenta_atras(10)

