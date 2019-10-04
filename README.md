# AIML
Python modules from Articial Intelligence course at Polytechinic of Bari.

## Graph
Graph module _graph.py_ contains class Graph which abstracts the logic for building graphs.
You can instantiate a new graph with:

```
graph = Graph()
```

Methods graph.add_nodes(node: str) and graph.add_path(path: tuple, cost: int) are used to build the graph.
Implementation of methods to modify the graph are available as well.
In order to fully exploit the functionality of graph search, user has to correctly set
graph.solutions=[list of str] and graph.starting=str.

## Tree Search
Tree search module exposes the class TreeSearch which enables alghoritm to find a path to starting
node to ending node by simply calling:

```
TreeSearch(graph).search(node_selector_algorithm)
```
Algorithm for node selection available are: fifo, lifo and least cost. The function returns to a list representing
a path from starting node to a valid solution, False if none is found.
