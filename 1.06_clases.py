class Automovil:

  def __init__(self, modelo, marca, color):
    self.modelo = modelo
    self.marca = marca
    self.color = color
    self._estado = 'En reposo'     #variable privada
    self._motor = Motor(cilindros=4)  #cuando alguien haga una instancia de "Automovil", se le agregará un motor

  def acelerar(self, tipo='Despacio'):
    if tipo == 'rapido':
      self._motor.inyecta_gasolina(10)
    else:
      self._motor.inyecta_gasolina(3)


class Motor:
  def __init__(self, cilindros, tipo='gasolina'):
    self.cilindros = cilindros
    self.tipo = tipo
    self._temperatura = 0

  def inyecta_gasolina(self, cantidad):
    pass