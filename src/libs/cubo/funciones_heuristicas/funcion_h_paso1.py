from src.libs.cubo.matriz import matriz_cubo

coste_mas_alto = 0
n_encontradas = 0


valores = {
  "0":0,
  "1":0,
  "2":0,
  "3":0,
  "4":0,
  "5":0,
}
ayuda = 0

def reiniciar():
  global coste_mas_alto 
  global n_encontradas 
  global valores 
  coste_mas_alto = 0
  n_encontradas = 0


  valores = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
  }

def funcion_h_paso1(cubo):
  matriz_cubo_estado_anterior = cubo.get_padre()

  if matriz_cubo_estado_anterior == None:
    return True
  
  matriz_cubo_estado_anterior = matriz_cubo_estado_anterior.get_estado()
  matriz_cubo_actual = cubo.get_estado()

  coste_hijo = 0
  coste_padre = 0
  
  cara_cubo_actual = matriz_cubo_actual[5]

  if (cara_cubo_actual[0][1] == '1-b') :
    coste_hijo+=1
  
  if (cara_cubo_actual[1][1] == '4-b'):
    coste_hijo+=1
  
  if (cara_cubo_actual[2][1] == '7-b') :
    coste_hijo+=1
  
  if (cara_cubo_actual[1][0] == '3-b') :
    coste_hijo+=1
  
  if (cara_cubo_actual[1][2] == '5-b'):
    coste_hijo+=1
  
  cara_cubo_estado_anterior = matriz_cubo_estado_anterior[5]



  if (cara_cubo_estado_anterior[0][1] == '1-b') :
    coste_padre+=1

  if (cara_cubo_estado_anterior[1][1] == '4-b'):
    coste_padre+=1

  if (cara_cubo_estado_anterior[2][1] == '7-b') :
    coste_padre+=1

  if (cara_cubo_estado_anterior[1][0] == '3-b') :
    coste_padre+=1

  if (cara_cubo_estado_anterior[1][2] == '5-b'):
    coste_padre+=1

  global coste_mas_alto
  global valores


  if coste_hijo >= coste_padre :
    # print(f"{coste_padre} - {coste_hijo} - {coste_mas_alto}")
    # print(valores)

    condi = coste_hijo >= coste_mas_alto

    if condi:
        coste_mas_alto = coste_hijo

    condi = coste_hijo >= coste_mas_alto - 1
    if condi:
        valores[str(coste_mas_alto)] += 1
        if (valores[str(coste_mas_alto)] > 1050):
          return False
        return True
  return False
