from puzzle import Puzzle
from module.tree.search import *
from module.utils.stopwatch import Stopwatch
from time import sleep


# Fast function to print current table
def print_puzzle_table(x):
    print("═════════")
    for row in x:
        for number in row:
            if number == 0:
                print("║-║", end="")
            else:
                print("║{}║".format(number), end="")
        print("\n═════════")
    print("\n\n\n")


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

puzzle = Puzzle(hard_table)
stopwatch = Stopwatch()


stopwatch.tic()
print("Searching A*")
result = AStar(puzzle, h1).search()
stopwatch.toc()

for path in result.path:
    print("\n" * 99)
    print_puzzle_table(path)
    sleep(0.5)


print("Depth = " + str(result.depth))
print("Cost = " + str(result.cost))
print("Time = " + str(stopwatch))
