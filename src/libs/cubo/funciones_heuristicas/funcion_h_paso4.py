import numpy as np
from src.libs.cubo.algoritmos.algoritmos_paso4 import algoritmos 
from src.libs.cubo.funciones_verificacion import varificar_paso_4


def funcion_h_paso4(cubo):
  matriz_cubo = np.copy(cubo.get_estado())
  
  for algoritmo in algoritmos:
    matriz_cubo = np.copy(cubo.get_estado())


    
    for movimiento in algoritmo:
      matriz_cubo = movimiento(matriz_cubo)
  


    if varificar_paso_4(matriz_cubo):
      cubo.set_movimiento_previsto(algoritmo)
      return True
    
  # print("***************************************************************+")
  return True


