from tree.search import *
from utils.stopwatch import Stopwatch
from time import sleep

from datamodel import graph


class Puzzle(graph.Graph):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def __init__(self, table):
        super().__init__()
        solution = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 0))
        self.solutions.append(solution)
        self.add_node(solution)
        self.add_node(table)
        self.set_starting_node(table)

    @staticmethod
    def _get_hole_position(table):
        for row in table:
            for number in row:
                if number == 0:
                    return tuple([table.index(row), row.index(number)])
        raise Exception("Cannot find hole, table = {}".format(str(table)))

    @staticmethod
    def __tuple_sum(a, b):
        if len(a) != 2 or len(b) != 2:
            raise Exception("Wrong coordinate format")
        return tuple((
            a[0] + b[0],
            a[1] + b[1]
        ))

    @staticmethod
    def __swap(table: tuple, a: tuple, b: tuple):
        lst = list()
        for row in table:
            lst.append(list(row))
        lst[a[0]][a[1]],  lst[b[0]][b[1]] = lst[b[0]][b[1]],  lst[a[0]][a[1]]
        mixed_list = []
        for row in lst:
            mixed_list.append(tuple(row))
        return tuple(mixed_list)

    @staticmethod
    def _move(table, direction):
        current_position = Puzzle._get_hole_position(table)
        new_position = Puzzle.__tuple_sum(current_position, direction)
        if new_position[0] in range(3) and new_position[1] in range(3):
            return Puzzle.__swap(table, current_position, new_position)
        else:
            return table

    @staticmethod
    def _is_table_valid(table):
        if len(table) != 3:
            print("Warning, invalid col size")
            return False
        for row in table:
            if len(row) != 3:
                print("Warning, invalid row size")
                return False
        return True

    def successor(self, node):
        if node is None:
            node = self.starting_node

        moves = [
            self._move(node, Puzzle.UP),
            self._move(node, Puzzle.DOWN),
            self._move(node, Puzzle.LEFT),
            self._move(node, Puzzle.RIGHT)
        ]
        while node in moves:
            moves.remove(node)
        result = []
        for successor in moves:
            result.append([successor, 1])
        return result


# Fast function to print current table
def print_puzzle_table(x):
    print("╔═══╦═══╦═══╗")
    for idx, row in enumerate(x):
        for number in row:
            if number == 0:
                print("║ █ ", end="")
            else:
                print("║ {} ".format(number), end="")
        if idx != 2:
            print("║\n╠═══╬═══╬═══╣")
        else:
            print("║\n╚═══╩═══╩═══╝\n")



def h1(node):
    cost = 0
    for col in range(3):
        for row in range(3):
            cell = node.content[row][col]
            if cell == 0:
                continue
            target_row = (cell - 1) // 3
            target_col = (cell - 1) % 3
            cost += abs(target_row - row) + abs(target_col - col)
    return cost


easy_table = (
   (1, 8, 2),
   (0, 4, 3),
   (7, 6, 5)
)

hard_table = (
    (8, 0, 6),
    (5, 4, 7),
    (2, 3, 1)
)


def main():
    puzzle = Puzzle(hard_table)
    stopwatch = Stopwatch()
    stopwatch.tic()
    print("Searching A*")
    result = AStar(puzzle, h1).search()
    stopwatch.toc()
    for path in result.path:
        sleep(0.25)
        print_puzzle_table(path)

    print("Depth = " + str(result.depth))
    print("Cost = " + str(result.cost))
    print("Time = " + str(stopwatch))
    return 0


if __name__ == "__main__":
    sys.exit(main())
