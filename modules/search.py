from modules.tree import TreeSearch
import heapq
import collections
import sys


class BreadthFirst(TreeSearch):
    def __init__(self, graph):
        super().__init__(graph)
        self.fringe = collections.deque([self.root])

    def add(self, node):
        self.fringe.append(node)

    def get(self):
        return self.fringe.popleft()

    def search(self):
        return self.iterative_search()


class DepthFirst(TreeSearch):
    def __init__(self, graph):
        super().__init__(graph)
        self.fringe = collections.deque([self.root])

    def add(self, node):
        self.fringe.append(node)

    def get(self):
        return self.fringe.pop()

    def search(self):
        return self.iterative_search()


class Uniform(TreeSearch):
    def __init__(self, graph):
        super().__init__(graph)
        self.fringe = [self.root]

    def add(self, node):
        heapq.heappush(self.fringe, node)

    def get(self):
        return heapq.heappop(self.fringe)

    def search(self):
        return self.iterative_search()


class LimitedDepth(TreeSearch):
    def __init__(self, graph, limit):
        super().__init__(graph)
        self.fringe = [self.root]
        if limit is None:
            raise Exception("Limited search requires limit value")
        self.limit = limit

    def add(self, node):
        if node.depth < self.limit:
            self.fringe.append(node)

    def get(self):
        return self.fringe.pop(-1)

    def search(self):
        return self.iterative_search()


class IterativeLimitedDepth:
    def __init__(self, graph, limit=-1):
        self.graph = graph
        if limit < 0:
            self.limit = sys.maxsize

    def search(self):
        for i in range(self.limit):
            result = LimitedDepth(self.graph, i).search()
            if result["success"]:
                return result


class LimitedCost(TreeSearch):
    def __init__(self, graph, limit):
        super().__init__(graph)
        self.fringe = [self.root]
        if limit is None:
            raise Exception("Limited searches requires limit value")
        self.limit = limit

    def add(self, node):
        if node.cost < self.limit:
            self.fringe.append(node)

    def get(self):
        return self.fringe.pop(-1)

    def search(self):
        return self.iterative_search()


class Greedy(TreeSearch):
    def __init__(self, graph, heuristic):
        super().__init__(graph)
        self.heuristic_function = heuristic
        self.fringe = [(heuristic(self.root), self.root)]

    def add(self, node):
        heapq.heappush(self.fringe, (self.heuristic_function(node), node))

    def get(self):
        return heapq.heappop(self.fringe)[1]

    def search(self):
        return self.iterative_search()


class AStar(TreeSearch):
    def __init__(self, graph, heuristic):
        super().__init__(graph)
        self.heuristic_function = heuristic
        self.fringe = [(heuristic(self.root) + self.root.cost, self.root)]

    def add(self, node):
        heapq.heappush(self.fringe, (self.heuristic_function(node) + node.cost, node))

    def get(self):
        return heapq.heappop(self.fringe)[1]

    def search(self):
        return self.iterative_search()