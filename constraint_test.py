from module.constraint.constraint import CSPProblem
from module.datamodel.graph import Graph


class Australia(CSPProblem):

    def __init__(self, graph, domain):
        super().__init__(domain)
        self.graph = graph
        self.domain = domain

    def is_assignment_complete(self):
        if len(self.assignment) == len(self.graph.nodes):
            for region, color in self.assignment.items():
                if not self.is_assignment_consistent(region, color):
                    return False
            return True
        else:
            return False

    def select_unassigned_variable(self):
        for node in self.graph.nodes:
            if self.assignment.get(node) is None:
                return node

    def is_assignment_consistent(self, var, value):
        for path in self.graph.paths:
            color_a = self.assignment.get(path[0])
            color_b = self.assignment.get(path[1])
            if color_a == color_b and color_a is not None:
                return False
        return True

    def add_assignment(self, var, value):
        self.assignment[var] = value

    def remove_assignment(self, var):
        del self.assignment[var]


graph = Graph()
graph.add_path(("WA", "NT"), 1, True, True)
graph.add_path(("WA", "SA"), 1, True, True)
graph.add_path(("NT", "Q"), 1, True, True)
graph.add_path(("NT", "SA"), 1, True, True)
graph.add_path(("Q", "NSW"), 1, True, True)
graph.add_path(("SA", "NSW"), 1, True, True)
graph.add_path(("SA", "V"), 1, True, True)
graph.add_path(("NSW", "V"), 1, True, True)
graph.add_path(("SA", "Q"), 1, True, True)
graph.add_node("T")

domain = ["RED", "GREEN", "BLUE"]
australia = Australia(graph, domain)
print(australia.backtrack_search().assignment)
