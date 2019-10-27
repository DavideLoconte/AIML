from constraint.constraint import CSPProblem


class CSPForwardChecking(CSPProblem):

    def __init__(self):
        super().__init__()

    def cost(self, var, value):
        raise NotImplementedError

    def is_assignment_complete(self):
        raise NotImplementedError

    def select_unassigned_variable(self):
        raise NotImplementedError

    def is_assignment_consistent(self, var, value):
        raise NotImplementedError