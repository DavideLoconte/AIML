from module.datamodel.graph import Graph
from module.datamodel.result import CSPResult


class CSPProblem:
    def __init__(self, domain):
        self.assignment = {}
        self.domain = []

    def is_assignment_complete(self):
        raise NotImplementedError

    def select_unassigned_variable(self):
        raise NotImplementedError

    def is_assignment_consistent(self, var, value):
        raise NotImplementedError

    def add_assignment(self, var, value):
        raise NotImplementedError

    def remove_assignment(self, var):
        raise NotImplementedError

    def backtrack_search(self):
        if self.is_assignment_complete():
            return CSPResult(self.assignment)
        var = self.select_unassigned_variable()
        if var is not None:
            for value in self.domain:
                if self.is_assignment_consistent(var, value):
                    self.add_assignment(var, value)
                    self.backtrack_search()
                    if self.is_assignment_complete():
                        return CSPResult(assignment=self.assignment)
                    self.remove_assignment(var)
        return CSPResult(None)


def backtracking_search(csp):
    return _backtracks({}, csp)


def _backtracks(assignment, csp):
    if csp.is_assignment_complete():
        return CSPResult(assignment)
    var = csp.select_unassigned_variable()
    for value in csp.domain:
        if csp.is_assignment_consistent(var, value):
            csp.add_assignment(var, value)
            result = _backtracks(assignment, csp)
            if result.success:
                return result
            csp.remove_assignment(var)
    return CSPResult(None)
