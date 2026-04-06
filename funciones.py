import random
import numpy as np
from variables import FILAS, COLUMNAS, AGUA, BARCO, TOCADO, FALLO

def colocar_barcos_aleatorios(tablero, lista_esloras):
    """Coloca una lista de barcos de forma aleatoria en el tablero.

    Itera sobre una lista de tamaños de barcos (esloras), elige unas
    coordenadas y orientación aleatorias, comprueba que el barco cabe
    y no choca con otros, y lo coloca en el tablero.

    Args:
        tablero (Tablero): Objeto Tablero donde se colocarán los barcos.
        lista_esloras (list): Lista de enteros donde cada número representa
            el tamaño de un barco (ej. [4, 3, 3, 2, 2, 1]).
    """
    for eslora in lista_esloras:
        colocado = False

        while not colocado:
            # 1. Generamos coordenadas y orientación aleatorias
            fila = random.randint(0, FILAS - 1)
            col = random.randint(0, COLUMNAS - 1)
            orientacion = random.choice(['H', 'V'])  # H = Horizontal, V = Vertical

            # 2. Comprobamos límites y colisiones
            if orientacion == 'H':
                # ¿Cabe horizontalmente sin salirse?
                if col + eslora <= COLUMNAS:
                    # ¿Están todas las celdas donde iría el barco llenas de AGUA?
                    if np.all(tablero.tablero[fila, col:col+eslora] == AGUA):
                        tablero.tablero[fila, col:col+eslora] = BARCO
                        colocado = True

            elif orientacion == 'V':
                # ¿Cabe verticalmente sin salirse?
                if fila + eslora <= FILAS:
                    # ¿Están todas las celdas llenas de AGUA?
                    if np.all(tablero.tablero[fila:fila+eslora, col] == AGUA):
                        tablero.tablero[fila:fila+eslora, col] = BARCO
                        colocado = True

def disparar(tablero, fila, col):
    """Aplica un disparo comprobando el contenido de la celda.

    Revisa las coordenadas indicadas en el tablero y actualiza la celda
    dependiendo de si había un barco, si era agua, o si ya se había
    disparado en esa posición anteriormente.

    Args:
        tablero (Tablero): El tablero sobre el que se va a efectuar el disparo.
        fila (int): El número de fila apuntado.
        col (int): El número de columna apuntado.

    Returns:
        bool: True si ha impactado en un barco no tocado previamente.
        False en caso de impactar en agua o en una coordenada ya atacada.
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
        return False

def pedir_coordenadas_jugador():
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

            if 0 <= fila < FILAS and 0 <= col < COLUMNAS:
                return fila, col
            else:
                print(f"Error: Fila debe estar entre 0 y {FILAS-1}, columna entre 0 y {COLUMNAS-1}.")
        except ValueError:
            print("Error: Introduce números enteros.")

def disparo_aleatorio_maquina(tablero_jugador):
    """Genera coordenadas aleatorias válidas para el disparo de la máquina.

    Calcula una posición aleatoria para la fila y la columna utilizando los
    límites definidos en las variables globales FILAS y COLUMNAS, evitando
    repetir coordenadas donde ya se haya disparado anteriormente.

    Args:
        tablero_jugador (Tablero): El tablero del jugador, usado para evitar
            disparar a coordenadas ya atacadas.

    Returns:
        tuple: Una tupla (fila, col) de enteros (int, int) con las coordenadas
        donde disparará la máquina.
    """
    while True:
        fila = random.randint(0, FILAS - 1)
        col = random.randint(0, COLUMNAS - 1)
        celda = tablero_jugador.tablero[fila, col]
        if celda != TOCADO and celda != FALLO:
            return fila, col

def comprobar_victoria(tablero):
    """Comprueba si se ha ganado la partida revisando el tablero.

    Analiza la matriz del tablero buscando si queda alguna celda que contenga
    el símbolo del barco. Si no se encuentra ninguno, significa que toda la
    flota de ese tablero ha sido hundida.

    Args:
        tablero (Tablero): El objeto de la clase Tablero que se desea comprobar.

    Returns:
        bool: True si no queda ningún barco en el tablero (victoria).
        False si aún quedan barcos a flote.
    """
    return not np.any(tablero.tablero == BARCO)
