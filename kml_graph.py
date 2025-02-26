import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Funzione per generare un grafo casuale
def generate_random_graph(num_nodes, edge_prob):
    G = nx.erdos_renyi_graph(num_nodes, edge_prob)
    return G

# Funzione per la compressione (algoritmo di esempio, basato sulla riduzione dei nodi)
def kml_compression(graph):
    # Ad esempio, riduciamo il grafo rimuovendo nodi con un grado inferiore a una certa soglia
    nodes_to_remove = [node for node, degree in graph.degree() if degree < 2]
    graph.remove_nodes_from(nodes_to_remove)
    return graph

# Funzione per visualizzare un grafo
def plot_graph(graph, title="Grafo"):
    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(graph)  # Layout per una visualizzazione interessante
    nx.draw(graph, pos, with_labels=True, node_color="skyblue", node_size=3000, edge_color="gray", width=1, alpha=0.7)
    plt.title(title)
    plt.show()

# Algoritmo di compressione KML-Compression che sfrutta i grafi
def main():
    # Parametri per il grafo (numero di nodi e probabilità di connessione tra di essi)
    num_nodes = 20
    edge_prob = 0.3

    # Generazione del grafo casuale
    G = generate_random_graph(num_nodes, edge_prob)

    # Visualizzazione del grafo originale
    plot_graph(G, "Grafo Originale")

    # Applicazione dell'algoritmo di compressione KML-Compression
    compressed_graph = kml_compression(G)

    # Visualizzazione del grafo compresso
    plot_graph(compressed_graph, "Grafo Compressed")

    # Stampa delle informazioni sul grafo compresso
    print("Numero di nodi nel grafo originale:", num_nodes)
    print("Numero di nodi nel grafo compresso:", len(compressed_graph.nodes))
    print("Numero di archi nel grafo compresso:", len(compressed_graph.edges))

if __name__ == "__main__":
    main()
