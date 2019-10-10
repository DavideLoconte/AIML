from modules.graph import Graph
from abc import abstractmethod


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
        self.closed = set()
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
        self.closed.add(node.node)
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

    def iterative_search(self):
        if isinstance(self.__class__, TreeSearch):
            raise Exception("TreeSearch is abstract")
        while True:
            self.iteration += 1
            if len(self.fringe) != 0:
                self.next_node = self.get()
                if self.graph.is_solution(self.next_node.node):
                    return self.get_complete_path(self.next_node)
                else:
                    new_nodes = self.expand(self.next_node)
                    for new_node in new_nodes:
                        if new_node.node not in self.closed:
                            self.add(new_node)
            else:
                return {
                    "success": False,
                    "depth": self.next_node.depth
                }

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
            "depth": depth,
            "success": True
        }
        return result

    @abstractmethod
    def search(self):
        raise Exception("TreeSearch is abstract")

    @abstractmethod
    def get(self):
        raise Exception("TreeSearch is abstract")

    @abstractmethod
    def add(self, node):
        raise Exception("TreeSearch is abstract")
