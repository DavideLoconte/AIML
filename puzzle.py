from modules import graph


class Puzzle(graph.Graph):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def __init__(self, table):
        super().__init__()
        solution1 = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 0)
        )
        solution2 = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8)
        )
        self.solutions.append(solution1)
        self.solutions.append(solution2)
        self.add_node(solution1)
        self.add_node(solution2)
        self.add_node(table)
        self.set_starting_node(table)
        self.visited = set()

    @staticmethod
    def get_hole_position(table):
        for row in table:
            for number in row:
                if number == 0:
                    return tuple([table.index(row), row.index(number)])
        raise Exception("Cannot find hole, table = {}".format(str(table)))

    @staticmethod
    def __tuple_sum(a, b):
        if len(a) != 2 or len(b) != 2:
            raise Exception("Wrong tuple format")
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
        row0 = tuple(lst[0])
        row1 = tuple(lst[1])
        row2 = tuple(lst[2])
        return tuple((row0, row1, row2))

    @staticmethod
    def move(table, direction):
        current_position = Puzzle.get_hole_position(table)
        new_position = Puzzle.__tuple_sum(current_position, direction)
        if new_position[0] in range(3) and new_position[1] in range(3):
            return Puzzle.__swap(table, current_position, new_position)
        else:
            return table

    @staticmethod
    def is_table_valid(table):
        if len(table) != 3:
            print("Warning, invalid col size")
            return False
        for row in table:
            if len(row) != 3:
                print("Warning, invalid row size")
                return False
        return True

    # Override
    def successor(self, node):
        if node is None:
            node = self.starting_node

        if node in self.visited:
            return []
        moves = [
            self.move(node, Puzzle.UP),
            self.move(node, Puzzle.DOWN),
            self.move(node, Puzzle.LEFT),
            self.move(node, Puzzle.RIGHT)
        ]
        while node in moves:
            moves.remove(node)

        result = []
        for successor in moves:
            path = tuple((node, successor))
            result.append([successor, 1])
        return result
