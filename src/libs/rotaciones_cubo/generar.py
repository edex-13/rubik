from .transformaciones import girar_lado, girar_cara, mutar_cubo , rotar_cubo , rotar_inverso_cubo


def generar(tipo_de_rotacion, eje, cubo, sentido,numero_de_cara=0 ):
  cubo = cubo.reshape(6, 3, 3)
  if tipo_de_rotacion == 'horizontal':
    girar_lado(eje, cubo , sentido)

  elif tipo_de_rotacion == 'cara':
    girar_cara(numero_de_cara, cubo, sentido)

  elif tipo_de_rotacion == 'vertical':
    nuevo_cubo = mutar_cubo(cubo)
    nuevo_cubo = girar_lado(eje, nuevo_cubo, sentido)
    cubo = mutar_cubo(nuevo_cubo, True, cubo)

  elif tipo_de_rotacion == 'lateral':

    cubo = rotar_cubo(cubo)
    cubo = generar('vertical', eje , cubo , sentido)
    cubo = rotar_inverso_cubo(cubo)
  else:
    print("ERROR")
    return 0

  return cubo
