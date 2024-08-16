from .encontrar_fichas import encontrar_fichas
import numpy as np
def grupos(arista , cubo  , cara_ignorar = None , cara_busqueda = None):
  print(arista)
  print(cubo)
  n_grupos = 0
  indice = encontrar_fichas(cubo , arista)
  cara = cubo[indice[0][0]]
  if cara_ignorar != None:
    if indice[0][0] == cara_ignorar:
      return 0

  if cara_busqueda != None:
    print(indice[0][0] )
    if indice[0][0] != cara_busqueda:
      return 0
  print(cara)





  # obtener el indice de la arista en la cara
  indice_arista = np.where(cara == arista)
  indice_arista_1 = indice_arista[0][0]
  if indice_arista_1 == 0 or indice_arista_1 == 2:

    arista = arista.split('-')


    ficha_1 = cara[indice_arista_1][indice_arista[1][0] + 1]
    if ficha_1 != '*':
      ficha_1 = ficha_1.split('-')

      if ficha_1[1] == arista[1] and int(ficha_1[0]) - 1 == int(arista[0]):
          n_grupos += 1

    ficha_2 = cara[indice_arista_1][indice_arista[1][0] - 1]
    if ficha_2 != '*':
      ficha_2 = ficha_2.split('-')

      if ficha_2[1] == arista[1] and int(ficha_2[0]) + 1 == int(arista[0]):
          n_grupos += 1


  else:
    arista = arista.split('-')
    ficha_1 = cara[indice_arista_1 - 1][indice_arista[1][0]]
    if ficha_1 != '*':
      ficha_1 = ficha_1.split('-')

      if ficha_1[1] == arista[1] and int(ficha_1[0]) + 3 == int(arista[0]):
          n_grupos += 1


    ficha_2 = cara[indice_arista_1 + 1][indice_arista[1][0]]
    if ficha_2 != '*':
      ficha_2 = ficha_2.split('-')

      if ficha_2[1] == arista[1] and int(ficha_2[0]) - 3 == int(arista[0]):
          n_grupos += 1



  
  return n_grupos

  




matriz_cubo = np.array([
    [ ['*','*','*'],
      ['3-az', '4-az', '5-az'],
      ['6-az', '7-az', '8-az']
    ],
    [ 
      ['*','*','*'],
      ['3-r', '4-r', '5-r'],
      ['6-r', '7-r', '8-r']
    ],
    [ ['*','*','*'],
      ['3-v', '4-v', '5-v'],
      ['6-v', '7-v', '8-v']
    ],
    [ 
      ['*','*','*'],
      ['3-n', '4-n', '1-n'],
      ['6-n', '7-n', '8-n']
    ],
    [ 
      ['0-a', '1-a', '2-a'],
      ['3-a', '4-a', '5-a'],
      ['6-a', '5-n', '6-n']
    ],
    [
      ['0-b', '1-b', '2-b'],
      ['3-b', '4-b', '5-b'],
      ['6-b', '7-b', '8-b']
    ]
])


#grupos('3-b' , matriz_cubo)



def calcular_coste_grupos(cubo):
  coste = 0
  # coste += grupos('5-az', cubo , None , 4)
  # coste += grupos('3-az', cubo , None , 4)
  # coste += grupos('5-v', cubo , None , 4)
  # coste += grupos('7-v', cubo , None , 4)

  # coste += grupos('3-r', cubo , None , 4)
  # coste += grupos('5-r', cubo , None , 4)
  coste += grupos('5-n', cubo , None , 4)
  # coste += grupos('7-n', cubo , None , 4)
  return coste

# print(calcular_coste_grupos(matriz_cubo))
