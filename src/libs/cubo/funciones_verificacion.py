from ..cubo.matriz import matriz_cubo
import numpy as np


def varificar_paso_1(cubo):
  matriz_cubo2 = cubo
  cara = matriz_cubo2[5]
  cara_original = matriz_cubo[5]

  if (cara[0][1] == cara_original[0][1]) and \
    (cara[1][0] == cara_original[1][0]) and \
    (cara[1][2] == cara_original[1][2]) and \
    (cara[2][1] == cara_original[2][1]):
    return True
  return False

def calcular_coste_aristas(cubo):
  coste = 0
  if (cubo[0][1][0] == '3-az'):
    coste += 1
  if (cubo[0][1][2] == '5-az'):
    coste += 1
  if (cubo[2][1][0] == '3-v'):
    coste += 1
  if (cubo[2][1][2] == '5-v'):
    coste += 1
  return coste


def varificar_paso_2(cubo):
  matriz_cubo2 = cubo

  cara = matriz_cubo2[5]
  cara_original = matriz_cubo[5]

  coste = calcular_coste_aristas(matriz_cubo2)


  if (cara[0][0] == cara_original[0][0]) and \
  (cara[0][2] == cara_original[0][2]) and \
  (cara[2][0] == cara_original[2][0]) and \
  (cara[2][2] == cara_original[2][2]):
    
    if varificar_paso_1(cubo):
      if coste == 4:
        return True
  return False


def varificar_paso_3(cubo):
  matriz_cubo2 = cubo
  cara = matriz_cubo2[4]
  cara_original = matriz_cubo[4]
  color = cara_original[0][0].split('-')[1]
  
  if (cara[0][1] != '*') and \
  (cara[1][0] != '*') and \
  (cara[1][2] != '*') and \
  (cara[2][1]!= '*'):
    if (cara[0][1].split('-')[1] == color) and \
      (cara[1][0].split('-')[1] == color) and \
      (cara[1][2].split('-')[1] == color) and \
      (cara[2][1].split('-')[1] == color):
    
      if varificar_paso_2(cubo):
        return True
  return False
  
def varificar_paso_4(cubo):
  matriz_cubo2 = cubo
  cara = matriz_cubo2[4]
  cara_original = matriz_cubo[4]
  color = cara_original[0][0].split('-')[1]
  
  if (cara[0][0] != '*') and \
  (cara[0][2] != '*') and \
  (cara[2][0] != '*') and \
  (cara[2][1]!= '*'):
    if (cara[0][0].split('-')[1] == color) and \
      (cara[0][2].split('-')[1] == color) and \
      (cara[2][0].split('-')[1] == color) and \
      (cara[2][1].split('-')[1] == color):
    
      if varificar_paso_3(cubo):
        return True
  return False





def varificar_paso_5(cubo):
  return np.array_equal(cubo , matriz_cubo)


