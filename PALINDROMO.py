#ALGORITMO DE PALINDROMO

invertida=input("INGRESE UNA PALABRA\n")
invertida=invertida.upper()
invertida_final=invertida.replace(" ","")
Palindromo = invertida_final[::-1]
if (Palindromo==invertida_final):
    print("ES PALINDROMA")
    print("--------------------")
    print(Palindromo)
    print(invertida)
    print("--------------------")
else:
    print("NO ES PALINDROMA")
    print("--------------------")
    print(Palindromo)
    print(invertida)
    print("--------------------")
