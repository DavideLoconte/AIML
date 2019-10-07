from puzzle import Puzzle
from modules.tree import TreeSearch, fifo, lifo, least_cost
import time


# Fast function to print current table
def print_puzzle_table(x):
    print("═════════")
    for row in x:
        for number in row:
            if number==0:
                print("║-║", end="")
            else:
                print("║{}║".format(number), end="")
        print("\n═════════")
    print("\n\n\n")


print("Starting puzzle:")
puzzle = Puzzle((
    (1, 8, 2),
    (0, 4, 3),
    (7, 6, 5)
))
print_puzzle_table(puzzle.starting_node)

start = time.process_time_ns()
print("\nSolving with breadth-first")
fifo_result = TreeSearch(puzzle).search(fifo)
elapsed = (time.process_time_ns() - start) / 1000000.0
print("Solved:\telasped_time = {} ms".format(elapsed))
depth = fifo_result.get("depth")
print("      \tdepth = {}".format(depth))


start = time.process_time_ns()
print("\nSolving with uniform cost (least cost)")
lc_result = TreeSearch(puzzle).search(least_cost)
elapsed = (time.process_time_ns() - start) / 1000000.0
print("Solved:\telasped_time = {} ms".format(elapsed))
print("      \tdepth = {}".format(lc_result.get("depth")))

print("Printing result:")
for tab in lc_result.get("path"):
    print_puzzle_table(tab)
