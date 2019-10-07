from modules.graph import Graph


class TreeNode:
    def __init__(self, node, total_cost, depth, parent):
        self.node = node
        self.cost = total_cost
        self.depth = depth
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost


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

    def iterative_search(self, node_selector, log=False):
        while True:
            self.iteration += 1
            if log:
                print("Iteration: {}".format(self.iteration))
                print("Depth: {}\t Fringe_len: {}".format(self.next_node.depth, len(self.fringe)))
                print(": {}".format(str(self.fringe)))

            if len(self.fringe) != 0:
                self.next_node = node_selector(self.fringe)
                if self.graph.is_solution(self.next_node.node):
                    return get_complete_path(self.next_node)
                else:
                    new_nodes = self.expand(self.next_node)
                    for new_node in new_nodes:
                        self.fringe.append(new_node)
            else:
                return False

    def search(self, node_selector=None, log=False):
        if node_selector is None:
            if log:
                print("No node selection algorithm specified, falling back to breadth_first")
            node_selector = fifo
        if log:
            print("Starting iterative search")
        return self.iterative_search(node_selector, log)


def fifo(fringe: list):
    return fringe.pop(0)


def lifo(fringe: list):
    return fringe.pop(-1)


def least_cost(fringe):
    fringe.sort(key=lambda x: x.cost)
    return fringe.pop(0)
