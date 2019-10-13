class Closure:
    """
    Class representing closure for tree searches
    """
    def __init__(self):
        self.nodes = set()

    def __contains__(self, item):
        return item in self.nodes

    def add(self, node):
        self.nodes.add(node)


class WeightedClosure(Closure):
    """
    Closure which stores weights alongside visited nodes
    If nodes is visited with a smaller weight, it is considered to not be visited yet
    Used in deepening searches
    """
    def __init__(self, weight):
        """
        Init weighted closure istance
        :param weight: Callable which evaluates weight. Function which calls
        """
        super().__init__()
        self.weight = weight
        self.nodes = {}

    def __contains__(self, item):
        """
        Check if state is stored in the closure
        Currently stored state with larger weight are not considered
        :param item: State to be checked, must be a State instance
        :return: True if state exists with a smaller weight.
        Accepts one parameter, a State instance
        """
        if item not in self.nodes:
            return False
        elif self.nodes[item] > self.weight(item):
            return False
        else:
            return True

    def add(self, item):
        """
        Add state to closure if its weight is smaller than already existing
        :param item: State to be stored, must be a State instance
        """
        if item in self.nodes.keys():
            self.nodes[item] = min(self.weight(item), self.nodes[item])
        else:
            self.nodes[item] = self.weight(item)