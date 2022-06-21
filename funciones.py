import numpy as np


def loadMatrix():
    matriz = np.loadtxt('input.txt', skiprows=0)
    return matriz


def aniadirBordes(lista, indice):
    lista.append([indice, 0])
    return


def buscarEntrada(matriz, contador):
    valor = matriz[contador][0]
    return contador if valor == 0 else buscarEntrada(matriz, contador + 1)


def buscarSalida(matriz,contador):
    valor = matriz[contador][-1]
    return contador if valor == 0 else buscarSalida(matriz, contador + 1)

"""
def findPaths(matriz, path, i, j):

    M = len(matriz)
    N = len(matriz[0])
    visited = [[0] * N for _ in range(N)]
    if (i == M - 1 and j == N - 1):
        path.append(matriz[i][j])
        print(path)
        path.pop()
        return

    path.push()

    # move right
    if ((i >= 0 and i < M and j + 1 >= 0 and j + 1 < N)):
        findPaths(matriz, path, i, j + 1)


    #move down
    if ((i + 1 >= 0 and i + 1 < M and j >= 0 and j < N)):
        findPaths(matriz, path, i + 1, j)


    # backtrack: remove the current cell from the path
    path.pop()
"""

