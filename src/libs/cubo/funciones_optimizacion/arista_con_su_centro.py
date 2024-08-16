import numpy as np
def arista_con_su_centro(cara, arista , T = False):
 
  # print (arista)
  if (arista == cara[0][1] or arista == cara[1][0] or arista == cara[1][2] or arista == cara[2][1]):
    return True
  return False

"""
test:
"""
matriz_cubo = np.array([
    [
      ['0-b',  '1-b',  '2-b'],
      ['3-b',  '4-b',  '5-b'],
      ['6-b',  '7-b',  '8-b']
    ],
    [ 
      ['0-r', '1-r', '2-r'],
      ['3-r', '4-r', '5-r'],
      ['6-r', '7-r', '8-r']
    ],
    [ 
      ['0-a', '1-a', '2-a'],
      ['3-a', '4-a', '5-a'],
      ['6-a', '7-a', '8-a']
    ],
    [ 
      ['0-n', '1-n', '2-n'],
      ['3-n', '4-n', '5-n'],
      ['6-n', '7-n', '8-n']
    ],
    [ ['0-az', '1-az', '2-az'],
      ['3-az', '4-az', '5-az'],
      ['6-az', '7-az', '8-az']
    ],
    [ ['0-v', '1-v', '2-v'],
      ['3-v', '4-v', '5-v'],
      ['6-v', '7-v', '8-v']
    ]
])
cubo = np.array([
    [
      ['0-b',  '1-b',  '2-b'],
      ['3-b',  '4-b',  '5-b'],
      ['6-b',  '7-b',  '8-b']
    ],
    [ 
      ['0-r', '1-r', '2-r'],
      ['3-r', '4-r', '5-r'],
      ['6-r', '7-r', '8-r']
    ],
    [ 
      ['0-a', '1-f', '2-a'],
      ['1-o', '4-a', '5-a'],
      ['6-a', '7-a', '8-a']
    ],
    [ 
      ['0-n', '1-n', '2-n'],
      ['3-n', '4-n', '5-n'],
      ['6-n', '7-n', '8-n']
    ],
    [ ['0-az', '1-az', '2-az'],
      ['3-az', '4-az', '5-az'],
      ['6-az', '7-az', '8-az']
    ],
    [ ['0-v', '1-v', '2-v'],
      ['3-v', '4-v', '5-v'],
      ['6-v', '7-v', '8-v']
    ]
])

def verificar_vuelta(cubo , cubo_original):
  cara1 = cubo_original[0]
  if ((arista_con_su_centro(cubo[2], cara1[0][1] , True))):
    return False
  if ((arista_con_su_centro(cubo[2], cara1[1][0] , True))):
    return False
  if ((arista_con_su_centro(cubo[2], cara1[1][2] , True))):
    return False
  if ((arista_con_su_centro(cubo[2], cara1[2][1] , True))):
    return False
  return True


if not(verificar_vuelta(cubo, matriz_cubo)):
  print ("no esta bien")



"print (verificar_vuelta(cubo , matriz_cubo))"
"""

print (arista_con_su_centro(matriz_cubo, 0, '1-b'))
print (arista_con_su_centro(matriz_cubo, 0, '3-b'))
print (arista_con_su_centro(matriz_cubo, 0, '5-b'))
print (arista_con_su_centro(matriz_cubo, 0, '7-b')) 


def verificar_centros(cubo , matriz_cubo):

  cara_1 = cubo[1]
  cara_1_original = matriz_cubo[1]
  if (not(arista_con_su_centro( cara_1 , cara_1_original[1][0]))):
    return False
  cara_2 = cubo[3]
  cara_2_original = matriz_cubo[3]
  if (not(arista_con_su_centro( cara_2 , cara_2_original[1][2]))):
    return False
  cara_3 = cubo[4]
  cara_3_original = matriz_cubo[4]
  if (not(arista_con_su_centro( cara_3 , cara_3_original[2][1]))):
    return False
  cara_4 = cubo[5]
  cara_4_original = matriz_cubo[5]
  if (not(arista_con_su_centro( cara_4 , cara_4_original[0][1]))):
    return False
  

  return True
"""
