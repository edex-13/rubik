import numpy as np
# from libs.cubo.matriz import matriz_cubo

from .libs.rotaciones_cubo.generar import generar

def R(cubo):
  cubo2 = np.copy(cubo)

  generar('vertical', 2, cubo2 , 'contrario')
  generar('cara', 0, cubo2,'normal' ,1)
  
  return cubo2


def R_PRIMA(cubo):
  cubo2 = np.copy(cubo)

  generar('vertical', 2, cubo2 , 'normal')
  generar('cara', 0, cubo2,'contrario' ,1)

  return cubo2


def L(cubo):
  cubo2 = np.copy(cubo)

  generar('vertical', 0, cubo2 , 'normal')
  generar('cara', 0, cubo2,'normal', 3)

  return cubo2

def L_PRIMA(cubo):
  cubo2 = np.copy(cubo)

  generar('vertical', 0, cubo2 , 'contrario')
  generar('cara', 0, cubo2,'contrario', 3)

  return cubo2



def U(cubo):
  cubo2 = np.copy(cubo)

  generar('horizontal', 0, cubo2 , 'contrario')
  generar('cara', 0, cubo2,'normal', 4)
  return cubo2


def U_PRIMA(cubo):
  cubo2 = np.copy(cubo)

  
  generar('horizontal', 0, cubo2 , 'normal')
  generar('cara', 0, cubo2,'contrario', 4)
 


  return cubo2


def D(cubo):
  cubo2 = np.copy(cubo)

  generar('horizontal', 2, cubo2 , 'normal')
  generar('cara', 5, cubo2,'normal' ,5)

  return cubo2

def D_PRIMA(cubo):
  cubo2 = np.copy(cubo)

  generar('horizontal', 2, cubo2 , 'contrario')
  generar('cara', 5, cubo2,'contrario' ,5)

  return cubo2



def F(cubo):
  cubo2 = np.copy(cubo)

  cubo2 = generar('lateral' , 2 , cubo2, 'contrario')
  cubo2 = generar('cara' , 0 , cubo2 ,'normal')

  return cubo2
def F_PRIMA(cubo):
  cubo2 = np.copy(cubo)

  cubo2 = generar('lateral' , 2 , cubo2, 'normal')
  cubo2 = generar('cara' , 0 , cubo2 ,'contrario')

  

  return cubo2



def B_PRIMA(cubo):
  cubo2 = np.copy(cubo)

  cubo2 = generar('lateral' , 0, cubo2 , 'contrario')
  cubo2 = generar('cara' , 2 , cubo2,'contrario',2)

  return cubo2


def B(cubo):
  cubo2 = np.copy(cubo)

  cubo2 = generar('lateral' , 0, cubo2, 'normal')

  cubo2 = generar('cara' , 2 , cubo2 ,'normal', 2)

  return cubo2

