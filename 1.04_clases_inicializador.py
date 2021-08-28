class Gato:
  def __init__(self, nombre, edad, genero, saludo='Hola'):
    # Nadie te lo indica pero el programa debe de llevar los argumentos predefinidos hasta el final de los argumentos
    self.saludo = saludo
    self.nombre = nombre
    self.edad = edad
    self.genero = genero

  def mostrar_informacion(self):
    print(f'{self.saludo} mi nombre es {self.nombre},\ny tengo {self.edad} años de edad, soy {self.genero}')

michi = Gato('Michi', 2, 'niña')
michi.mostrar_informacion()