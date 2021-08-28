class Punto:
  def __init__(self, x=0, y=0):
    """Define las coordenas x e y"""
    self.x = x
    self.y = y

  def __str__(self):
    """Muestra el punto como un par ordenado"""
    return "(" + str(self.x) + ", " + str(self.y) + ")"

  def distancia(self, otra_cordenada):
    x_diff = (self.x - otra_cordenada.x)**2
    y_diff = (self.y - otra_cordenada.y)**2

    return (x_diff + y_diff)**0.5

p1 = Punto()
p2 = Punto(3, 4)

print(p1.distancia(p2))




# print('El los nodos son: ', nodos)

# class Puntos:
#   def __init__(self, numero_de_nodos):
#     self.numero_nodos = numero_de_nodos

#   def ingresar_nodos(self):
#     for i in range(self.numero_nodos):
#       print(i)
#       nodos = []
#       x = int(input('x --> '))
#       y = int(input('y --> '))




# p = Puntos(2)
# p.ingresar_nodos()