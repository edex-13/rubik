import numpy as np
def encontrar_fichas(cubo , fichas):

  indices = np.where(np.isin(cubo, fichas))

  return indices


