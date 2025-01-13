import networkx as nx
import matplotlib.pyplot as plt

class GraphTheory:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        """Menambahkan simpul ke graf."""
        self.graph.add_node(node)

    def add_edge(self, u, v, weight=1):
        """Menambahkan sisi dengan bobot tertentu."""
        self.graph.add_edge(u, v, weight=weight)

    def visualize_graph(self):
        """Visualisasi graf dengan bobot pada sisi."""
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.title("Graph Visualization")
        plt.show()

    def shortest_path(self, start, end):
        """Menghitung jalur terpendek berdasarkan bobot."""
        return nx.shortest_path(self.graph, source=start, target=end, weight='weight')

    def visual_shortest_path(self, start, end):
        """Visualisasi jalur terpendek."""
        path = self.shortest_path(start, end)
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')

        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=2)
        plt.title("Graph Visualization with Shortest Path")
        plt.show()

    # 5 metode tambahan
    def degree_of_node(self, node):
        """Menghitung derajat suatu simpul."""
        return self.graph.degree[node]

    def is_connected(self):
        """Memeriksa apakah graf terhubung atau tidak."""
        return nx.is_connected(self.graph)

    def minimum_spanning_tree(self):
        """Menghitung Minimum Spanning Tree (MST)."""
        mst = nx.minimum_spanning_tree(self.graph, weight='weight')
        return list(mst.edges(data=True))

    def all_pairs_shortest_paths(self):
        """Menghitung semua pasangan jalur terpendek."""
        return dict(nx.all_pairs_dijkstra_path(self.graph, weight='weight'))

    def eccentricity_of_node(self, node):
        """Menghitung eksentrisitas suatu simpul."""
        if nx.is_connected(self.graph):
            return nx.eccentricity(self.graph, node)
        else:
            raise ValueError("Graf tidak terhubung, tidak dapat menghitung eksentrisitas.")
