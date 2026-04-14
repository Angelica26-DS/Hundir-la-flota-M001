import numpy as np
import random
from variables import FILAS, COLUMNAS, AGUA, BARCO, TOCADO, FALLO


def mostrar_tablero(tablero):
    """Muestra por consola el estado actual del tablero.

    Args:
        tablero (Tablero): El objeto Tablero que se desea mostrar.
    """
    print(tablero.tablero)


def validar_coordenadas(fila, col):
    """Comprueba si unas coordenadas están dentro de los límites del tablero.

    Args:
        fila (int): El número de fila a validar.
        col (int): El número de columna a validar.

    Returns:
        bool: True si las coordenadas son válidas. False si se salen del tablero.
    """
    return 0 <= fila < FILAS and 0 <= col < COLUMNAS


def pedir_coordenadas():
    """Solicita al jugador las coordenadas donde quiere disparar.

    Pide por consola la fila y la columna, asegurándose mediante un bucle de
    que el usuario introduce números enteros válidos y que se encuentran
    dentro de los límites del tablero.

    Returns:
        tuple: Una tupla (fila, col) de enteros (int, int) que representa
        las coordenadas válidas introducidas por el usuario.
    """
    while True:
        try:
            fila = int(input(f"Elige fila (0-{FILAS-1}): "))
            col = int(input(f"Elige columna (0-{COLUMNAS-1}): "))

            if validar_coordenadas(fila, col):
                return fila, col
            else:
                print(f"Error: Fila debe estar entre 0 y {FILAS-1}, columna entre 0 y {COLUMNAS-1}.")
        except ValueError:
            print("Error: Introduce números enteros.")

def colocar_barcos_aleatorios(tablero, lista_esloras):
    for eslora in lista_esloras:
        colocado = False
        while not colocado:
            fila = random.randint(0, FILAS - 1)
            col = random.randint(0, COLUMNAS - 1)
            orientacion = random.choice(['H', 'V'])
            if orientacion == 'H':
                if col + eslora <= COLUMNAS:
                    if np.all(tablero.tablero[fila, col:col+eslora] == AGUA):
                        tablero.tablero[fila, col:col+eslora] = BARCO
                        colocado = True
            elif orientacion == 'V':
                if fila + eslora <= FILAS:
                    if np.all(tablero.tablero[fila:fila+eslora, col] == AGUA):
                        tablero.tablero[fila:fila+eslora, col] = BARCO
                        colocado = True

def disparar(tablero, fila, col):
    """Procesa un disparo en el tablero y actualiza su estado.

    Verifica el contenido de la celda y lo sustituye por TOCADO o FALLO
    según corresponda, imprimiendo el resultado por consola.

    Args:
        tablero (Tablero): El tablero sobre el que se efectúa el disparo.
        fila (int): Fila elegida para el disparo.
        col (int): Columna elegida para el disparo.

    Returns:
        bool o None: True si hay impacto (BARCO), False si falla (AGUA),
                     y None si se dispara a una coordenada repetida.
    """
    celda = tablero.tablero[fila, col]
    if celda == BARCO:
        print("¡Tocado! 💥")
        tablero.tablero[fila, col] = TOCADO
        return True
    elif celda == AGUA:
        print("¡Agua! 💦")
        tablero.tablero[fila, col] = FALLO
        return False
    elif celda == TOCADO or celda == FALLO:
        print("Ya habías disparado a estas coordenadas.")
        return None

def disparo_aleatorio_maquina(tablero_jugador):
    """Genera coordenadas aleatorias válidas para el turno de la máquina.

    Busca de forma aleatoria en el tablero hasta encontrar una celda
    a la que la máquina no haya disparado previamente.

    Args:
        tablero_jugador (Tablero): El tablero del jugador humano.

    Returns:
        tuple: (fila, col) con las coordenadas válidas para el disparo.
    """
    while True:
        fila = random.randint(0, FILAS - 1)
        col = random.randint(0, COLUMNAS - 1)
        celda = tablero_jugador.tablero[fila, col]
        if celda != TOCADO and celda != FALLO:
            return fila, col

def comprobar_victoria(tablero):
    """Verifica si todos los barcos del tablero han sido hundidos.

    Comprueba en la matriz del tablero si queda alguna celda con el 
    estado BARCO.

    Args:
        tablero (Tablero): El tablero que se desea comprobar.

    Returns:
        bool: True si no quedan barcos (victoria), False en caso contrario.
    """
    return not np.any(tablero.tablero == BARCO)
