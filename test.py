from puzzle import Puzzle
from modules.search import *
import time


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
            cell = node.node[row][col]
            if cell == 0:
                continue
            target_row = (cell - 1) // 3
            target_col = (cell - 1) % 3
            cost += abs(target_row - row) + abs(target_col - col)
    return cost


puzzle = Puzzle((
   (1, 8, 2),
   (0, 4, 3),
   (7, 6, 5)
))
# puzzle = Puzzle((
#     (8, 0, 6),
#     (5, 4, 7),
#     (2, 3, 1)
# ))
#
# puzzle = Puzzle((
#      (1, 2, 3),
#      (4, 5, 6),
#      (7, 0, 8)
# ))

#print(h1(puzzle.starting_node))

#
#
# start = time.process_time_ns()
# print("Breadth First:")
# result = BreadthFirst(puzzle).search()
# elapsed = (time.process_time_ns() - start) / 1000000.0
# if not result.get("success"):
#     print("Solution not found:\telasped_time = {} ms".format(elapsed))
# else:
#     print("Solved:\telasped_time = {} ms".format(elapsed))
# depth = result.get("depth")
# print("      \tdepth = {}".format(depth))
#
# start = time.process_time_ns()
# print("Depth First:")
# result = DepthFirst(puzzle).search()
# elapsed = (time.process_time_ns() - start) / 1000000.0
# print("Solved:\telasped_time = {} ms".format(elapsed))
# depth = result.get("depth")
# print("      \tdepth = {}".format(depth))
#
# start = time.process_time_ns()
# print("Uniform cost:")
# result = Uniform(puzzle).search()
# elapsed = (time.process_time_ns() - start) / 1000000.0
# if not result.get("success"):
#     print("Solution not found:\telasped_time = {} ms".format(elapsed))
# else:
#     print("Solved:\telasped_time = {} ms".format(elapsed))
# depth = result.get("depth")
# print("      \tdepth = {}".format(depth))
#
# start = time.process_time_ns()
# print("Limited depth:")
# result = LimitedDepth(puzzle, 100).search()
# elapsed = (time.process_time_ns() - start) / 1000000.0
# if not result.get("success"):
#     print("Solution not found:\telasped_time = {} ms".format(elapsed))
# else:
#     print("Solved:\telasped_time = {} ms".format(elapsed))
# depth = result.get("depth")
# print("      \tdepth = {}".format(depth))
#
start = time.process_time_ns()
print("Iterative depth:")
result = AStar(puzzle, heuristic=h1).search()
elapsed = (time.process_time_ns() - start) / 1000000.0
if not result.get("success"):
    print("Solution not found:\telasped_time = {} ms".format(elapsed))
else:
    print("Solved:\telasped_time = {} ms".format(elapsed))
depth = result.get("depth")
print("      \tdepth = {}".format(depth))
#
#
#
