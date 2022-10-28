gravedad = 9.81
fuerza = 3.711
fuerza_neptuno = 11.15

print("INGRESE SU PESO EN KG")
peso_tierra= int(input())
print("INDIQUE 1 PARA PESO EN MARTE Y 2 PARA NEPTUNO")
planeta= int(input())
if (planeta==1):
  peso_marte= peso_tierra / gravedad * fuerza
  print("SU PESO EN MARTE SERIA ",peso_marte)
else:
  peso_neptuno= peso_tierra / gravedad * fuerza_neptuno
  print("SU PESO EN MARTE NEPTUNO ",peso_neptuno)