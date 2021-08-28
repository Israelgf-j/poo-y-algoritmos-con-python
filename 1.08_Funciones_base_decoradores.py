# esta es una funcion cualquiera, ya la sabes leer:

def elevar_al_cubo(numero):
  return numero * numero * numero

print(elevar_al_cubo(3))

print()

def presentarse(nombre):
  return f'Me llamo {nombre}'

def estudiamos_juntos(nombre):
  return f'Hey {nombre}, estudiamos juntos'

def come_funciones(funcion_entrada):
  return funcion_entrada('David')

print(come_funciones(presentarse))
print(come_funciones(estudiamos_juntos))

# es el anidamiento de funciones, como cuando en la funcion for, usas la funcion len o range
