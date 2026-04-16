import numpy as np
from variables import FILAS, COLUMNAS, AGUA


class Tablero:
    def __init__(self, jugador):
        #Guardamos el nombre del jugador al que pertenece este tablero
        self.jugador = jugador
        #Creamos la matriz del tablero con numpy, rellenada completamente con AGUA
        self.tablero = np.full((FILAS, COLUMNAS), AGUA)

    def mostrar_tablero(self):
        # Imprimimos por consola el estado actual del tablero
        print(self.tablero)


