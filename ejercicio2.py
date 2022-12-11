from __future__ import annotations

solucion = []


def is_safe(tablero: list[list[int]], fila: int, columna: int) -> bool:
    """
    Esta función devuelve un valor booleano True si es seguro colocar una reina allí
    teniendo en cuenta el estado actual de la junta.
    Parámetros:
    tablero (matriz 2D): tablero
    fila, columna: coordenadas de la celda en un tablero
    Devoluciones :
    Valor booleano
    """
    for i in range(len(tablero)):
        if tablero[fila][i] == 1:
            return False
    for i in range(len(tablero)):
        if tablero[i][columna] == 1:
            return False
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    for i, j in zip(range(fila, -1, -1), range(columna, len(tablero))):
        if tablero[i][j] == 1:
            return False
    return True


def solve(tablero: list[list[int]], fila: int) -> bool:
    """
    Crea un árbol de espacio de estado y llama a la función segura hasta que recibe un
    Falso Booleano y termina esa rama y retrocede a la siguiente
    posible rama de solución.
    """
    if fila >= len(tablero):
        """
        Si el número de fila excede N, tenemos un tablero con una combinación exitosa
        y esa combinación se agrega a la lista de soluciones y se imprime el tablero.
        """
        solucion.append(tablero)
        printboard(tablero)
        print()
        return True
    for i in range(len(tablero)):
        """
        Para cada fila itera a través de cada columna para verificar si es factible
        coloca una reina allí.
        Si todas las combinaciones para esa rama en particular tienen éxito, el tablero es
        reinicializará para la siguiente combinación posible.
        """
        if is_safe(tablero, fila, i):
            tablero[fila][i] = 1
            solve(tablero, fila + 1)
            tablero[fila][i] = 0
    return False


def printboard(tablero: list[list[int]]) -> None:
    """
    Imprime los tableros que tienen una combinación exitosa.
    """
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


n=int(input("El numero de reinas"))
n = 15
tablero = [[0 for i in range(n)] for j in range(n)]
solve(tablero, 0)
print("El numero total de soluciones son :", len(solucion))

