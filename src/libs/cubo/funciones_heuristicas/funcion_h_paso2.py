import numpy as np
# importar el archivo de funciones de optimizacion para poder usar la funcion arista_con_su_centro
from src.libs.cubo.funciones_optimizacion.arista_con_su_centro import arista_con_su_centro 
# from src.libs.cubo.funciones_optimizacion.grupos import grupos as numero_de_grupos
from src import permutaciones

from src.libs.cubo.matriz import matriz_cubo


coste_mas_alto = 0
valores = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5":0,
        "6":0,
        "7":0,
        "8":0,
        "9":0,
}

def verificar_centros(cubo , matriz_cubo):

  cara_1 = cubo[0]
  arista_1 = matriz_cubo[0][2][1]
  arista_esta_en_su_centro = arista_con_su_centro( cara_1 , arista_1)
  if (not(arista_esta_en_su_centro)):
    return False
  
  cara_2 = cubo[1]
  arista_2 = matriz_cubo[1][2][1]
  arista_esta_en_su_centro = arista_con_su_centro( cara_2 , arista_2)
  if (not(arista_esta_en_su_centro)):
    return False
  
  cara_3 = cubo[2]
  arista_3 = matriz_cubo[2][2][1]
  arista_esta_en_su_centro = arista_con_su_centro( cara_3 , arista_3)
  if (not(arista_esta_en_su_centro)):
    return False
  
  cara_4 = cubo[3]
  arista_4 = matriz_cubo[3][2][1]
  arista_esta_en_su_centro = arista_con_su_centro( cara_4 , arista_4)
  if (not(arista_esta_en_su_centro)):
    return False
  

  return True




def calcular_coste_cruz(cubo):
  numero_aristas_cruz = 0

  if (cubo[5][0][1] == '1-b'):
    numero_aristas_cruz += 1
  if (cubo[5][1][0] == '3-b'):
    numero_aristas_cruz += 1
  if (cubo[5][1][1] == '4-b'):
    numero_aristas_cruz += 1
  if (cubo[5][1][2] == '5-b'):
    numero_aristas_cruz += 1
  if (cubo[5][2][1] == '7-b'):
    numero_aristas_cruz += 1
  
  return numero_aristas_cruz

def calcular_coste(cubo):
  coste = 0
  if (cubo[5][0][0] == '0-b'):
    coste += 1
  if (cubo[5][0][2] == '2-b'):
    coste += 1
  if (cubo[5][2][0] == '6-b'):
    coste += 1
  if (cubo[5][2][2] == '8-b'):
    coste += 1
  return coste

def calcular_coste_aristas(cubo):
  coste = 0
  if (cubo[0][1][0] == '3-az') and cubo[5][0][0] == '1-b':
    coste += 1
  if (cubo[0][1][2] == '5-az') and cubo[5][0][2] == '2-b':
    coste += 1
  if (cubo[2][1][0] == '3-v') and cubo[5][2][0] == '6-b':
    coste += 1
  if (cubo[2][1][2] == '5-v') and cubo[5][2][2] == '8-b':
    coste += 1
  return coste




def validacion(cubo , nodo_cubo):
  movimiento = []
  # if cubo[4][2][2] == '6-r' and cubo[4][2][1] == '3-r':
  #   # print(cubo)
  #   movimiento = [permutaciones.U_PRIMA , permutaciones.F_PRIMA , permutaciones.U , permutaciones.F]
  #   # print("suuuuuuuuuuuuuuuuuu++")
    
  if cubo[1][0][0] == '2-b' and cubo[4][0][1] == '5-az':
    movimiento = [permutaciones.R , permutaciones.U , permutaciones.R_PRIMA]
    # R U R'
  if cubo[0][0][2] == '2-b' and cubo[4][1][0] == '3-r':
    movimiento = [permutaciones.F_PRIMA , permutaciones.U_PRIMA , permutaciones.F]
    #F' U' F   

  if cubo[0][0][0] == '0-b' and cubo[4][1][2] == '5-n':
    movimiento = [permutaciones.F , permutaciones.U , permutaciones.U_PRIMA]
    #F,U,F'
  if cubo[3][0][2] == '0-b' and cubo[4][0][1] == '3-az':
    movimiento = [permutaciones.L_PRIMA , permutaciones.U_PRIMA , permutaciones.L]
    # L' U' L
  

  if cubo[2][0][2] == '6-b' and cubo[4][1][2] == '3-n':
    movimiento = [permutaciones.B_PRIMA , permutaciones.U_PRIMA , permutaciones.B]
    # b' u' b
  if cubo[3][0][0] == '6-b' and cubo[4][2][1] == '5-v':
    movimiento = [permutaciones.L , permutaciones.U , permutaciones.L_PRIMA]
    # L u L'

  if cubo[2][0][0] == '8-b' and cubo[4][1][0] == '5-r':
    movimiento = [permutaciones.B , permutaciones.U , permutaciones.B_PRIMA]
    # b u b'
  

  if cubo[1][0][2] == '8-b' and cubo[4][2][1] == '3-v':
    movimiento = [permutaciones.R_PRIMA , permutaciones.U_PRIMA , permutaciones.R]
    # r' , u' , r

  if cubo[4][2][2] == '8-az' and cubo[4][1][2] == '4-az':
    print("suuuuuuuuuuuuuuuuuu--")

  

  if len(movimiento) == 0:
    return False
  # print("SUUUUUUUUUUUUUUUUU")
  
  nodo_cubo.set_movimiento_previsto(movimiento)
  # print(nodo_cubo.get_movimiento_previsto())
  return True

  



def funcion_h_paso2(cubo):
    
    global coste_mas_alto
    global valores
  
    matriz_cubo_actual = cubo.get_estado()
    matriz_cubo_estado_padre = cubo.get_padre().get_estado()


    numero_aristas_cruz = calcular_coste_cruz(matriz_cubo_actual)

    coste_arista = calcular_coste_aristas(matriz_cubo_actual)
    coste_arista_padre = calcular_coste_aristas(matriz_cubo_estado_padre)
    
    coste_hijo = calcular_coste(matriz_cubo_actual)
    coste_hijo_real = (calcular_coste(matriz_cubo_actual) + numero_aristas_cruz ) + coste_arista
    coste_padre = calcular_coste(matriz_cubo_estado_padre)
    coste_padre_real = (calcular_coste(matriz_cubo_estado_padre) + numero_aristas_cruz) + coste_arista_padre

    

    centros_no_estan = verificar_centros(matriz_cubo_actual, matriz_cubo)

    

    if validacion(matriz_cubo_actual , cubo):
      # print("aaa")
      valor =  cubo.get_padre().get_contador_movimientos_previstos()
      cubo.set_contador_movimientos_previstos(valor+1)
      return True
    
    elif cubo.get_padre().get_contador_movimientos_previstos() > 4 :
      print("sss")
      return False
    else:

      if not(centros_no_estan ):
          return False
      
      # if coste_hijo == 3 and numero_aristas_cruz == 4:
      #     return True
      
      
      if coste_hijo == 4 and numero_aristas_cruz <= 4:
        return False
      
      
      if coste_hijo_real >= coste_padre_real - 6:

        
          # print(valores)
        

          condi = coste_hijo_real >= coste_mas_alto

          if condi:
              coste_mas_alto = coste_hijo_real

          condi = coste_hijo_real >= coste_mas_alto - 2
          if condi:
              if str(coste_mas_alto) not in valores:
                valores[str(coste_mas_alto)] = 0
              
              if (valores[str(coste_mas_alto)] > 1500):
                # print("suuuuuuuu")
                return False
              valores[str(coste_mas_alto) ] += 1
              
            
        
              return True
      if coste_hijo == 2 and numero_aristas_cruz == 4:
          return True
      return False

def reiniciar():
    global coste_mas_alto
    global n_encontradas
    global valores
    coste_mas_alto = 0

    n_encontradas = 0

    valores = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5":0,
        "6":0,
        "7":0,
        "8":0,
        "9":0,
    }

