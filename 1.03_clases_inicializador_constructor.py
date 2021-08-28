# Hay una manera mas elegante de dar atributos a una clase: Metodo inicializador:
print('Hay una manera mas elegante de dar atributos a una clase: Metodo inicializador:')

class Persona:
  def __init__(self, nombre, apellido, escuela, edad=None):
    self.nombre = nombre
    self.apellido = apellido
    self.escuela = escuela
    self.edad = edad

  def print_informacion(self):
    print('Hola, ni nombre es "{} {}" y estoy estudiando en "{}" y tengo "{} años de edad".'.format(self.nombre, self.apellido, self.escuela, self.edad))


print('Este es mi objeto:')
Fernanda = Persona('Fernanda', 'Alzati', 'Le pcelpe', 15)
Fernanda.print_informacion()

print()

print('Este es mi objeto:')
Gerardo = Persona('Gerardo', 'Robles', 'Justo Sierra')
Gerardo.print_informacion()