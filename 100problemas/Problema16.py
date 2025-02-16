Voc = "aeiouAEIOU"
Con = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
contvoc = 0
contc = 0
palabra = input("Ingresa palabra")
for i in palabra:
    if i in Voc:
        contvoc = contvoc + 1
    else:
        contc = contc + 1

print ("El numero de vocales es",contvoc, "y de consonantes",contc)


