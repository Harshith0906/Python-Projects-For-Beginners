import networkx as nx
import matplotlib.pyplot as plt
import heapq
import time

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

        # Visualize the current step
        visualize_step(graph, distances, current_node)
        time.sleep(1)  # Add a delay for visualization

    return distances

def visualize_step(graph, distances, current_node):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    labels = {node: f"{node}\n{distances[node]:.2f}" for node in G.nodes()}
    node_colors = ['lightblue' if n == current_node else 'gray' for n in G.nodes()]

    nx.draw(G, pos, with_labels=True, labels=labels, node_color=node_colors, node_size=700, font_size=8, font_color='black')
    edge_labels = {(i, j): f"{G[i][j]['weight']}" for i, j in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title(f"Current Node: {current_node}")
    plt.show()

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    print(f"Shortest distances from {start_node}: {shortest_distances}")
