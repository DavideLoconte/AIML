from datamodel.result import CSPResult


class CSPProblem:
    def __init__(self):
        self.assignment = {}
        self.domain = set()

    def is_assignment_complete(self):
        raise NotImplementedError

    def select_unassigned_variable(self):
        raise NotImplementedError

    def is_assignment_consistent(self, var, value):
        raise NotImplementedError

    # Public

    def add_assignment(self, var, value):
        self.assignment[var] = value

    def remove_assignment(self, var):
        del self.assignment[var]

    # Search function

    def search(self):
        return self.backtrack_search()

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

