import random
import time

import multiprocessing
from flask import Flask, request, jsonify



from src.libs.cubo.matriz import matriz_cubo


from src.libs.busqueda.nodo import Nodo

from src.libs.cubo.resolver_pasos import resolver_paso1, resolver_paso2, resolver_paso3, resolver_paso4, resolver_paso5
from src import permutaciones
import numpy as np


inicio = time.time()



# IMPRIMIR LOS MOVIMIENTOS USADOS PARA LLEGAR A UN NODO
def obtener_movimientos(nodo):

  movimientos = nodo.get_cadena_de_movimientos()
  return movimientos[::-1]


def ejecutar_movimientos(nodo ):
  movimientos = obtener_movimientos(nodo)
  # print(movimientos)
  cantidad_m =len(movimientos)
  matriz = nodo.get_estado_o()

  for movimiento in movimientos:
    if 'CADENA-' in movimiento:
      cantidad_m -= 1

      partes = movimiento.split('-')
      lo_que_sigue_despues_del_guion = partes[1]
      lista = eval(lo_que_sigue_despues_del_guion)
      cantidad_m +=  len(lista)
      for sub_movimiento in lista:
        funcion = eval(f"permutaciones.{sub_movimiento}")
        matriz = funcion(matriz)

    else:
      funcion = eval(f"permutaciones.{movimiento}")
      matriz = funcion(matriz)

  nodo.set_catidad_movimientos(cantidad_m)
  

  return matriz


def solucionar_cubo_rubik(matriz_revuelta, arr_movimiento , paso = 4):

  cubo = Nodo(matriz_revuelta, "inicial" ,matriz_revuelta)


  resolver = [resolver_paso1, resolver_paso2, resolver_paso3,
              resolver_paso4, resolver_paso5]

  numero_de_pasos = paso
  cubo_actual = []

  cubo1 = cubo
  random.seed()  # Reiniciar la semilla aleatoria en cada proceso.
  movimientos_copia = movimientos.copy()  # Asegúrate de copiar la matriz correctamente.
  random.shuffle(movimientos_copia)
  for paso in range(0, numero_de_pasos+1):
    # print(f"--------------- PASO {paso+1} ---------------")
   


    cubo_actual = resolver[paso](
        cubo1,
        movimientos_copia,
        []
    )
    encontro_solucion = cubo_actual[0]
    matriz_cubo = cubo_actual[1]

    if not (encontro_solucion):
      print(f"NO SE ENCONTRO , PASO {paso + 1}")
      return None
    else:
      cubo = cubo_actual[1]
      print(F"SOLUCION ENCONTRADA {paso +1}")

      a = ejecutar_movimientos(matriz_cubo)
      # print(a)
      matriz_cubo.set_estado(a)
      cubo1 = matriz_cubo

  return cubo_actual
def wrapper(args):
    return solucionar_cubo_rubik(*args)



app = Flask(__name__)


def main(cubo):
  matriz_revuelta = np.array(cubo)
  matriz_revuelta = matriz_revuelta.reshape(6, 3, 3)
  matriz_revuelta = np.copy(matriz_revuelta)

  

  parametros = [(np.copy(matriz_revuelta), np.copy(movimientos)),
                (np.copy(matriz_revuelta), np.copy(movimientos)),
                (np.copy(matriz_revuelta), np.copy(movimientos)),
  ]
  soluciones = []
  longitudes = []
  pool = multiprocessing.Pool(3)
  resultados = pool.map(wrapper, parametros)
  pool.close()
  pool.join()
  for resultado in resultados:
        if resultado != None:
          soluciones.append(obtener_movimientos(resultado[1]))
          longitudes.append(resultado[1].get_catidad_movimientos())

  return [soluciones , longitudes]

@app.route('/api/endpoint', methods=['POST'])

def mi_punto_de_entrada():
    try:
        data = request.get_json()  # Obtén los datos JSON de la solicitud POST
        if not data:
            return jsonify({"error": "No se proporcionaron datos JSON"}), 400

        if "mi_array" in data and isinstance(data["mi_array"], list):
            mi_array = data["mi_array"]
            # Haz algo con el array, por ejemplo, imprímelo
            print(mi_array)
            [soluciones , longitudes]= main(mi_array)
            

            fin = time.time()
            tiempo_transcurrido = fin - inicio
            print(len(soluciones))
            print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")
            return  jsonify({'mi_array': soluciones , 'longitudes': longitudes})
        else:
            return jsonify({"error": "El parámetro 'mi_array' no es una lista válida"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
  
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
  app.run(debug=True)

  
  num_hilos = 6
  
  


