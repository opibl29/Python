
tablero = [" " for _ in range(9)]

def mostrar_tablero():
    print()
    print(tablero[0], "|", tablero[1], "|", tablero[2])
    print("--+---+--")
    print(tablero[3], "|", tablero[4], "|", tablero[5])
    print("--+---+--")
    print(tablero[6], "|", tablero[7], "|", tablero[8])
    print()


def hay_ganador(jugador):
    combinaciones = [
        (0,1,2), (3,4,5), (6,7,8),  
        (0,3,6), (1,4,7), (2,5,8), 
        (0,4,8), (2,4,6)           
    ]
    for a, b, c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c] == jugador:
            return True
    return False


jugador_actual = "X"

while True:
    mostrar_tablero()
    posicion = int(input(f"Jugador {jugador_actual}, elige una posición (1-9): ")) - 1

    if tablero[posicion] != " ":
        print(" Esa posición ya está ocupada. Intenta otra.")
        continue

    tablero[posicion] = jugador_actual

    if hay_ganador(jugador_actual):
        mostrar_tablero()
        print(f"¡Jugador {jugador_actual} ha ganado!")
        break

    if " " not in tablero:
        mostrar_tablero()
        print("¡Empate!")
        break

    if jugador_actual == "X":
        jugador_actual = "O"
    else:
        jugador_actual = "X"