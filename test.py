from puzzle import Puzzle
from modules.search import Uniform
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


print("Starting puzzle:")
puzzle = Puzzle((
    (1, 8, 2),
    (0, 4, 3),
    (7, 6, 5)
))

start = time.process_time_ns()
print("\nSolving with breadth-first")
fifo_result = Uniform(puzzle).search()
elapsed = (time.process_time_ns() - start) / 1000000.0
print("Solved:\telasped_time = {} ms".format(elapsed))
depth = fifo_result.get("depth")
print("      \tdepth = {}".format(depth))

for element in fifo_result.get("path"):
    print_puzzle_table(element)
