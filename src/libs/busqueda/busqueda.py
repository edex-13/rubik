import numpy as np
#import numba

from .nodo import Nodo

from collections import deque

counter = 0
# @numba.jit(nopython=True)
def busqueda_amplitud_con_nodos(cubo_inicial, es_estado_final, operadores, FUNC_H , nodos_visitados=[] ):
  # print(es_estado_final)
  estados_visitados = {} 
  global counter 
  counter = 0
  matriz_cubo_inicial = cubo_inicial.get_estado()
  if es_estado_final(matriz_cubo_inicial):
    return [True , cubo_inicial, nodos_visitados]

  frontera = deque([cubo_inicial])

  estado_hijo = matriz_cubo_inicial.flatten()
  estado_str = ' '.join(estado_hijo)



  contador1 = 0
  contador2 = 0
  while len(frontera) > 0:


    cubo = frontera.popleft()

    hijos = []
    
    movimientos_previsto = cubo.get_movimiento_previsto()
    if len(movimientos_previsto) != 0:
      contador1 += 1
      

      nueva_matriz_cubo = np.copy(cubo.get_estado())
      nombres_movimientos  = []
      for movimiento_previsto in movimientos_previsto:
        hijo = movimiento_previsto(nueva_matriz_cubo)
        nombres_movimientos.append(movimiento_previsto.__name__)
        nueva_matriz_cubo = hijo

      nuevo_nodo = Nodo(hijo, f"CADENA-{str(nombres_movimientos)}" ,cubo_inicial.get_estado_o() )

      nuevo_nodo.set_movimiento_activo = True
      hijos.append(nuevo_nodo)
      cubo.set_hijos(hijos)
      if es_estado_final(nuevo_nodo.get_estado()):
            cubo.set_hijos(hijos)
            return [True , nuevo_nodo, nodos_visitados]

      frontera.appendleft(nuevo_nodo)
      


    else:
      for operador in operadores:
        nueva_matriz_cubo = np.copy(cubo.get_estado())
        hijo = operador(nueva_matriz_cubo)
        estado_str = ' '.join(hijo.flatten())
        estado_repetido  = estado_str  in estados_visitados
        estados_visitados[estado_str] = True

        if not estado_repetido:
          # print("mmm")


          nuevo_nodo = Nodo(hijo, operador.__name__ ,cubo_inicial.get_estado_o() )
          hijos.append(nuevo_nodo)
          cubo.set_hijos(hijos)
          counter = counter + 1
          
          if FUNC_H(nuevo_nodo):
            hijos.append(nuevo_nodo)
            if len(nuevo_nodo.get_movimiento_previsto()) >0:
              contador2 += 1
              frontera.appendleft(nuevo_nodo)
            else:
              frontera.append(nuevo_nodo)
            if es_estado_final(nuevo_nodo.get_estado()):
              cubo.set_hijos(hijos)
              return [True , nuevo_nodo, nodos_visitados]

      
        cubo.set_hijos(hijos)

  print(counter)
  # print(len(nodos_visitados))


  return [False, cubo_inicial , nodos_visitados]
