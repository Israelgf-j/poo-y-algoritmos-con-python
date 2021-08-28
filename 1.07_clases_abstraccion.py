# Abstraccion:

class Lavadora:

  def __init__(self):
    pass

  def lavar(self, temperatura='caliente'):
    self._llenar_el_tanque_de_agua(temperatura)
    self._anadir_jabon()
    self._lavar()
    self._centrigugar()

  def _llenar_el_tanque_de_agua(self, temperatura):
    print(f'llenando el tanque de agua {temperatura}.')

  def _anadir_jabon(self):
    print('Anadiendo jabon')

  def _lavar(self):
    print('Lavando la ropa')

  def _centrigugar(self):
    print('Centrifugando la ropa')


if __name__=='__main__':
  lavadora = Lavadora()
  lavadora.lavar()