from module.datamodel.graph import Graph
from module.constraint.constraint import CSPProblem
from module.utils.stopwatch import Stopwatch



def make_row(rowdata, col, empty, full, start, end):
    items = [col] * (2*len(rowdata) + 1)
    items[1::2] = (full if d else empty for d in rowdata)
    items[0] = start
    items[-1] = end
    return ''.join(items)


def make_board(queens, col="┼", row="───", empty="   ", full=" ♛ "):
    size = len(queens)
    bar = make_row(queens, col, row, row, '╟', '╢')
    board = [bar] * (2*size + 1)
    board[1::2] = (make_row([i == q for i in range(size)], '│', empty, full, '║', "║") for q in queens)
    first = list(board[0])
    end = list(board[-1])
    first[0] = '╔'
    first[-1] = '╗'
    for idx, c in enumerate(first):
        if c == col:
            first[idx] = '╤'
        if c == '─':
            first[idx] = '═'
    for idx, c in enumerate(end):
        if c == col:
            end[idx] = '╧'
        if c == '─':
            end[idx] = '═'
    end[0] = '╚'
    end[-1] = '╝'
    board[0] = ''.join(first)
    board[-1] = ''.join(end)

    return '\n'.join(board)


queens = [0, 2, 6, 4, 7, 1, 5, 3]


class QueenCSP(CSPProblem):

    def __init__(self, size):
        super().__init__([1])
        self.size = size
        self.assignment = []
        self.domain = []
        for i in range(self.size):
            self.domain.append(i)
            self.assignment.append(-1)
        self.var = range(size)

    def is_assignment_complete(self):
        if self.assignment.count(-1) != 0:
            return False
        for assignment in enumerate(self.assignment):
            if not self.is_assignment_consistent(assignment[0], assignment[1]):
                return True
        return False

    def select_unassigned_variable(self):
        if -1 not in self.assignment:
            return None
        return self.assignment.index(-1)

    def is_assignment_consistent(self, var, value):
        return self.assignment.count(value) == 0 and self.__check_diagonals((var, value))

    def add_assignment(self, var, value):
        self.assignment[var] = value

    def remove_assignment(self, var):
        self.assignment[var] = -1

    def __check_diagonals(self, house):
        for i in range(self.size // 2 + 1):
            for old_assignment in enumerate(self.assignment):
                if old_assignment[1] == -1:
                    continue

                if house[0] in [old_assignment[0] + i, old_assignment[0] - i] and \
                        house[1] in [old_assignment[1] + i, old_assignment[1] - i]:
                    return False
        return True


stopwatch = Stopwatch()

stopwatch.tic()
queen = QueenCSP(45)
result = queen.backtrack_search()
stopwatch.toc()
print("N = {};\ttime={}".format(8, stopwatch))
if result.success:
    print("result: {}".format(result.assignment))
    print(make_board(result.assignment))


