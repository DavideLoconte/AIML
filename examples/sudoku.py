import math
import sys

from constraint.constraint import CSPProblem
from utils.stopwatch import Stopwatch


def sudoku_pretty_print(table):
    print("┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓")
    for row_number, row in enumerate(table):
        print("┃", end="")
        for col_number, number in enumerate(row):
            if (col_number + 1) % 3 == 0:
                print(" " + str(number) + " ┃", end="")
            else:
                print(" " + str(number) + " │", end="")

        if (row_number + 1) % 3 == 0 and row_number != 8:
            print("\n┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫")
        elif row_number != 8:
            print("\n┠───┼───┼───╂───┼───┼───╂───┼───┼───┨")

    print("\n┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛")


class Sudoku(CSPProblem):

    def is_assignment_complete(self):
        for var in self.vars:
            if self.assignment.get(var) is None:
                return False
        return True

    def select_unassigned_variable(self):
        for var in self.vars:
            if self.assignment.get(var) is None:
                return var
        return None

    def is_assignment_consistent(self, var, value):
        for cell, number in self.assignment.items():
            if number == value:
                if (cell[0] == var[0] or cell[1] == var[1]):
                    return False
                if self.same_square(var, cell):
                    return False
        return True

    def same_square(self, cell_1, cell_2):
        left = math.floor(cell_1[0] / 3) * 3
        top = math.floor(cell_1[1] / 3) * 3
        if cell_2[0] in range(left, left + 3) and cell_2[1] in range(top, top + 3):
            return True
        return False

    def __init__(self, table):
        super().__init__()
        self.domain = list(range(1, 10))
        self.vars = []

        for i in range(9):
            for j in range(9):
                if table[i][j] != 0:
                    self.assignment[(i, j)] = table[i][j]
                else:
                    self.vars.append((i, j))


# ez_table = [
#     [8, 1, 0, 9, 0, 4, 0, 5, 7],
#     [7, 5, 3, 0, 0, 0, 9, 4, 6],
#     [0, 4, 9, 7, 0, 3, 8, 2, 0],
#
#     [1, 0, 6, 3, 9, 2, 4, 0, 5],
#     [0, 0, 0, 6, 0, 1, 0, 0, 0],
#     [9, 0, 4, 8, 7, 5, 1, 0, 2],
#
#     [0, 2, 7, 5, 0, 9, 6, 1, 0],
#     [3, 6, 1, 0, 0, 0, 5, 9, 4],
#     [5, 9, 0, 4, 0, 6, 0, 7, 3]
# ]

hard_table = [
    [3, 0, 0, 0, 0, 2, 0, 7, 0],
    [1, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 7, 9, 0, 0, 8, 1],

    [7, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [5, 4, 0, 0, 0, 0, 7, 0, 0],

    [9, 0, 0, 0, 6, 0, 5, 0, 8],
    [0, 0, 0, 1, 2, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 4]
]

hardest_table = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],

    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],

    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]


# void_table = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]


def main():
    table = hardest_table

    sudoku = Sudoku(
        table
    )
    stopwatch = Stopwatch()
    stopwatch.tic()
    res = sudoku.search()
    stopwatch.toc()
    print("Solved={}\ttime={}".format(res.success, stopwatch))

    if res.success:
        for coordinates, number in res.assignment.items():
            if table[coordinates[0]][coordinates[1]] == 0:
                table[coordinates[0]][coordinates[1]] = number
            else:
                if table[coordinates[0]][coordinates[1]] != number:
                    raise Exception("Algoritmo di ricerca sminchiato")

        sudoku_pretty_print(table)
    return 0


if __name__ == "__main__":
    sys.exit(main())
