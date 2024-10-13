import networkx as nx
import matplotlib.pyplot as plt

# Завдання 1: Створення та візуалізація графа
def create_graph():
    G = nx.Graph()
    # Додавання вершин
    G.add_nodes_from([1, 2, 3, 4, 5])
    # Додавання ребер
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
    return G

def visualize_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
    plt.show()

def analyze_graph(G):
    print(f"Кількість вершин: {G.number_of_nodes()}")
    print(f"Кількість ребер: {G.number_of_edges()}")
    print(f"Ступені вершин: {dict(G.degree())}")

# Завдання 2: Реалізація алгоритмів DFS та BFS
def dfs_paths(G, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(G.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_paths(G, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(G.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def compare_algorithms(G, start, goal):
    dfs_result = list(dfs_paths(G, start, goal))
    bfs_result = list(bfs_paths(G, start, goal))
    print(f"Шляхи DFS: {dfs_result}")
    print(f"Шляхи BFS: {bfs_result}")

# Завдання 3: Реалізація алгоритму Дейкстри
def dijkstra(G, start):
    return nx.single_source_dijkstra_path(G, start)

def main():
    G = create_graph()
    visualize_graph(G)
    analyze_graph(G)
    compare_algorithms(G, 1, 5)
    # Додавання ваг до ребер
    G.add_weighted_edges_from([(1, 2, 1), (1, 3, 4), (2, 4, 2), (3, 4, 1), (4, 5, 3)])
    shortest_paths = dijkstra(G, 1)
    print(f"Найкоротші шляхи за алгоритмом Дейкстри: {shortest_paths}")

if __name__ == "__main__":
    main()