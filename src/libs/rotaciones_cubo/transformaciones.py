#import numba
import numpy as np

#@numba.jit(nopython=True)
def girar_lado(row, cubo, sentido="normal"):
    # Guarda una copia de la fila correspondiente del cubo
    estado_anterior = cubo[0, row].copy()
    
    if sentido == "normal":
        estado_anterior = cubo[3, row].copy()
    
        # Realiza la rotación
        cubo[1:4, row] = cubo[0:3, row]
        cubo[0, row] = estado_anterior


    elif sentido == "contrario":
        # Realiza la rotación en sentido contrario
        cubo[0:3, row] = cubo[1:4, row]
        cubo[3, row] = estado_anterior
    else:
        pass
        # raise ValueError("El parámetro 'sentido' debe ser 'normal' o 'contrario'")
    
    return cubo





# import numpy as np
#@numba.jit(nopython=True)
def girar_cara(cara, cubo , sentido="normal"):
    if sentido == "normal":  # Sentido horario
        cubo[cara] = np.rot90(cubo[cara], 3)
    elif sentido == "contrario":  # Sentido antihorario
        cubo[cara] = np.rot90(cubo[cara])
    return cubo



# #@numba.jit(nopython=True)
def mutar_cubo (cube , undo = False ,original_cube = []):
    if original_cube is None:
        original_cube = []
    if undo:       
        original_cube[0] = np.transpose(np.fliplr(cube[0]))
        original_cube[5] = np.transpose(np.fliplr(cube[1]))
        original_cube[2] = np.transpose(np.flip(cube[2] , axis= 0))
        original_cube[4] = np.transpose(np.fliplr(cube[3]))
        return original_cube

    face1 = np.fliplr(np.transpose(cube[0]))
    face2 = np.fliplr(np.transpose(cube[5]))
    face3 = np.transpose(cube[2])
    face4 = np.fliplr(np.transpose(cube[4]))

    new_cube = np.array([face1 , face2 , np.flip(face3, axis=0), face4])
    return new_cube

#@numba.jit(nopython=True)
def rotar_cubo(cubo):
  cubo_copia = np.copy(cubo)

  cubo_copia[0] = cubo[3]
  cubo_copia[1] = cubo[0]
  cubo_copia[2] = cubo[1]
  cubo_copia[3] = cubo[2]

  cubo_copia = girar_cara(4,cubo_copia )
  cubo_copia = girar_cara(4,cubo_copia )
  cubo_copia = girar_cara(4,cubo_copia )
  cubo_copia = girar_cara(5,cubo_copia )

  return cubo_copia

#@numba.jit(nopython=True)
def rotar_inverso_cubo(cubo):
  cubo_copia = np.copy(cubo)

  cubo_copia[3] = cubo[0]
  cubo_copia[0] = cubo[1]
  cubo_copia[1] = cubo[2]
  cubo_copia[2] = cubo[3]

  cubo_copia = girar_cara(4,cubo_copia )

  cubo_copia = girar_cara(5,cubo_copia )
  cubo_copia = girar_cara(5,cubo_copia )
  cubo_copia = girar_cara(5,cubo_copia )

  return cubo_copia