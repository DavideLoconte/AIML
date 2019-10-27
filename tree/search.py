from tree.tree import TreeSearch
from datamodel.closure import WeightedClosure
import heapq
import collections
import sys


class BreadthFirst(TreeSearch):
    """
    TreeSearch implementation using breadth first strategy
    (FIFO) to select states from fringe
    Uses deque structure to retrieve states faster
    """
    def __init__(self, graph):
        super().__init__(graph)
        self.fringe = collections.deque([self.root])

    def add(self, state):
        """
        Add state to fringe
        :param state: add state to Fringe
        """
        self.fringe.append(state)

    def get(self):
        """
        :return: Get next State
        """
        return self.fringe.popleft()

    def search(self):
        """
        Start tree search
        :return: SearchResult
        """
        return self._iterative_search()


class DepthFirst(TreeSearch):
    """
    TreeSearch implementation using depth
    first strategy (LIFO) to select states from the fringe
    Uses deque structure to retrieve states faster
    """

    def __init__(self, graph):
        """
        :param graph: Problem to solve
        """
        super().__init__(graph)
        self.fringe = collections.deque([self.root])

    def add(self, state):
        """
        Add state to fringe
        :param state: add state to Fringe
        """
        self.fringe.append(state)

    def get(self):
        """
        :return: Get next State
        """
        return self.fringe.pop()

    def search(self):
        """
        Start tree search
        :return: SearchResult
        """
        return self._iterative_search()


class Uniform(TreeSearch):
    """
    TreeSearch implementation using uniform cost
    strategy to select states from fringe (select least cost states first)
    Exploits heap queues to order nodes in an efficent way
    """
    def __init__(self, graph):
        """
        :param graph: Problem to solve
        """
        super().__init__(graph)
        self.fringe = [self.root]

    def add(self, state):
        heapq.heappush(self.fringe, state)

    def get(self):
        return heapq.heappop(self.fringe)

    def search(self):
        return self._iterative_search()


class LimitedDepth(TreeSearch):
    """
    TreeSearch implementation using depth
    first strategy (LIFO) to select states from the fringe
    It limits the depth to a given value
    """
    def __init__(self, graph, limit=-1):
        """
        :param graph: Problem to solve
        :param limit: max tree depth. If none, it selects sys.maxsize
        """
        super().__init__(graph)
        self.fringe = [self.root]
        self.closure = WeightedClosure(lambda x: x.depth)

        if limit < 0:
            limit = sys.maxsize
        self.limit = limit

    def add(self, state):
        if state.depth <= self.limit:
            self.fringe.append(state)

    def get(self):
        return self.fringe.pop()

    def search(self):
        return self._iterative_search()


class IterativeDeepning:
    """
    Not an actual implementation of TreeSearch
    Performs many limited depth searches iteratively and increase
    depth limit at each steps
    """
    def __init__(self, graph, limit=-1):
        """
        :param graph: Problem to solve
        :param limit: max final depth. If none, it selects sys.maxsize
        """
        self.graph = graph
        if limit < 0:
            self.limit = sys.maxsize
        else:
            self.limit = limit

    def search(self):
        for i in range(self.limit):
            result = LimitedDepth(self.graph, i).search()
            if result.success:
                return result


class Greedy(TreeSearch):
    """
    TreeSearch implementation using greedy
    strategy to select states from fringe. It needs
    a weight function to assign each state a heuristic value,
    which depends on the problem. It selects the nodes with smallest
    heuristic value.
    Exploits heap queues to order nodes efficiently
    """
    def __init__(self, graph, heuristic):
        """
        Asks for graph and heuristic function
        :param graph: Problem to solve
        :param heuristic: function used to compute heuristic value.
        Must have only one argument, a State instance
        """
        super().__init__(graph)
        self.heuristic_function = heuristic
        self.fringe = [(heuristic(self.root), self.root)]

    def add(self, state):
        heapq.heappush(self.fringe, (self.heuristic_function(state), state))

    def get(self):
        return heapq.heappop(self.fringe)[1]

    def search(self):
        return self._iterative_search()


class AStar(TreeSearch):
    """
    TreeSearch implementation using greedy
    strategy to select states from fringe. It needs
    a weight function to assign each state a heuristic value,
    which depends on the problem. It selects the nodes with smallest
    weight, computed as (heuristic value + path cost). If
    heuristic is a admissible function, it ensures to find the optimal value.
    Exploits heap queues to order nodes efficiently
    """
    def __init__(self, graph, heuristic):
        """
        Asks for graph and heuristic function
        :param graph: Problem to solve
        :param heuristic: function used to compute heuristic value.
        Must have only one argument, a State instance
        """
        super().__init__(graph)
        self.heuristic_function = heuristic
        self.fringe = [(heuristic(self.root) + self.root.cost, self.root)]

    def add(self, state):
        heapq.heappush(self.fringe, (self.heuristic_function(state) + state.cost, state))

    def get(self):
        return heapq.heappop(self.fringe)[1]

    def search(self):
        return self._iterative_search()
