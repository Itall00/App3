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

def laberinto( ):