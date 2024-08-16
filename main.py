
from src import permutaciones
import random
import numpy as np
from src.libs.cubo.matriz import matriz_cubo

movimientos = [
      permutaciones.R,
      permutaciones.U,
      permutaciones.L,
      permutaciones.F,
      permutaciones.D,
      permutaciones.B,
      permutaciones.R_PRIMA,
      permutaciones.U_PRIMA,
      permutaciones.L_PRIMA,
      permutaciones.F_PRIMA,
      permutaciones.D_PRIMA,
      permutaciones.B_PRIMA,
  ]

matriz_revuelta = matriz_cubo

r=[]
for _ in range(0, 10):
      movement = random.choice(movimientos)
      r.append(movement.__name__)
      matriz_revuelta = movement(matriz_revuelta)


print(r)

# Abre el archivo en modo escritura ("w" para escribir, "a" para agregar al final)

matriz_revuelta = matriz_revuelta.flatten()

cadena = ','.join(map(str, matriz_revuelta))

with open("matriz.txt", "w") as archivo:
      archivo.write(cadena)
   

# El archivo se cierra automáticamente cuando sales del bloque 'with'
