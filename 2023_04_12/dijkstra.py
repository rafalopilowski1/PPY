class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.connections = []

    def __str__(self) -> str:
        return f"Node: x={self.x}, y={self.y}, value={self.value}"

    def __repr__(self):
        return f"Node: x={self.x}, y={self.y}, value={self.value}"


class NodeConnection:
    def __init__(self, dest_node, cost):
        self.dest_node = dest_node
        self.cost = cost


class Graph:
    def __init__(self):
        self.nodes = []

    def get_node_or_create(self, value, given_x, given_y):
        found_nodes = list(filter(lambda node: node.x == given_x and node.y == given_y, self.nodes))
        if len(found_nodes) == 0:
            temp_node = Node(value, given_x, given_y)
            self.nodes.append(temp_node)
            return temp_node
        return found_nodes[0]

    def min_distance(self, dist: dict, spt_set: dict):
        return list(sorted(filter(lambda node: not spt_set.get(node), self.nodes), key=lambda node: dist.get(node)))[0]

    def dijkstra(self, src: Node):
        distance = {}
        visited_nodes = {}
        for node in self.nodes:
            distance[node] = float('inf')
            visited_nodes[node] = False
        distance[src] = 0.0
        for _ in self.nodes:
            nearest_node = self.min_distance(distance, visited_nodes)
            visited_nodes[nearest_node] = True
            for connected_node in filter(lambda node_lambda: not visited_nodes.get(node_lambda.dest_node),
                                         nearest_node.connections):
                if distance.get(nearest_node) + connected_node.cost <= distance.get(connected_node.dest_node):
                    distance[connected_node.dest_node] = distance.get(nearest_node) + connected_node.cost
        return distance


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    graph = Graph()
    sample_nodes = []
    node_a = Node(0, 0, 'A')
    node_b = Node(1, 1, 'B')
    node_c = Node(2, 2, 'C')
    node_d = Node(3, 3, 'D')
    node_e = Node(4, 4, 'E')
    node_f = Node(5, 5, 'F')

    node_a.connections.append(NodeConnection(node_b, 4))
    node_a.connections.append(NodeConnection(node_c, 5))
    node_b.connections.append(NodeConnection(node_c, 11))
    node_b.connections.append(NodeConnection(node_e, 7))
    node_b.connections.append(NodeConnection(node_d, 9))
    node_c.connections.append(NodeConnection(node_e, 3))
    node_d.connections.append(NodeConnection(node_e, 13))
    node_d.connections.append(NodeConnection(node_f, 2))
    node_e.connections.append(NodeConnection(node_f, 6))

    graph.nodes.append(node_a)
    graph.nodes.append(node_b)
    graph.nodes.append(node_c)
    graph.nodes.append(node_d)
    graph.nodes.append(node_e)
    graph.nodes.append(node_f)

    graph_resolved = graph.dijkstra(node_a)

    print("Distance from node A:")
    for node, distance in graph_resolved.items():
        print(node, distance, sep=' = ')
