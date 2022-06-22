import numpy as np


def loadMatrix():  # cargo el archivo que contiene la matriz del laberinto
    matriz = np.loadtxt('input.txt', skiprows=0)
    return matriz


def buscarEntrada(matriz, contador):  # busco la entrada asumiendo que comenzara en el primer 0 de de la columna
    valor = matriz[contador][0]
    return contador if valor == 0 else buscarEntrada(matriz, contador + 1)


def buscarSalida(matriz, contador):
    valor = matriz[contador][-1]
    return contador if valor == 0 else buscarSalida(matriz, contador + 1)


def is_valid_cell(x, y, N):  # compruebo que la celda sea valida
    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    return True


def encontrar_patron(mat, inicio, final, visitada, path, paths):

    if inicio == final:
        paths.append(path[:])  # append copy of current path
        return

    # mark current cell as visited
    N = len(mat)
    x, y = inicio
    visitada[x][y] = 1

    # if current cell is a valid and open cell,
    if is_valid_cell(x, y, N) and mat[x][y]:
        # Using Breadth First Search on path extension in all direction

        if x + 1 < N and (not (visitada[x + 1][y] != 0)):  #me muevo a la derecha
            path.append((x + 1, y))
            encontrar_patron(mat, (x + 1, y), final, visitada, path, paths)
            path.pop()

        if x - 1 >= 0 and (not (visitada[x - 1][y] != 0)):  # me muevo a la izquierda
            path.append((x - 1, y))
            encontrar_patron(mat, (x - 1, y), final, visitada, path, paths)
            path.pop()

        if y + 1 < N and (not (visitada[x][y + 1] != 0)):  # me muevo hacia arriba
            path.append((x, y + 1))
            encontrar_patron(mat, (x, y + 1), final, visitada, path, paths)
            path.pop()

        if y - 1 >= 0 and (not (visitada[x][y - 1] != 0)): #me muevo hacia abajo
            path.append((x, y - 1))
            encontrar_patron(mat, (x, y - 1), final, visitada, path, paths)
            path.pop()

        # Unmark current cell as visited
    visitada[x][y] = 0

    return paths


def find_paths(mat, inicio, final):  # busca rutas

    N = len(mat)  # calculo el tamaño de la matriz de n*n

    # 2D matrix to keep track of cells involved in current path
    visitada = [[0] * N for _ in range(N)] """corregir esta parte"""

    path = [inicio]
    paths = []
    paths = encontrar_patron(mat, inicio, final, visitada, path, paths)

    return paths
