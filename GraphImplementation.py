class Node:
    def __init__(self, value, neighbors=None) :
        self.value = value
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors

    def has_neighbors(self):
        if len(self.neighbors) == 0:
            return False
        return True

    def number_of_neighbors(self):
        return len(self.neighbors)

    def add_neighbor (self, neighbor):
        self.neighbors.append(neighbor)


class Graph:

    def __init__(self, nodes=None) :
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def add_node( self, value, neighbors=None) :
        self.nodes .append(Node (value, neighbors))

    def find_node( self, value):
        for node in self.nodes:
            if node. value == value:
                return node
            return None

    def add_edge( self, valuel, value2, weight=1):
        nodel = self. find_node (valuel)
        node2 = self. find_node(value2)
        if (nodel is not None) and ( node2 is not None):
            nodel.add_neighboor((node2, weight))
            node2.add_neighboor((nodel, weight))
        else:
            print( "Error: One or more nodes were not found'")

    def number_of_nodes(self):
        return f"The graph has {len(self .nodes)} nodes"

    def are_connected( self, node_one, node_two):
        node_one = self.find_node (node_one)
        node_two = self.find_node (node_two)
        for neighboor in node_one. neighbors:
            if neighboor [0]. value == node_two.value:
                return True
            return False

