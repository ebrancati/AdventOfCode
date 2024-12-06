def simulate_guard_path(map):
    """Simulates the guard's path and returns the set of visited positions."""

    directions = [('^', (-1, 0)), ('>', (0, 1)), ('v', (1, 0)), ('<', (0, -1))]
    guard_direction = 0
    
    # Troviamo la posizione iniziale della guardia e la sua direzione
    start_row, start_col = -1, -1
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == '^':  # La direzione iniziale è verso l'alto
                start_row, start_col = row, col
    
    # Inizializziamo la simulazione
    visitated = set()  # Per memorizzare le posizioni visitate come tuple (riga, colonna)
    row, col = start_row, start_col
    visitated.add((row, col))  # Partiamo segnando la posizione iniziale come visitata

    # Calcola la prima mossa in base alla direzione iniziale
    value = directions[guard_direction][1] 
    new_row = row + value[0]
    new_col = col + value[1]
    
    visitated.add((row, col))
    
    i = 0
    while True:
        print("["+str(row)+" "+str(col))
        i+=1

        # Controlliamo se la guardia esce dalla mappa
        if not (0 <= new_row  < len(map)) or not (0 <= new_col < len(map[0])):
            break

        # Verifichiamo se la nuova posizione è all'interno dei limiti e non è un ostacolo
        if (0 <= new_row  < len(map)) and (0 <= new_col < len(map[0])) and map[new_row][new_col] != '#':
            # Se è una mossa valida, aggiorniamo la posizione e segniamo come visitata
            row = new_row 
            col = new_col
            visitated.add((row, col))
        else:
            # Se la mossa non è valida, cambiamo direzione
            guard_direction = (guard_direction + 1) % 4  # Cambia la direzione ciclicamente (0-3)
   
        
        # Calcoliamo la nuova posizione con la direzione aggiornata
        value = directions[guard_direction][1] 
        new_row = row + value[0]
        new_col = col + value[1]



    # Restituiamo il numero di posizioni distinte visitate
    return len(visitated)

map = []
with open("input1.txt", 'r') as file:
    for row in file:
        map.append(row.strip())

# Simula il percorso della guardia
print(simulate_guard_path(map))