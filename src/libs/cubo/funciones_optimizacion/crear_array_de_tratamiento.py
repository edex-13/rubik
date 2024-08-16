import numpy as np

from src.libs.cubo.funciones_optimizacion.encontrar_fichas import encontrar_fichas

def crear_array_de_tratamiento(matriz_cubo, elementos_a_mantener):
    centros = ['4-b' , '4-r' , '4-a' , '4-n' , '4-az' , '4-v']
    # unir elementos a manter a centros
    elementos_a_mantener = np.append(elementos_a_mantener, centros)
    nuevo_array = np.full_like(matriz_cubo, '*',)
    
    indices = encontrar_fichas(matriz_cubo, elementos_a_mantener)
    
    nuevo_array[indices] = matriz_cubo[indices]
    
    return nuevo_array





