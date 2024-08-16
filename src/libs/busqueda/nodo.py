
class Nodo:
  def __init__(self, estado, movimiento,estado_real , hijos=None, coste=None ):
    self.estado = estado
    self.estado_real = estado_real
    self.hijos = None
    self.padre = None
    self.movimiento_previsto= []
    self.contador_movimientos_previstos = 0
    self.movimiento_activo = False

    self.coste = coste
    self.catidad_movimientos = 0
    self.movimiento = movimiento
    self.set_hijos(hijos)


  def get_hijos(self):
    return self.hijos

  def set_hijos(self, hijos):
    self.hijos = hijos
    if self.hijos != None:
      for h in self.hijos:
        h.padre = self

  def get_movimiento(self):
    return self.movimiento

  def get_padre(self):
    return self.padre

  def set_padre(self, padre):
    self.padre = padre

  def get_movimiento_activo(self):
    return self.movimiento_activo

  def set_movimiento_activo(self, movimiento_activo):
    self.movimiento_activo = movimiento_activo

  def get_estado(self):
    return self.estado
  def get_estado_o(self):
    return self.estado_real

  def set_estado(self, estado):
    self.estado = estado

  def get_coste(self):
    return self.coste

  def set_coste(self, coste):
    self.coste = coste

  def get_cadena_de_movimientos(self):

    copia_nodo = self
    movimientos= []
    while copia_nodo.get_padre() != None:
        movimientos.append(copia_nodo.get_movimiento())
        copia_nodo = copia_nodo.get_padre()

    return movimientos
  
  def get_movimiento_previsto(self):
    return self.movimiento_previsto
  def set_movimiento_previsto(self, movimiento_previsto):
    self.movimiento_previsto = movimiento_previsto
  
  def get_contador_movimientos_previstos(self):
    return self.contador_movimientos_previstos

  def set_contador_movimientos_previstos(self, contador_movimientos_previstos):
    self.contador_movimientos_previstos = contador_movimientos_previstos
  
  def get_catidad_movimientos(self):
    return self.catidad_movimientos

  def set_catidad_movimientos(self, catidad_movimientos):
    self.catidad_movimientos = catidad_movimientos
  
  def __str__(self):
    return str(self.get_estado())
