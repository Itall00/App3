from funciones import *


def main():
    lista = []
    matriz = loadMatrix()

    entrada = buscarEntrada(matriz, 0)
    aniadirBordes(lista, entrada)

    salida = buscarSalida(matriz,0)
    aniadirBordes(lista,salida)

    print(lista)



if __name__ == "__main__":
    main()
