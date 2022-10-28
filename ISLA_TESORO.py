print("Bienvenido a la Isla del Tesoro")
print("Escoge un camino")
print("Derecha (1) o Izquierda (2)")
opcion_a=int(input())
if (opcion_a==1):
  print("Caiste por un agujero. GAME OVER")
else:
  print("Nadar (1) o Esperar(2)")
  opcion_b=int(input())
  if (opcion_b==1):
    print("Cual puerta escoges (Rojo (1), Negra(2) y Azul(3))")
    puerta= int(input())
    if (puerta==1):
      print("Sendero con dos caminos (Corto (1) o Largo(2))")
      sendero=int(input())
      if (sendero==1):
        print("Caes por un acantilado. GAME OVER")
      else:
        print("Te come una planta carnivora. GAME OVER")
    elif(puerta==2):
        print("Abres y hay dos puertas mas (Morada(1) y Verde(2))")
        puertas_segundas=int(input())
        if (puertas_segundas==1):
                          print("Brincas en un agujero y está el tesoro. GANASTE")
        else:
                           print("Tesoro Falso. GAME OVER")
    else:
      print("Hay una montaña (Subir (1) o Rodear(2))")
      montaña=int(input())
      if (montaña==1):
        print("Tesoro en la cima. GANASTE")
      else:
        print("Serpiente te envenena. GAME OVER")
  else:
    print("Atacado por una tribu. GAME OVER")