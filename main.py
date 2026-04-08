from clases import Tablero
from funciones import pedir_coordenadas, validar_coordenadas, mostrar_tablero


def main():
    """Ejecuta una prueba básica de integración del proyecto."""
    tablero_jugador = Tablero("Jugador")

    print("Bienvenido a Hundir la Flota")
    print("Tablero inicial:\n")

    mostrar_tablero(tablero_jugador)

    fila, col = pedir_coordenadas()

    if validar_coordenadas(fila, col):
        print(f"\nCoordenadas válidas: ({fila}, {col})")
    else:
        print("\nCoordenadas inválidas")


if __name__ == "__main__":
    main()