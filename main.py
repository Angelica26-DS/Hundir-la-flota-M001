"""
Módulo principal del juego Hundir la Flota.

Este archivo integra la lógica del juego, la visualización del tablero
y la interacción con el usuario.
"""

from clases import Tablero
from funciones import (
    pedir_coordenadas,
    disparar,
    comprobar_victoria,
    disparo_aleatorio_maquina
)
from visualizacion import mostrar_tablero_visual
from variables import BARCO


def main():
    """
    Ejecuta el flujo principal del juego Hundir la Flota.

    Se encarga de:
    - mostrar la bienvenida y reglas
    - crear los tableros
    - colocar barcos de prueba para la demo
    - gestionar los turnos del jugador y de la máquina
    - mostrar el estado del juego
    - comprobar la victoria

    Para simplificar la demo, los barcos se colocan manualmente
    en este archivo.
    """
    print("=" * 40)
    print("      BIENVENIDO A HUNDIR LA FLOTA")
    print("=" * 40)

    print()
    print("¿Cómo te llamas?")
    nombre = input("👉 ").strip().capitalize()

    print()
    print("¡Vamos a jugar, " + nombre + "! 🚀")

    print()
    print("Leyenda:")
    print("O → Barco")
    print("X → Impacto")
    print("- → Fallo")
    print(". → Agua")

    print()
    print("Reglas:")
    print("- Introduce fila y columna para disparar")
    print("- El tablero se actualiza con cada turno")
    print("- Gana quien destruya todos los barcos")

    print()
    input("Presiona Enter para comenzar el juego...")

    # Crear tablero del jugador y tablero de la máquina
    jugador = Tablero("Jugador")
    maquina = Tablero("Máquina")

    # Colocación manual de barcos para simplificar la demo
    maquina.tablero[0, 0] = BARCO
    maquina.tablero[1, 1] = BARCO

    jugador.tablero[2, 2] = BARCO
    jugador.tablero[3, 3] = BARCO

    turno = 0

    # Bucle principal del juego: controla turnos y flujo general
    while True:
        print()
        print("=" * 40)
        print("TU TABLERO".center(40))
        print("=" * 40)
        mostrar_tablero_visual(jugador.tablero)

        print()
        print("🎯 Tu turno")
        fila, col = pedir_coordenadas()

        resultado = disparar(maquina, fila, col)

        if resultado is True:
            print("🎉 ¡Ole " + nombre + "! Acertaste 💥 (" + str(fila) + ", " + str(col) + ")")
        elif resultado is False:
            print("😅 Ups " + nombre + ", fallaste 🌊 (" + str(fila) + ", " + str(col) + ")")
        else:
            print("⚠️ Ya habías disparado ahí")

        print()
        input("Presiona Enter para ver el tablero enemigo...")

        print()
        print("=" * 40)
        print("TABLERO ENEMIGO".center(40))
        print("=" * 40)
        mostrar_tablero_visual(maquina.tablero)

        if comprobar_victoria(maquina):
            print()
            print("🏆 ¡Ganaste, " + nombre + "!")
            break

        print()
        print("🤖 Turno de la máquina")
        fila_m, col_m = disparo_aleatorio_maquina(jugador)

        resultado_m = disparar(jugador, fila_m, col_m)

        if resultado_m is True:
            print("🤖🎯 ¡Ole! La máquina acertó 💥 (" + str(fila_m) + ", " + str(col_m) + ")")
        elif resultado_m is False:
            print("🤖😅 Ups, la máquina falló 🌊 (" + str(fila_m) + ", " + str(col_m) + ")")

        print()
        input("Presiona Enter para continuar...")

        if comprobar_victoria(jugador):
            print()
            print("💀 La máquina ha ganado")
            break

        turno += 1

        # Límite de turnos para que la demo no se alargue demasiado
        if turno >= 6:
            print()
            print("⏹ Fin de demo")
            print("Gracias por jugar a Hundir la Flota")
            break


if __name__ == "__main__":
    main()