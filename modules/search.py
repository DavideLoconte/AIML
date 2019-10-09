from modules.tree import TreeSearch
import heapq


class BreadthFirst(TreeSearch):
    def __init__(self, graph):
        super().__init__(graph)
        self.fringe = [self.root]

    def add(self, node):
        self.fringe.append(node)

    def get(self):
        return self.fringe.pop(0)

    def search(self, log=False):
        return self.iterative_search(log=log)


class DepthFirst(TreeSearch):
    def __init__(self, graph):
        super().__init__(graph)
        self.fringe = [self.root]

    def add(self, node):
        self.fringe.append(node)

    def get(self):
        return self.fringe.pop(-1)

    def search(self, log=False):
        return self.iterative_search(log=log)


class Uniform(TreeSearch):
    def __init__(self, graph):
        super().__init__(graph)
        self.fringe = [self.root]

    def add(self, node):
        heapq.heappush(self.fringe, node)

    def get(self):
        return heapq.heappop(self.fringe)

    def search(self, log=False):
        return self.iterative_search(log=log)


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

    def search(self, log=False):
        return self.iterative_search(log=log)


class IterativeLimitedDepth(TreeSearch):
    def __init__(self, graph, limit=-1):
        super().__init__(graph)
        self.fringe = [self.root]
        self.limit = limit

    def add(self, node):
        if node.depth < self.limit:
            self.fringe.append(node)

    def get(self):
        return self.fringe.pop(-1)

    def search(self, log=False):
        if self.limit != -1:
            for i in range(0, self.limit):
                result = self.iterative_search(log=log)
                if result != False:
                    return result
        else:
            while True:
                result = self.iterative_search(log=log)
                if result != False:
                    return result
        return False

