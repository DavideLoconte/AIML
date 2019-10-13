from module.datamodel.graph import Graph
from module.datamodel.result import SearchResult
from module.datamodel.closure import Closure


class State:
    """
    Represent a tree node for the search algorithms
    Encapsulate some information about each node
    """
    def __init__(self, content, total_cost, depth, parent):
        self.content = content
        self.cost = total_cost
        self.depth = depth
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.content == other.content

    def __hash__(self):
        return self.content.__hash__()

    def __repr__(self):
        return self.content.__repr__()

    def __iter__(self):
        return self.content.__iter__()

    def __next__(self):
        return self.content.__next__()


class TreeSearch:
    """
    Abstract tree class, not intended to be used
    you should use specialized algorithms
    """
    def __init__(self, graph: Graph):
        """
        Init tree search
        :param graph: instance implementing successor function to generate graph
        """
        self.closure = Closure()
        self.graph = graph
        self.root = State(
            content=graph.get_starting_node(),
            total_cost=0,
            depth=0,
            parent=None)
        self.fringe = [self.root]
        self.next_node = self.root
        self.iteration = 0

    def expand(self, state):
        """
        Expand tree state by generating states from successor
        :param state: state to expand
        :return: list of new states to be appended to the fringe
        """
        successor_function = self.graph.successor(state.content)
        new_nodes_list = []
        for successor in successor_function:
            new_node = State(
                content=successor[0],
                total_cost=state.cost + successor[1],
                depth=state.depth + 1,
                parent=state
            )
            new_nodes_list.append(new_node)
        self.closure.add(state)
        return new_nodes_list

    def _iterative_search(self):
        """
        Start iterative search
        :return: SearchResult istance representing the result
        """
        if isinstance(self.__class__, TreeSearch):
            raise Exception("TreeSearch is abstract")
        while True:
            self.iteration += 1
            if len(self.fringe) != 0:
                self.next_node = self.get()
                if self.graph.is_solution(self.next_node.content):
                    return SearchResult(self.next_node)
                else:
                    new_nodes = self.expand(self.next_node)
                    for new_node in new_nodes:
                        if new_node not in self.closure:
                            self.add(new_node)
            else:
                return SearchResult(None)

    def search(self):
        """
        Abstract search function, has to be overridden
        Start the search
        :return: SearchResult
        """
        raise Exception("TreeSearch is abstract")

    def get(self):
        """
        Abstract get function, has to be overridden
        :return: get the next node in the fringe
        """
        raise Exception("TreeSearch is abstract")

    def add(self, state):
        """
        Abstract add function, has to be overridden
        Add state to fringe
        :param state: state to be added
        """
        raise Exception("TreeSearch is abstract")


