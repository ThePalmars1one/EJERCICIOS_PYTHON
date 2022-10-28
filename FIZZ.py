print("INGRESE UN NUMERO")
numero=int(input())
print("---------------------------")
for numero in range (1,numero+1):
    if (numero%15==0):
        print("fizzbuzz")
        continue
    elif (numero%3==0):
        print("fizz")
        continue
    elif (numero%5==0):
        print("buzz")
        continue
    print (numero)
