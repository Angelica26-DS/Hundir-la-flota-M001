import numpy as np
from variables import FILAS, COLUMNAS, AGUA

class Tablero:
    def __init__(self, jugador):
        self.jugador = jugador
        self.tablero = np.full((FILAS, COLUMNAS), AGUA)

    def mostrar_tablero(self):
        print(self.tablero)


