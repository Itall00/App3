from funciones import *
from Example import *

def main():
    paths = []
    matriz = loadMatrix()

    entrada = buscarEntrada(matriz, 0)
    salida = buscarSalida(matriz,0)

    N = len(matriz)

    maze = np.array(matriz)
    # print(matriz)

    maze[maze == 1] = 2
    maze[maze == 0] = 1
    maze[maze == 2] = 0
    print(maze)
    # Start point and destination
    source = (entrada, 0)  # top left corner
    destination = (salida, N-1)  # bottom right corner

    # Find all paths
    paths = find_paths(maze, source, destination)



    print(paths)



if __name__ == "__main__":
    main()
