import random
import numpy as np
from variables import FILAS, COLUMNAS, AGUA, BARCO, TOCADO, FALLO

def colocar_barcos_aleatorios(tablero, lista_esloras):
    """Coloca una lista de barcos de forma aleatoria en el tablero.

    Itera sobre una lista de tamaños de barcos (esloras), elige unas 
    coordenadas y orientación aleatorias, comprueba que el barco cabe 
    y no choca con otros usando slicing de numpy, y lo coloca.

    Args:
        tablero (Tablero): Objeto Tablero donde se colocarán los barcos.
        lista_esloras (list): Lista de enteros donde cada número representa 
            el tamaño de un barco (ej. [4, 3, 3, 2, 2, 1]).
    """
    for eslora in lista_esloras:
        colocado = False
        
        while not colocado:
            fila = random.randint(0, FILAS - 1)
            col = random.randint(0, COLUMNAS - 1)
            orientacion = random.choice(['H', 'V']) # H = Horizontal, V = Vertical
            
            if orientacion == 'H':
                # Comprobamos que cabe y que todas las celdas son AGUA
                if col + eslora <= COLUMNAS and np.all(tablero.tablero[fila, col:col+eslora] == AGUA):
                    tablero.tablero[fila, col:col+eslora] = BARCO
                    colocado = True
                        
            elif orientacion == 'V':
                # Comprobamos que cabe y que todas las celdas son AGUA
                if fila + eslora <= FILAS and np.all(tablero.tablero[fila:fila+eslora, col] == AGUA):
                    tablero.tablero[fila:fila+eslora, col] = BARCO
                    colocado = True

def disparar(tablero, fila, col):
    """Realiza un disparo comprobando el contenido de la matriz.

    Revisa las coordenadas indicadas y actualiza la celda dependiendo de 
    si había un barco, si era agua, o si ya se había disparado ahí.

    Args:
        tablero (Tablero): El tablero sobre el que se va a efectuar el disparo.
        fila (int): El número de fila apuntado.
        col (int): El número de columna apuntado.

    Returns:
        bool: True si ha impactado en un barco. False en caso de agua o error.
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

    Pide por consola la fila y la columna, asegurándose de que el usuario 
    introduce números enteros válidos dentro de los límites del tablero.

    Returns:
        tuple: (fila, col) enteros que representan coordenadas válidas.
    """
    while True:
        try:
            fila = int(input(f"Elige fila (0-{FILAS-1}): "))
            col = int(input(f"Elige columna (0-{COLUMNAS-1}): "))
            
            if 0 <= fila < FILAS and 0 <= col < COLUMNAS:
                return fila, col
            else:
                print(f"Error: Debes introducir números entre 0 y {FILAS-1}.")
        except ValueError:
            print("Error: Introduce números enteros.")

def disparo_aleatorio_maquina():
    """Genera coordenadas aleatorias para el disparo de la máquina.

    Returns:
        tuple: (fila, col) enteros con las coordenadas para la máquina.
    """
    fila = random.randint(0, FILAS - 1)
    col = random.randint(0, COLUMNAS - 1)
    return fila, col

def comprobar_victoria(tablero):
    """Comprueba si se ha ganado la partida revisando el tablero.

    Args:
        tablero (Tablero): El objeto Tablero que se desea comprobar.

    Returns:
        bool: True si no queda ningún barco (victoria). False si quedan.
    """
    return not np.any(tablero.tablero == BARCO)