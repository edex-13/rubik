from ..busqueda.busqueda import busqueda_amplitud_con_nodos
from src import permutaciones


from .funciones_heuristicas.funcion_h_paso1 import funcion_h_paso1
from .funciones_heuristicas.funcion_h_paso1 import reiniciar as reiniar_h_1
from .funciones_verificacion import varificar_paso_1

from .funciones_heuristicas.funcion_h_paso2 import funcion_h_paso2
from .funciones_heuristicas.funcion_h_paso2 import reiniciar as reiniar_h_2
from .funciones_verificacion import varificar_paso_2

from .funciones_heuristicas.funcion_h_paso3 import funcion_h_paso3
from .funciones_verificacion import varificar_paso_3

from .funciones_heuristicas.funcion_h_paso4 import funcion_h_paso4
from .funciones_verificacion import varificar_paso_4

from .funciones_heuristicas.funcion_h_paso5 import funcion_h_paso5
from .funciones_heuristicas.funcion_h_paso5 import reiniciar as reiniar_h_5

from .funciones_verificacion import varificar_paso_5

from .funciones_optimizacion.crear_array_de_tratamiento import crear_array_de_tratamiento

# IMPORTAR LA MATRIZ DEL CUBO
from src.libs.cubo.matriz import matriz_cubo

coste_mas_alto = 0
n_encontradas = 0
def a(cubo):
  return True
  


def resolver_paso1(cubo, movimientos, estados_visitados):
  reiniar_h_1()
  # FICHAS DE LA CRUZ
  cara1 = matriz_cubo[5]
  fichas = [cara1[0][1] , cara1[1][0] , cara1[1][2] , cara1[2][1]]

  cubo_tratamiento = crear_array_de_tratamiento(cubo.get_estado() ,fichas )


  cubo.set_estado(cubo_tratamiento)

  return busqueda_amplitud_con_nodos(cubo, varificar_paso_1, movimientos, funcion_h_paso1, estados_visitados)


def resolver_paso2(cubo, movimientos, estados_visitados):
  reiniar_h_2()
  cara1 = matriz_cubo[5]
  cara2 = matriz_cubo[0]
  cara3 = matriz_cubo[1]
  cara4 = matriz_cubo[2]
  cara5 = matriz_cubo[3]

  fichas = [cara1[0][1] ,
  cara1[0][0] ,
  cara1[0][2] ,
  cara1[1][0] ,
  cara1[1][2] ,
  cara1[2][0] ,
  cara1[2][1] ,
  cara1[2][2] ,


  cara2[1][0] ,
  cara2[1][2] ,

  cara2[2][0] ,
  cara2[2][1] ,
  cara2[2][2] ,

  cara3[1][0] ,
  cara3[1][2] ,

  cara3[2][0] ,
  cara3[2][1] ,
  cara3[2][2] ,
  
  cara4[1][0] ,
  cara4[1][2] ,

  cara4[2][0] ,
  cara4[2][1] ,
  cara4[2][2] ,

  cara5[1][0] ,
  cara5[1][2] ,

  cara5[2][0] ,
  cara5[2][1] ,
  cara5[2][2] ,


  ]


  cubo_tratamiento = crear_array_de_tratamiento(cubo.get_estado() ,fichas)

  cubo.set_estado(cubo_tratamiento)

  return busqueda_amplitud_con_nodos(cubo, varificar_paso_2, movimientos, funcion_h_paso2, estados_visitados)



def resolver_paso3(cubo, movimientos, estados_visitados):
  cara1 = matriz_cubo[5]
  cara2 = matriz_cubo[0]
  cara3 = matriz_cubo[1]
  cara4 = matriz_cubo[2]
  cara5 = matriz_cubo[3]
  cara6 = matriz_cubo[4]

  fichas = [cara1[0][1] ,
  cara1[0][0] ,
  cara1[0][2] ,
  cara1[1][0] ,
  cara1[1][2] ,
  cara1[2][0] ,
  cara1[2][1] ,
  cara1[2][2] ,


  cara2[1][0] ,
  cara2[1][2] ,

  cara2[2][0] ,
  cara2[2][1] ,
  cara2[2][2] ,

  cara3[1][0] ,
  cara3[1][2] ,

  cara3[2][0] ,
  cara3[2][1] ,
  cara3[2][2] ,
  
  cara4[1][0] ,
  cara4[1][2] ,

  cara4[2][0] ,
  cara4[2][1] ,
  cara4[2][2] ,

  cara5[1][0] ,
  cara5[1][2] ,

  cara5[2][0] ,
  cara5[2][1] ,
  cara5[2][2] ,

  # cara6[0][0],
  cara6[0][1],
  # cara6[0][2],
  cara6[1][0],
  cara6[1][2],
  # cara6[2][0],
  cara6[2][1],
  # cara6[2][2],

  ]

  cubo_tratamiento = crear_array_de_tratamiento(cubo.get_estado() ,fichas)
  # print(cubo_tratamiento)
  cubo.set_estado(cubo_tratamiento)
  movimientos = [permutaciones.U , permutaciones.U_PRIMA]

  return busqueda_amplitud_con_nodos(cubo, varificar_paso_3, movimientos, funcion_h_paso3, estados_visitados)




def resolver_paso4(cubo, movimientos, estados_visitados):
  cara1 = matriz_cubo[5]
  cara2 = matriz_cubo[0]
  cara3 = matriz_cubo[1]
  cara4 = matriz_cubo[2]
  cara5 = matriz_cubo[3]
  cara6 = matriz_cubo[4]

  fichas = [cara1[0][1] ,
  cara1[0][0] ,
  cara1[0][2] ,
  cara1[1][0] ,
  cara1[1][2] ,
  cara1[2][0] ,
  cara1[2][1] ,
  cara1[2][2] ,


  cara2[1][0] ,
  cara2[1][2] ,

  cara2[2][0] ,
  cara2[2][1] ,
  cara2[2][2] ,

  cara3[1][0] ,
  cara3[1][2] ,

  cara3[2][0] ,
  cara3[2][1] ,
  cara3[2][2] ,
  
  cara4[1][0] ,
  cara4[1][2] ,

  cara4[2][0] ,
  cara4[2][1] ,
  cara4[2][2] ,

  cara5[1][0] ,
  cara5[1][2] ,

  cara5[2][0] ,
  cara5[2][1] ,
  cara5[2][2] ,

  cara6[0][0],
  cara6[0][1],
  cara6[0][2],
  cara6[1][0],
  cara6[1][2],
  cara6[2][0],
  cara6[2][1],
  cara6[2][2],

  ]

  cubo_tratamiento = crear_array_de_tratamiento(cubo.get_estado() ,fichas)
  # print(cubo_tratamiento)
  cubo.set_estado(cubo_tratamiento)
  movimientos = [permutaciones.U , permutaciones.U_PRIMA]

  return busqueda_amplitud_con_nodos(cubo, varificar_paso_4, movimientos, funcion_h_paso4, estados_visitados)



def resolver_paso5(cubo, movimientos, estados_visitados):
  movimientos = [permutaciones.U , permutaciones.U_PRIMA]
  # print(cubo.get_estado())
  return busqueda_amplitud_con_nodos(cubo, varificar_paso_5, movimientos, funcion_h_paso5, estados_visitados)


