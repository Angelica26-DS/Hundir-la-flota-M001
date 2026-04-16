from variables import FILAS, COLUMNAS
from variables import AGUA, BARCO, TOCADO, FALLO


#  MARKDOWN FUNCTION 

def tablero_a_markdown(tablero):

    columnas = "ABCDEFGHIJ"
    md = "## Tablero de juego\n\n"

 # Detect number of columns 
    num_columnas = tablero.shape[1] if hasattr(tablero, "shape") else len(tablero[0])

  # Headers

    md += "|   | " + " | ".join(columnas[:num_columnas]) + " |\n"
    md += "|---|" + "---|" * num_columnas + "\n"

# Rows
    for i, fila in enumerate(tablero):
        fila_md = f"| {i+1} | "

        # LOOP MUST BE INSIDE
        for celda in fila:            
            if celda == AGUA:
                simbolo = "."
            elif celda == BARCO:
                simbolo = "O"
            elif celda == TOCADO:
                simbolo = "X"
            elif celda == FALLO:
                simbolo = "-"
            else:
                simbolo = "?"

            fila_md += simbolo + " | "

        md += fila_md + "\n"

    # Legend
    md += "\n### Leyenda\n"
    md += "- O → Barco\n"
    md += "- X → Impacto\n"
    md += "- - → Fallo\n"
    md += "- . → Agua\n"

    return md


# CONSOLE FUNCTION VISUALISATIION 

def mostrar_tablero_visual(tablero):

    columnas = "ABCDEFGHIJ"
    num_columnas = tablero.shape[1] if hasattr(tablero, "shape") else len(tablero[0])

    print("\n   " + " ".join(columnas[:num_columnas]))

    for i, fila in enumerate(tablero):
        fila_str = f"{i+1:<2} "

        for celda in fila:
            
            if celda == AGUA:
                simbolo = "."
            elif celda == BARCO:
                simbolo = "O"
            elif celda == TOCADO:
                simbolo = "X"
            elif celda == FALLO:
                simbolo = "-"
            else:
                simbolo = "?"

            fila_str += simbolo + " "

        print(fila_str)

    print("\nLeyenda:")
    print("O → Barco")
    print("X → Impacto")
    print("- → Fallo")
    print(". → Agua\n")


# EXMP/TEST BLOCK 

if __name__ == "__main__":

    tablero_test = [
        [BARCO]*10,
        [FALLO]*10,
        [TOCADO]*10,
        [AGUA]*10,
        [AGUA]*10,
    ]

    mostrar_tablero(tablero_test)
    print(tablero_a_markdown(tablero_test))