divisor= 1
residuos_cero=0

print("Ingrese un número")
numero=int(input())
if(numero<=1):
  print("No es un número primo")
else:
  while (divisor<=numero):
    division=numero%divisor
    if (division==0):
      residuos_cero=residuos_cero+1
      divisor=divisor+1
    else:
      divisor=divisor+1
  if (residuos_cero==2):
    print("Es un número primo")
  else:
    print ("No es un número primo")