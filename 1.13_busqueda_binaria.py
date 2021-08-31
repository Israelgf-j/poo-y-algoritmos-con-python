from random import randint

def busqueda_binaria(lista, comienzo, final, objetivo, i = 0):

    i += 1

    print(f' --> buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')

    if comienzo > final:
        return (False, i)

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, i)

    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, i=i)

    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, i=i)


if __name__ == '__main__':
    tamano_lista = int(input('De que tamanio sera la lista: '))
    objetivo = int(input('numero a encontrar: '))

    print()

    lista = sorted([randint(0, 100) for i in range(tamano_lista)])

    (encontrado, i) = busqueda_binaria(lista, 0, len(lista), objetivo)

    print('\n',lista)
    print(f'\nEl elemento {objetivo} {"ESTÁ" if encontrado else "NO ESTÁ"} en la lista')
    print(f'Numero de iteracciones: {i}')