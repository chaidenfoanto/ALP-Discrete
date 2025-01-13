from GraphTheory import GraphTheory

graph = GraphTheory()

# Menambahkan simpul (node)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

# Menambahkan sisi (edge) dengan bobot
graph.add_edge(1, 2, weight=4.5)
graph.add_edge(1, 3, weight=3.2)
graph.add_edge(2, 4, weight=2.7)
graph.add_edge(3, 4, weight=1.8)
graph.add_edge(1, 4, weight=6.7)
graph.add_edge(3, 5, weight=2.7)

# Visualisasi graf
print("Visualisasi Graf:")
graph.visualize_graph()

# Mencari jalur terpendek antara node 1 dan 5
print("\nJalur Terpendek dari 1 ke 5:")
path = graph.shortest_path(1, 5)
print(f"Jalur: {path}")

# Visualisasi jalur terpendek
print("\nVisualisasi Jalur Terpendek:")
graph.visual_shortest_path(1, 5)

# Menampilkan derajat node tertentu
node = 3
print(f"\nDerajat simpul {node}: {graph.degree_of_node(node)}")

# Mengecek apakah graf terhubung
print("\nApakah graf terhubung?")
print(graph.is_connected())

# Menampilkan Minimum Spanning Tree (MST)
print("\nMinimum Spanning Tree (MST):")
mst = graph.minimum_spanning_tree()
print(mst)

# Menghitung eksentrisitas simpul tertentu
try:
    eccentricity = graph.eccentricity_of_node(1)
    print(f"\nEksentrisitas simpul 1: {eccentricity}")
except ValueError as e:
    print(e)
