import networkx as nx
import matplotlib.pyplot as plt


def basic_graph():
    graph = nx.Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'A', weight=10)
    graph.add_edge('B', 'B', weight=10)
    graph.add_node(str)
    return graph

def print_graph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()

if __name__ == '__main__':
    graph = basic_graph()
    print_graph(graph)