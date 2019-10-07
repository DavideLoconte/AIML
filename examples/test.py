from graph import Graph
from tree import TreeSearch, fifo, lifo, least_cost

graph = Graph()
# graph.add_path(("A", "B"), 3, True)
# graph.add_path(("A", "G"), 2, True)
# graph.add_path(("A", "E"), 1, True)
# graph.add_path(("B", "G"), 1, True)
# graph.add_path(("C", "B"), 1, True)
# graph.add_path(("C", "I"), 2, True)
# graph.add_path(("C", "J"), 3, True)
# graph.add_path(("C", "D"), 4, True)
# graph.add_path(("D", "J"), 1, True)
# graph.add_path(("I", "J"), 2, True)
# graph.add_path(("I", "H"), 1, True)
# graph.add_path(("H", "C"), 1, True)
# graph.add_path(("H", "G"), 2, True)
# graph.add_path(("G", "F"), 1, True)
# graph.add_path(("F", "E"), 1, True)
# graph.add_path(("F", "A"), 2, True)
# graph.add_path(("E", "F"), 1, True)

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")

graph.add_path(("A", "D"),5)
graph.add_path(("A", "B"))
graph.add_path(("A", "E"))
graph.add_path(("B", "E"))
graph.add_path(("D", "C"))
graph.add_path(("F", "E"))

graph.solutions = ["C"]
graph.set_starting_node("A")

print("FIFO: " + str(TreeSearch(graph).search(fifo)))
print("LIFO: " + str(TreeSearch(graph).search(lifo)))
print("LEAST_COST: " + str(TreeSearch(graph).search(least_cost)))



