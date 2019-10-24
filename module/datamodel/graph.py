class Graph:

    """
    Provides a common interface for modelling graphs
    """

    def __init__(self):
        self.nodes = list()
        self.paths: dict = {}
        self.starting_node = None
        self.solutions: list = []

    def is_solution(self, node):
        """
        Check if input node is a solution or a final state
        :param node: node to check
        :return: True if node is a solution
        """
        for solution in self.solutions:
            if node == solution:
                return True
        return False

    def add_solution(self, node):
        """
        Add node to solutions
        :param node: node to add as solution
        """
        if self.node_exists(node):
            self.solutions.append(node)
        else:
            raise Exception("Invalid node {}".format(str(node)))

    def add_node(self, node):
        """
        Add node to node set
        :param node: node to add
        """
        self.nodes.append(node)

    def set_starting_node(self, node):
        """
        Set existing node as starting node
        :param node: node to set as starting
        """
        if self.node_exists(node):
            self.starting_node = node
        else:
            raise Exception("Node {} does not exists".format(str(node)))

    def get_starting_node(self):
        """
        :return: Retrieve the starting node
        """
        return self.starting_node

    def remove_node(self, node):
        """
        Removes existing node
        :param node: node to be removed
        """
        if self.node_exists(node):
            self.nodes.remove(node)
        else:
            raise Exception("Node {} does not exists".format(str(node)))

    def node_exists(self, node):
        """
        Checks if node exists
        :param node: node to check
        :return: True if node exists, otherwise false
        """
        return node in self.nodes

    def add_path(self, path: tuple, cost: object = 1, gen_nodes: object = False, add_reversed: bool = False):
        """
        Add path in the path dictionary
        :param path: (src_node,dest_node) -> tuple of two element
        :param cost: cost of the path
        :param gen_nodes: If True, non existing nodes will be generated. Default False
        :param add_reversed: If True, add reversed path with same cost
        """
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
        if add_reversed:
            self.add_path(tuple(reversed(path)), cost, gen_nodes, False)

    def change_cost(self, path: tuple, new_cost: int = 1):
        """
        Changes the cost of existing path
        :param path: the path to change
        :param new_cost: new path cost
        """
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        if not self.path_exists(path):
            raise Exception("Path {} does not exists".format(str(path)))
        self.paths[path] = new_cost

    def remove_path(self, path: tuple):
        """
        Remove existing path
        :param path: path to remove
        """
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        if not self.path_exists(path):
            raise Exception("Path {} do not exists".format(str(path)))
        self.paths.pop(path)

    def successor(self, node):
        """
        Given a node, returns the next possible steps
        this method should be overrided in specialized classes to model new problems
        :param node: node to check
        :return: [*(next_node, cost)], list of tuples containing next_node from starting and path cost
        """
        successor = []
        if not self.node_exists(node):
            raise Exception("Node {} does not exists".format(str(node)))
        for path in self.paths.keys():
            if path[0] == node:
                successor.append((path[1], self.paths.get(path)))
        return successor

    def path_exists(self, path: tuple):
        """
        Check if path exists
        :param path: path to check
        :return: True if path exists
        """
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        return path in self.paths.keys()

    def get_cost(self, path: tuple):
        """
        Return the cost of the path
        :param path: path to retrieve the cost
        :return: path cost
        """
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        if not self.path_exists(path):
            raise Exception("Path {} do not exists".format(str(path)))
        return self.paths.get(path)

    def get_nodes(self):
        return self.nodes
