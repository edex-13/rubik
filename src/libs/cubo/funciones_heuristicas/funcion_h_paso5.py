import numpy as np
from src.libs.cubo.algoritmos.algoritmos_paso5 import algoritmos 
# from src.libs.cubo.funciones_verificacion import varificar_paso_5
from src.libs.cubo.matriz import matriz_cubo


valores = {
 '17': 11,
 '4': 9,
 '13': 9,
 '9': 8,
 '16': 7,
 '6': 5,
 '5': 5,
 '7': 5,
 '0': 5,
 '15': 5,
 '2': 4,
 '11': 4,
 '10': 4,
 '12': 4,
 '8': 4,
 '3': 3,
 '1': 3,
 '14': 3,
 '19': 2,
 '18': 2,
 '20': 2,
 }

def reiniciar():
  global valores 


  valores = {
  }

def varificar_paso_5(cubo):
   cubo = cubo[4]
   matriz_cubo2 = matriz_cubo[4]

   for _ in range(4):
    cubo = np.rot90(cubo)
    if np.array_equal(cubo , matriz_cubo2):
      return True

def funcion_h_paso5(cubo):
  global valores
  matriz_cubo = np.copy(cubo.get_estado())
  
  for algoritmo in algoritmos:
    matriz_cubo = np.copy(cubo.get_estado())


    
    for movimiento in algoritmo:
      matriz_cubo = movimiento(matriz_cubo)
    index = algoritmos.index(algoritmo)
    if varificar_paso_5(matriz_cubo):
      if str(index) not in valores:
                valores[str(index)] = 0
      valores[str(index)] +=1
      cubo.set_movimiento_previsto(algoritmo)
      # print(valores)

      return True
  return True