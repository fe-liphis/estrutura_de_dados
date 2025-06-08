from collections import deque 

grafo = {
    "A": ["B"],
    "B": ["A", "C", "D"],
    "C": ["B", "F", "J"],
    "D": ["B"],
    "F": ["C", "G"],
    "J": ["C"],
    "G": ['F']
}

fila = deque()
fila.append("A")
visitados = []

while fila:
    vertice_atual = fila.popleft()

    if vertice_atual not in visitados:
        visitados.append(vertice_atual)

        for vizinho in reversed(grafo.get(vertice_atual, [])):
            if vizinho not in visitados:
                fila.append(vizinho)

print("Ordem de visitação:", visitados)