# Entendiendo el concepto de decorador

def funcion_decoradora(funcion):
  def wrapper():
    print('Este es el ultimo mensaje.....')

    funcion()
    print("Este es el primer mensaje")

  return wrapper()

def zumbido():
  print('Buzzzzz')

zumbido = funcion_decoradora(zumbido)