import numpy as np

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
# Añadir la carpeta anterior a sys.path



from src import permutaciones
from src.libs.cubo.matriz import matriz_cubo

movimientos = [
      permutaciones.R,
      permutaciones.L,
      permutaciones.F,
      permutaciones.B,
      
  ]


aristas = {
    "az": [
        {"a": ["1-az", "7-a"]},
        {"n": ["3-az", "5-n"]},
        {"r": ["5-az", "3-r"]},
        {"b": ["7-az", "1-b"]}
    ],
    "r": [
        {"a": ["1-r", "5-a"]},
        {"b": ["7-r", "5-b"]}
    ],
    "n": [
        {"a": ["1-n", "3-a"]},
        {"b": ["7-n", "3-b"]}
    ],
    "v": [
        {"a": ["1-v", "1-a"]},
        {"r": ["3-v", "5-r"]},
        {"n": ["5-v", "3-n"]},
        {"b": ["7-v", "7-b"]}
    ]
}

esquinas_uno= [
  [["az","0-az"], ["a","6-a"] , ["n","2-n"]],
  [["az","2-az"], ["r","0-r"] , ["a","8-a"]],
  [["az","6-az"], ["n","8-n"] , ["b","0-b"]],
  [["az","8-az"], ["b","2-b"] , ["r","6-r"]],
  [["v","0-v"], ["a","2-a"] , ["r","2-r"]],
  [["v","2-v"], ["n","0-n"] , ["a","0-a"]],
  [["v","6-v"], ["r","8-r"] , ["b","8-b"]],
  [["v","8-v"], ["b","6-b"] , ["n","6-n"]],
]

esquinas_dos = [
  [["az","0-az"], ["a","6-a"] , ["n","2-n"]],
  [["az","2-az"], ["r","0-r"] , ["a","8-a"]],
  [["az","6-az"], ["n","8-n"] , ["b","0-b"]],
  [["az","8-az"], ["b","2-b"] , ["r","6-r"]],
  [["v","0-v"], ["a","2-a"] , ["r","2-r"]],
  [["v","2-v"], ["n","0-n"] , ["a","0-a"]],
  [["v","6-v"], ["r","8-r"] , ["b","8-b"]],
  [["v","8-v"], ["b","6-b"] , ["n","6-n"]],

]

def obtener_cordenadas( aristas, clave , subclave):
  if clave in aristas :
        for dic in aristas[clave]:
            if subclave in dic:
                return dic[subclave]
  if subclave in aristas:
        for dic in aristas[subclave]:
            if clave in dic:
                return dic[clave][::-1]
  
  print(clave , subclave)


def preparar_cubo(cubo_inicial):

  cubo_inicial = np.array(cubo_inicial , dtype='U10')

  cubo_inicial = cubo_inicial.reshape(6,3,3)



  for i in range(6):
    cubo_inicial[i][1][1] = str('4') + "-"+str(cubo_inicial[i][1][1]) 

  for i in range(4):
        clave = cubo_inicial[0][0][1]
        subclave = cubo_inicial[4][2][1]

        cordenadas_color = obtener_cordenadas(aristas , clave, subclave)
     

        cubo_inicial[0][0][1] = str(cordenadas_color[0])
        cubo_inicial[4][2][1] =  str(cordenadas_color[1])
      
        cubo_inicial = permutaciones.F(cubo_inicial)


  for i in range(2):
        clave = cubo_inicial[1][0][1]
        subclave = cubo_inicial[4][1][2]

        cordenadas_color = obtener_cordenadas(aristas , clave, subclave)
     
        # print(cordenadas_color)
        cubo_inicial[1][0][1] = str(cordenadas_color[0])
        cubo_inicial[4][1][2] =  str(cordenadas_color[1])
      
        cubo_inicial = permutaciones.R(cubo_inicial)
        cubo_inicial = permutaciones.R(cubo_inicial)
  print("a")

  for i in range(2):
        clave = cubo_inicial[3][0][1]
        subclave = cubo_inicial[4][1][0]


        cordenadas_color = obtener_cordenadas(aristas , clave, subclave)
        print("b")
        
        print(cordenadas_color)
        cubo_inicial[3][0][1] = str(cordenadas_color[0])
        print("c")
        cubo_inicial[4][1][0] =  str(cordenadas_color[1])

      
        cubo_inicial = permutaciones.L(cubo_inicial)
        cubo_inicial = permutaciones.L(cubo_inicial)

  print("d")

  for i in range(4):
        clave = cubo_inicial[2][0][1]
        subclave = cubo_inicial[4][0][1]

        cordenadas_color = obtener_cordenadas(aristas , clave, subclave)
     
        # print(cordenadas_color)
        cubo_inicial[2][0][1] = str(cordenadas_color[0])
        cubo_inicial[4][0][1] =  str(cordenadas_color[1])
      
        cubo_inicial = permutaciones.B(cubo_inicial)


  for i in range(4):
    clave = cubo_inicial[0][0][0]
    subclave_uno = cubo_inicial[4][2][0]
    subclave_dos = cubo_inicial[3][0][2]

    for esquina in esquinas_uno:
      for j in range (4):
       


        if esquina[0][0] == clave and esquina[1][0] == subclave_uno and esquina[2][0] == subclave_dos:
          cubo_inicial[0][0][0] = esquina[0][1]
          cubo_inicial[4][2][0] = esquina[1][1]
          cubo_inicial[3][0][2] = esquina[2][1]

          # print("*******************")

          # print(f"{clave} - {subclave_uno} - {subclave_dos}")
          # print("----")

          # print(f"{esquina[0][0]} - {clave}")
          # print(f"{esquina[1][0]} - {subclave_uno}")
          # print(f"{esquina[2][0]} - {subclave_dos}")
          # print("*******************")
          break


        valor = esquina[0]

        esquina[0]= esquina[2]
        esquina[2] = esquina[1]
        esquina[1]=valor


    cubo_inicial = permutaciones.F(cubo_inicial)
        

  for i in range(4):
    clave = cubo_inicial[2][0][0]
    subclave_uno = cubo_inicial[4][0][2]
    subclave_dos = cubo_inicial[1][0][2]

    for esquina in esquinas_dos:
      for j in range (4):
       


        if esquina[0][0] == clave and esquina[1][0] == subclave_uno and esquina[2][0] == subclave_dos:
          cubo_inicial[2][0][0]= esquina[0][1]
          cubo_inicial[4][0][2] = esquina[1][1]
          cubo_inicial[1][0][2] = esquina[2][1]

          # print("*******************")

          # print(f"{clave} - {subclave_uno} - {subclave_dos}")
          # print("----")

          # print(f"{esquina[0][0]} - {clave}")
          # print(f"{esquina[1][0]} - {subclave_uno}")
          # print(f"{esquina[2][0]} - {subclave_dos}")
          # print("*******************")
          break


        valor = esquina[0]

        esquina[0]= esquina[2]
        esquina[2] = esquina[1]
        esquina[1]=valor


    cubo_inicial = permutaciones.B(cubo_inicial)
  
  print(cubo_inicial)
  return cubo_inicial.ravel()

  
  

# preparar_cubo(matriz_cubo)