import numpy as np
from src.libs.cubo.algoritmos.algoritmos_paso3 import algoritmos 
from src.libs.cubo.funciones_verificacion import varificar_paso_3





def funcion_h_paso3(cubo):
  matriz_cubo = np.copy(cubo.get_estado())
  
  for algoritmo in algoritmos:
    matriz_cubo = np.copy(cubo.get_estado())


    
    for movimiento in algoritmo:
      matriz_cubo = movimiento(matriz_cubo)



    if varificar_paso_3(matriz_cubo):
      cubo.set_movimiento_previsto(algoritmo)
      return True
    
  return True