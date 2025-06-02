grafo = {
    "A": ["B"],
    "B": ["A", "C", "D"],
    "C": ["B", "J", "F"],
    "D": ["B"],
    "F": ["C", "G"],
    "J": ["C"],
    "G": ['F']
}

pilha = ["G"]
visitados = []

while pilha:
    vertice_atual = pilha.pop()

    if vertice_atual not in visitados:
        visitados.append(vertice_atual)

        for vizinho in reversed(grafo.get(vertice_atual, [])):
            if vizinho not in visitados:
                pilha.append(vizinho)

print("Ordem de visitação:", visitados)