import random
import time
import ast

import multiprocessing
from flask import Flask, request, jsonify


from flask_cors import CORS
from src.libs.cubo.matriz import matriz_cubo


from src.libs.busqueda.nodo import Nodo
from src.libs.cubo.crear_cubo import preparar_cubo

from src.libs.cubo.resolver_pasos import resolver_paso1, resolver_paso2, resolver_paso3, resolver_paso4, resolver_paso5
from src import permutaciones
import numpy as np
import json
import re



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



def optimizar_movimientos(movimientos):
    print(movimientos)
    def son_opuestos(m1, m2):
        # Asumimos que m1 y m2 son cadenas, no listas
        return (m1.replace('_PRIMA', '') == m2.replace('_PRIMA', '') and
                ('_PRIMA' in m1) != ('_PRIMA' in m2))

    def son_caras_opuestas(m1, m2):
        caras_opuestas = {'U': 'D', 'L': 'R', 'F': 'B'}
        c1 = m1[0]
        c2 = m2[0]
        return c2 == caras_opuestas.get(c1) or c1 == caras_opuestas.get(c2)

    optimizado = []
    i = 0
    while i < len(movimientos):
        # Caso 1: Movimiento seguido de su inverso
        if i+1 < len(movimientos) and son_opuestos(movimientos[i], movimientos[i+1]):
            i += 2
        # Caso 2: Tres movimientos iguales
        elif i+2 < len(movimientos) and movimientos[i] == movimientos[i+1] == movimientos[i+2]:
            optimizado.append(movimientos[i].replace('_PRIMA', '') if '_PRIMA' in movimientos[i] else f"{movimientos[i]}_PRIMA")
            i += 3
        # Caso 3: Cuatro movimientos iguales
        elif i+3 < len(movimientos) and movimientos[i] == movimientos[i+1] == movimientos[i+2] == movimientos[i+3]:
            i += 4
        
        # Caso 5: Movimientos de caras opuestas pueden intercambiarse
        elif i+1 < len(movimientos) and son_caras_opuestas(movimientos[i], movimientos[i+1]):
            optimizado.extend([movimientos[i+1], movimientos[i]])
            i += 2
    
        else:
            optimizado.append(movimientos[i])
            i += 1
    return optimizado

def optimizar_completamente(movimientos):
    # while True:
        return optimizar_movimientos(movimientos)
        # if optimizado == movimientos:
        #     return optimizado
        # movimientos = optimizado

def quitar_cadenas(soluciones):

  total_solucion = []
  n_menor = 99999999999999
  for solucion in soluciones:
    resultado = []

    for movimiento in solucion:
        if "CADENA" in movimiento:
            # Extraemos la lista de la cadena usando ast.literal_eval
            cadena = movimiento.split("CADENA-")[1]
            elementos = ast.literal_eval(cadena)
            resultado.extend(elementos)
        else:
            resultado.append(movimiento)

    solucion_final = optimizar_completamente(list(resultado))

    if  len(solucion_final) < n_menor:
      n_menor = len(solucion_final)
      total_solucion = [ solucion_final, len(solucion_final)]




  return total_solucion


app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'uploads'
cors = CORS(app, resources={r"/api/crearcubo": {"origins": "*"}})


def main(cubo):
  matriz_revuelta = np.array(cubo)
  matriz_revuelta = matriz_revuelta.reshape(6, 3, 3)
  matriz_revuelta = np.copy(matriz_revuelta)

  

  parametros = [(np.copy(matriz_revuelta), np.copy(movimientos)),
                (np.copy(matriz_revuelta), np.copy(movimientos)),
                (np.copy(matriz_revuelta), np.copy(movimientos)),
                (np.copy(matriz_revuelta), np.copy(movimientos)),
                
  ]
  soluciones = []
  longitudes = []
  pool = multiprocessing.Pool(4)
  resultados = pool.map(wrapper, parametros)
  pool.close()
  pool.join()
  for resultado in resultados:
        if resultado != None:
          soluciones.append(obtener_movimientos(resultado[1]))
          longitudes.append(resultado[1].get_catidad_movimientos())

  
 
  return  quitar_cadenas(soluciones)

@app.route('/api/solucionarcubo', methods=['POST'])

def solucionar_cubo():
    try:
        data = request.get_json()  # Obtén los datos JSON de la solicitud POST
        if not data:
            return jsonify({"error": "No se proporcionaron datos JSON"}), 400

        if "mi_array" in data and isinstance(data["mi_array"], list):
            mi_array = data["mi_array"]
            # Haz algo con el array, por ejemplo, imprímelo
            print(mi_array)
            [soluciones]= main(mi_array)
            

            fin = time.time()
            tiempo_transcurrido = fin - inicio
            print(len(soluciones))
            print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")
            return  jsonify({'mi_array': soluciones , 'longitudes': longitudes})
        else:
            return jsonify({"error": "El parámetro 'mi_array' no es una lista válida"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/crearcubo', methods=['POST'])

def crear_cubo():
    try:
        data = request.get_json()  # Obtén los datos JSON de la solicitud POST
        if not data:
            return jsonify({"error": "No se proporcionaron datos JSON"}), 400
        

        if "mi_array" in data:
            mi_array = data["mi_array"]
            

            cubo_preparado = preparar_cubo(mi_array)
            estados_cubo = []
            cubo_original = np.copy(cubo_preparado)
            solucion = main(cubo_preparado)
            for movimiento in solucion[0]:
              
              funcion = eval(f"permutaciones.{movimiento}")
              print(funcion)

              cubo_original = funcion(cubo_original)
              modified_array = np.array([remove_number_and_dash(e) for e in np.copy(cubo_original).ravel()])
              modified_array = modified_array.reshape(6,9)

              estados_cubo.append([modified_array.tolist() , movimiento])


            
            
            
            print(estados_cubo)
            return  jsonify({'mi_array':  estados_cubo })

        else:
            return jsonify({"error": "El parámetro 'mi_array' no es una lista válida"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def remove_number_and_dash(element):
    return re.sub(r'^\d+-', '', element)

# Aplicar la función a cada elemento del array
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

  movimientos_lista = {
      "R": permutaciones.R,
      "U": permutaciones.U,
      "L": permutaciones.L,
      "F": permutaciones.F,
      "D": permutaciones.D,
      "B": permutaciones.B,
      "R_PRIMA": permutaciones.R_PRIMA,
      "U_PRIMA": permutaciones.U_PRIMA,
      "L_PRIMA": permutaciones.L_PRIMA,
      "F_PRIMA": permutaciones.F_PRIMA,
      "D_PRIMA": permutaciones.D_PRIMA,
      "B_PRIMA": permutaciones.B_PRIMA,
  }
  app.run(debug=True)

  
  num_hilos = 6
  
  


