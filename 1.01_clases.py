# Programacion orientada a objetos en python.

# 1. Clases e instancias

# Creamos como un formulario, una plantilla, o base que es mi clase hotel
class Hotel():
  # ATRIBUTOS DE LA INSTANCIA, CARACTERISTICAS QUE TENDRAN LOS OBJETOS QUE CREEMOS
  def __init__(self, numero_max_huespedes, lugares_estacionamiento):
    self.numero_max_huespedes = numero_max_huespedes
    self.lugares_estacionamiento = lugares_estacionamiento
    self.huespedes = 0

  # MÉTODOS DE INSTANCIA
  def añadir_huespedes(self, cantidad_de_huespedes):
    self.huespedes += cantidad_de_huespedes       # Huespedes=0, luego se hace la operacion huespedes = huespedes + cantidad_de_huespedes

  def checkout(self, cantidad_de_huespedes):
    self.huespedes -= cantidad_de_huespedes       # huespedes = huespedes - cantidad_de_huespedes

  def ocupacion_total(self):
    return self.huespedes


# Generamos una instancia llamando al constructor

hotel_city = Hotel(numero_max_huespedes=50, lugares_estacionamiento=20)

print('El "Hotel city" tiene {} lugares para estacionarse.'.format(hotel_city.lugares_estacionamiento))
print('El "Hotel city" cuenta con {} unidades como limite de huespedes.'.format(hotel_city.numero_max_huespedes))

print()

# Generamos otra instacia, otro objeto con nuestra misma plantilla de base. Osea, Generamos otro hotel

holliday_inn = Hotel(numero_max_huespedes=100, lugares_estacionamiento=50)
print('El hotel "HOLLYDAY INN" tiene {} lugares para estacionarse.'.format(hotel_city.lugares_estacionamiento))
print('El Hotel "HOLLYDAY INN" cuenta con {} unidades como limite de huespedes.'.format(hotel_city.numero_max_huespedes))

print()

# usamos el objeto creado con la clase hotel, como base, y operamos sobre nuestro objeto

hotel_city = Hotel(50, 20)
entradas = hotel_city.añadir_huespedes(3)
salidas = hotel_city.checkout(1)
total = hotel_city.ocupacion_total()

print('El dia de hoy llegaron {} huespedes al hotel'.format(entradas))
print('Tambien hoy salieron {} huespedes del hotel'.format(salidas))
print(f'En total hay {total} huespedes')