import networkx as nx
import matplotlib.pyplot as plt

GRAFO = nx.Graph()

arestas = [("A", "B"), ("B", "C"), ("B", "D"), ("C","J"), ("C", "F"), ("F", "G")]

GRAFO.add_edges_from(arestas)

plt.figure(figsize=(10,8))
nx.draw(GRAFO, with_labels=True, node_color="lightblue", node_size=700, font_size=12, edge_color="gray")
plt.title("Grafo não direcionado")
plt.show()