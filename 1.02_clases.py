# Práctica con clases.

class Persona:
  nombre = ''
  apellido = ''
  escuela = ''
  edad = int()

  def print_name(self):
    print(self.name)

  def print_apellido(self):
    print(self.apellido)

  def print_edad(self):
    print(self.edad)

  def print_informacion(self):
    print(self.name)
    print(self.apellido)
    print(self.edad)


print('Este es mi objeto, se llama jorge: \n')
jorge = Persona()
jorge.name = 'Jorge'
jorge.apellido = 'Gonzalez'
jorge.edad = 25
jorge.print_name()
jorge.print_apellido()
jorge.print_edad()

print()

Israel = Persona()
Israel.name = 'Israel'
Israel.apellido = 'Hernandez'
Israel.edad = 13
Israel.print_name()
Israel.print_apellido()
Israel.print_edad()
print('Este es mi objeto, se llama israel: \n')

print()

print('Este es mi objeto, se llama jenifer: \n')
Jenifer = Persona()
Jenifer.name = 'Jenifer'
Jenifer.apellido = 'Garcia'
Jenifer.edad = 19
Jenifer.print_name()
Jenifer.print_apellido()
Jenifer.print_edad()

print()

print('Este es mi objeto, se llama oscar: \n')
Oscar = Persona()
Oscar.name = 'Oscar'
Oscar.apellido = 'Villanueva'
Oscar.edad = 47
Oscar.print_informacion()