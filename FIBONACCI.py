X = 1
Z= 0
print("Ingrese un número para la secuencia de Fibonacci")
numero=int(input())
print("----------------------")
print(Z)
print(X)
for fibonacci in range (1, numero, 1):
  suma=X+Z
  Z=X
  X=suma
  print(suma)

  #0,1,1,2,3