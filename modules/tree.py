from modules.graph import Graph
from abc import ABCMeta, abstractmethod


class TreeNode:
    def __init__(self, node, total_cost, depth, parent):
        self.node = node
        self.cost = total_cost
        self.depth = depth
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost


class TreeSearch:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.root = TreeNode(
            node=graph.get_starting_node(),
            total_cost=0,
            depth=0,
            parent=None)
        self.fringe = [self.root]
        self.next_node = self.root
        self.iteration = 0

    def expand(self, node):
        successor_function = self.graph.successor(node.node)
        new_nodes_list = []
        for successor in successor_function:
            new_node = TreeNode(
                node=successor[0],
                total_cost=node.cost + successor[1],
                depth=node.depth + 1,
                parent=node
            )
            new_nodes_list.append(new_node)
        return new_nodes_list

    def iterative_search(self, log=False):
        if  isinstance(self.__class__, TreeSearch):
            raise Exception("TreeSearch is abstract")
        while True:
            self.iteration += 1
            if log:
                print("Iteration: {}".format(self.iteration))
                print("Depth: {}\t Fringe_len: {}".format(self.next_node.depth, len(self.fringe)))
                print(": {}".format(str(self.fringe)))

            if len(self.fringe) != 0:
                self.next_node = self.get()
                if self.graph.is_solution(self.next_node.node):
                    return self.get_complete_path(self.next_node)
                else:
                    new_nodes = self.expand(self.next_node)
                    for new_node in new_nodes:
                        self.add(new_node)
            else:
                return False

    @staticmethod
    def get_complete_path(last_node: TreeNode):
        complete_path = list()
        cost = last_node.cost
        depth = last_node.depth
        while last_node.parent is not None:
            complete_path.append(last_node.node)
            last_node = last_node.parent
        complete_path.append(last_node.node)
        complete_path.reverse()
        result = {
            "path": complete_path,
            "cost": cost,
            "depth": depth
        }
        return result

    @abstractmethod
    def search(self, log=False):
        raise Exception("TreeSearch is abstract")

    @abstractmethod
    def get(self):
        raise Exception("TreeSearch is abstract")

    @abstractmethod
    def add(self, node):
        raise Exception("TreeSearch is abstract")