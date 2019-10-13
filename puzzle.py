from module.datamodel import graph


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
