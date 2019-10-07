class Graph:

    """Class modelling a graph
    Nodes are a list of strings called nodes
    Paths between nodes are a dictionary of k-v {(source_node, dest_node): cost}
    Cost is a integer value
    Solutions is a list of nodes
    Starting is a string representing a node"""

    def __init__(self):
        self.nodes = set()
        self.paths: dict = {}
        self.starting_node = None
        self.solutions: list = []

    def is_solution(self, node):
        """Return true if given node is in solution"""
        for solution in self.solutions:
            if node == solution:
                return True
        return False

    def add_solution(self, node):
        if self.node_exists(node):
            self.solutions.append(node)
        else:
            raise Exception("Invalid node {}".format(str(node)))

    def add_node(self, node):
        self.nodes.add(node)

    def set_starting_node(self, node):
        """Set a new starting node"""
        if self.node_exists(node):
            self.starting_node = node
        else:
            raise Exception("Node {} does not exists".format(str(node)))

    def get_starting_node(self):
        """Return starting node"""
        return self.starting_node

    def remove_node(self, node):
        """Remove existing node"""
        if self.node_exists(node):
            self.nodes.remove(node)
        else:
            raise Exception("Node {} does not exists".format(str(node)))

    def node_exists(self, node):
        """Return True if node exists"""
        return node in self.nodes

    def add_path(self, path: tuple, cost: object = 1, gen_nodes: object = False):
        """Add path between nodes. If gen_nodes is set True, non existing nodes will be generated"""
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        if self.path_exists(path):
            raise Exception("Path {} already exists".format(str(path)))
        if gen_nodes:
            if not self.node_exists(path[0]):
                self.add_node(path[0])
            if not self.node_exists(path[1]):
                self.add_node(path[1])
        elif not self.node_exists(path[0]) or not self.node_exists(path[1]):
            raise Exception("Node {} or {} does not exists".format(path[0], path[1]))
        self.paths[path] = cost

    def change_cost(self, path: tuple, new_cost: int = 1):
        """Change cost of existing path"""
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        if not self.path_exists(path):
            raise Exception("Path {} does not exists".format(str(path)))
        self.paths[path] = new_cost

    def remove_path(self, path: tuple):
        """Remove existing path"""
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        if not self.path_exists(path):
            raise Exception("Path {} do not exists".format(str(path)))
        self.paths.pop(path)

    def successor(self, node):
        """Return successor function of give node. By default, return value is a list of successor nodes
        if @return_cost is set True, return value is a list of (dest_node, cost)"""
        successor = []
        if not self.node_exists(node):
            raise Exception("Node {} does not exists".format(str(node)))
        for path in self.paths.keys():
            successor.append((path[1], self.paths.get(path)))
        return successor

    def path_exists(self, path: tuple):
        """Return True if path exists"""
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        return path in self.paths.keys()

    def get_cost(self, path: tuple):
        """Return cost of existing path"""
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        if not self.path_exists(path):
            raise Exception("Path {} do not exists".format(str(path)))
        return self.paths.get(path)
