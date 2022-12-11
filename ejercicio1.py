TableroAjedrez = [[1,2,3],[4,5,6], [7,8,9], [None, 0, None]]

def countMatrizElements(matriz):
 contador = 0
 for fila in range(len(matriz)):
  for columna in range (len(matriz[fila])):
      if matriz[fila][columna] != None:
          contador = contador + 1
 return contador

def horseValidMovementsAux(tablero, movimientos, inicio):
    if movimientos == 0:
        return 0
    for fila in range(len(tablero)):
        for columna in range (len(tablero[fila])):
            if(tablero[fila][columna] == inicio):
                if(fila==0 and columna == 0):
                   return 2+horseValidMovementsAux(tablero,movimientos-1,tablero[fila+1][columna+2])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila+2][columna+1])
                elif(fila==1 and columna == 0):
                    return 3+horseValidMovementsAux(tablero,movimientos-1,tablero[fila+1][columna+2])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila-1][columna+2])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila+2][columna+1])
                elif(fila==2 and columna == 0):
                    return 2+horseValidMovementsAux(tablero,movimientos-1,tablero[fila-1][columna+2])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila-2][columna+1])
                elif(fila== 3 and columna == 1):
                    return 2+horseValidMovementsAux(tablero,movimientos-1,tablero[fila-2][columna+1])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila-2][columna-1])
                elif(fila==0 and columna == 1):
                   return 2+horseValidMovementsAux(tablero,movimientos-1,tablero[fila+2][columna+1])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila+2][columna-1])
                elif(fila==1 and columna == 1):
                    return 0
                elif(fila==2 and columna == 1):
                    return 2+horseValidMovementsAux(tablero,movimientos-1,tablero[fila-2][columna+1])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila-2][columna-1])
                elif(fila==0 and columna == 2):
                   return 2+horseValidMovementsAux(tablero,movimientos-1,tablero[fila+2][columna-1])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila+1][columna-2])
                elif(fila==1 and columna == 2):
                    return 3+horseValidMovementsAux(tablero,movimientos-1,tablero[fila+2][columna-1])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila-1][columna-2])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila+1][columna-2])
                elif(fila==2 and columna == 2):
                    return 2+horseValidMovementsAux(tablero,movimientos-1,tablero[fila-2][columna-1])+horseValidMovementsAux(tablero,movimientos-1,tablero[fila-1][columna-2])
                                

def horseValidMovements(tablero, movimientos):
 contadormovimientos = 0
 for inicio in range(countMatrizElements(tablero)):
   contadormovimientos = contadormovimientos + horseValidMovementsAux(tablero, movimientos, inicio)
 return contadormovimientos

print(horseValidMovements(TableroAjedrez, 1))
