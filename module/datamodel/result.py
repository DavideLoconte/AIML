class Result:
    """
    Abstract result class
    """
    def __init__(self):
        self.success = True


class SearchResult(Result):
    """
    Represents the result of a Tree search algorithm,
    SearchResult.success -> True if algorithm found a solution
    SearchResult.path -> All the states from starting to the solution as a list
    SearchResult.depth -> Depth of the solution
    SearchResult.cost -> Cost of the solution
    """
    def __init__(self, last_node):
        super().__init__()
        self.path = []
        if last_node is None:
            self.success = False
            self.path = None
            self.cost = None
            self.depth = None
            return
        else:
            self.cost = last_node.cost
            self.depth = last_node.depth
            while last_node.parent is not None:
                self.path.append(last_node)
                last_node = last_node.parent
            self.path.append(last_node)
            self.path.reverse()
