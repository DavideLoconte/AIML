from graph import Graph


class TreeNode:
    def __init__(self, node: str = "", total_cost: int = 0, depth: int = 0, parent=None):
        self.node = node
        self.cost = total_cost
        self.depth = depth
        self.parent = parent


def get_complete_path(last_node: TreeNode):
    complete_path = list()
    while last_node.parent is not None:
        complete_path.append(last_node.node)
        last_node = last_node.parent
    complete_path.append(last_node.node)
    complete_path.reverse()
    return complete_path


class TreeSearch:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.root = TreeNode(
            node=graph.get_starting_node(),
            total_cost=0,
            depth=0,
            parent=None)
        self.fringe = [self.root]
        self.next_node: TreeNode = self.root

    def expand(self, node: TreeNode):
        successor_function = self.graph.successor(node.node, True)
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

    def search(self, node_selector=None):
        if node_selector is None:
            node_selector = fifo
        if len(self.fringe) != 0:
            self.next_node = node_selector(self.fringe)
            if self.graph.is_solution(self.next_node.node):
                return get_complete_path(self.next_node)
            else:
                new_nodes = self.expand(self.next_node)
                for new_node in new_nodes:
                    self.fringe.append(new_node)
                return self.search(node_selector)
        else:
            return False


def fifo(fringe: list):
    return fringe.pop(0)


def lifo(fringe: list):
    return fringe.pop(-1)


def least_cost(fringe: list):
    minimum = fringe[0].cost
    current = 0
    for index in range(1, len(fringe)):
        if minimum > fringe[index].cost:
            minimum = fringe[index].cost
            current = index
    return fringe.pop(current)
