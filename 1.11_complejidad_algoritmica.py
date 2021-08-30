import time, sys

def run():


    def factorial(n):
        respuesta = 1

        while n > 1:
            respuesta *= n
            n -= 1

        return respuesta


    def factorial_r(n):
        if n == 1:
            return 1

        return n * factorial_r(n - 1)


    sys.setrecursionlimit(100000)

    n = 90000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    print('Segunda funcion')

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)




if __name__ == '__main__':
    run()