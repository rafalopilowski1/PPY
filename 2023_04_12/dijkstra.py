from math import inf

import lib.algorithms.dijkstra.graph as graph
import lib.algorithms.dijkstra.node as node
import lib.algorithms.dijkstra.node_connection as node_connection

if __name__ == '__main__':
    graph = graph.Graph()
    sample_nodes = []
    node_a = node.Node(0, 0, 'A')
    node_b = node.Node(1, 1, 'B')
    node_c = node.Node(2, 2, 'C')
    node_d = node.Node(3, 3, 'D')
    node_e = node.Node(4, 4, 'E')
    node_f = node.Node(5, 5, 'F')

    node_a.connections.append(node_connection.NodeConnection(node_b, 4))
    node_a.connections.append(node_connection.NodeConnection(node_c, 5))
    node_b.connections.append(node_connection.NodeConnection(node_c, 11))
    node_b.connections.append(node_connection.NodeConnection(node_e, 7))
    node_b.connections.append(node_connection.NodeConnection(node_d, 9))
    node_c.connections.append(node_connection.NodeConnection(node_e, 3))
    node_d.connections.append(node_connection.NodeConnection(node_e, 13))
    node_d.connections.append(node_connection.NodeConnection(node_f, 2))
    node_e.connections.append(node_connection.NodeConnection(node_f, 6))

    graph.nodes.append(node_a)
    graph.nodes.append(node_b)
    graph.nodes.append(node_c)
    graph.nodes.append(node_d)
    graph.nodes.append(node_e)
    graph.nodes.append(node_f)

    print("Distance from node A:")
    graph_resolved = graph.dijkstra(node_a)
    for node, distance in graph_resolved.items():
        if (distance == inf):
            print(node, "Not reachable", sep=' = ')
        else:
            print(node, distance, sep=' = ')

    print("Distance from node B:")
    graph_resolved = graph.dijkstra(node_b)
    for node, distance in graph_resolved.items():
        if (distance == inf):
            print(node, "Not reachable", sep=' = ')
        else:
            print(node, distance, sep=' = ')
