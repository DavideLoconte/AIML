class Graph:
    """Class modelling a graph
    Nodes are a list of strings called nodes
    Paths between nodes are a dictionary of k-v {(source_node, dest_node): cost}
    Cost is a integer value
    Solutions is a list of nodes
    Starting is a string representing a node"""

    @staticmethod
    def __check_node(node):
        """Check if node overloads equality operator"""
        try:
            if node == node:
                return True
            else:
                return False
        except:
            if node is node:
                return True
            else:
                return False

    @staticmethod
    def __nodes_equals(a, b):
        try:
            if a == b:
                return True
        except:
            if a is b:
                return True
        return False

    def __init__(self):
        self.nodes: list = []
        self.paths: dict = {}
        self.starting: str = ""
        self.solutions: list = []

    def is_solution(self, node):
        """Return true if given node is in solution"""
        for solution in self.solutions:
            if self.__nodes_equals(node, solution):
                return True
        return False

    def add_solution(self, node):
        if self.__check_node(node):
            self.solutions.append(node)
        else:
            raise Exception("Invalid node {}".format(str(node)))

    def add_node(self, node):
        """Add non existing node. By default first node is setted as starting"""
        for existing_node in self.nodes:
            if self.__nodes_equals(existing_node, node):
                raise Exception("Node {} already exists".format(str(node)))
        if self.starting == "":
            self.starting = node
        self.nodes.append(node)

    def set_starting_node(self, node):
        """Set a new starting node"""
        if self.node_exists(node):
            self.starting = node
        else:
            raise Exception("Node {} does not exists".format(str(node)))

    def get_starting_node(self):
        """Return starting node"""
        return self.starting

    def remove_node(self, node):
        """Remove existing node"""
        for existing_node in self.nodes:
            if self.node_exists(node):
                self.nodes.remove(node)
            else:
                raise Exception("Node {} does not exists".format(str(node)))

    def node_exists(self, node):
        """Return True if node exists"""
        for existing_node in self.nodes:
            if self.__nodes_equals(node, existing_node):
                return True
        return False

    def add_path(self, path: tuple, cost: int = 1, gen_nodes: bool = False):
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
        del path

    def successor(self, node, return_cost: bool = False):
        """Return successor function of give node. By default, return value is a list of successor nodes
        if @return_cost is set True, return value is a list of (dest_node, cost)"""
        successor = []
        if not self.node_exists(node):
            raise Exception("Node {} does not exists".format(str(node)))
        for path in self.paths.keys():
            if self.__nodes_equals(node, path[0]):
                if return_cost:
                    successor.append((path[1], self.paths.get(path)))
                else:
                    successor.append(path[1])
        return successor

    def path_exists(self, path: tuple):
        """Return True if path exists"""
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        for existing_path in self.paths.keys():
            if self.__nodes_equals(path[0], existing_path[0]) and self.__nodes_equals(path[1], existing_path[1]):
                return True
        return False

    def get_cost(self, path: tuple):
        """Return cost of existing path"""
        if len(path) != 2:
            raise Exception("Illegal path format: {}".format(str(path)))
        if not self.path_exists(path):
            raise Exception("Path {} do not exists".format(str(path)))
        return self.paths.get(path)
