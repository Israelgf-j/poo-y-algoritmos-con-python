from random import randint


def busqueda_lineal(lista, objetivo):
    """
    Realiza una busqueda en forma lineal, elemento a elemento de una lista

    parameters:
        lista: Lista de donde se buscara el numero
        objetivo: numero a encontrar dentro de una lista

    returns:
        True: si ha encontrado el onjetivo en la lista
        False: si NO ha encontrado el onjetivo en la lista
    """

    match = False

    for elemento in lista:
        print('  Elemento: ', elemento)
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == '__main__':
    tamano_lista = int(input('De que tamanio sera la lista: '))
    objetivo = int(input('numero a encontrar: '))

    lista = [randint(0, 100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print('\n',lista)
    print(f'\nEl elemento {objetivo} {"ESTÁ" if encontrado else "NO ESTÁ"} en la lista')