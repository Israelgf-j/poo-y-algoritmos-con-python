from random import randint

def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


if __name__ == '__main__':

    tamanio_lista = int(input('De que tamanio será la lista: '))

    Mylista = [randint(0, 100) for i in range(tamanio_lista)]

    print()

    print(Mylista)

    lista_ordenada = ordenamiento_burbuja(Mylista)
    print(lista_ordenada)