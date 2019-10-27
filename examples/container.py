import sys
from constraint.constraint import CSPProblem
from utils.stopwatch import Stopwatch


class ContainerAssignment(CSPProblem):

    def is_assignment_complete(self):
        for category, items in self.products.items():
            for item in items:
                if self.assignment.get(item) is None:
                    return False
        return True

    def select_unassigned_variable(self):
        for category, items in self.products.items():
            for item in items:
                if self.assignment.get(item) is None:
                    return item
        return None

    def is_assignment_consistent(self, var, value):

        if list(self.assignment.values()).count(value) == self.capacity:
            return False

        if var in self.products.get("explosives"):
            for explosive in self.products.get("explosives"):
                if self.assignment.get(explosive) == value:
                    return False

        elif var in self.products.get("edibles"):
            for waste in self.products.get("wastes"):
                if self.assignment.get(waste) == value:
                    return False

        elif var in self.products.get("wastes"):
            for edible in self.products.get("edibles"):
                if self.assignment.get(edible) == value:
                    return False

        elif var in self.products.get("frozen"):
            for frozen in self.products.get("frozen"):
                if self.assignment.get(frozen) is not None and self.assignment.get(frozen) != value:
                    return False
            for fresh in self.products.get("fresh"):
                if self.assignment.get(fresh) == value:
                    return False

        elif var in self.products.get("fresh"):
            for frozen in self.products.get("frozen"):
                if self.assignment.get(frozen) == value:
                    return False
            pass

        return True

    def __init__(self, n_containers, capacity, wastes, edibles, explosives,
                 frozen, fresh):
        super().__init__()
        self.n_containers = n_containers
        self.domain = list(range(n_containers))
        self.capacity = capacity
        self.products = {
            "wastes": wastes,
            "edibles": edibles,
            "explosives": explosives,
            "frozen": frozen,
            "fresh": fresh,
        }

    def __repr__(self):
        all_cont = [[] for i in range(self.n_containers)]
        result = ""
        for item, cont in self.assignment.items():
            all_cont[cont].append(item)
        for number, content in enumerate(all_cont):
            result += "Container {}:\t".format(number)
            for item in content:
                result += "{}; ".format(item)
            result += "\n"
        return result


def main():
    containers = 6
    capacity = 6
    wastes = ['t{}'.format(i) for i in range(4)]
    explosive = ['e{}'.format(i) for i in range(4)]
    frozen = ['fz{}'.format(i) for i in range(5)]
    fresh = ['fs{}'.format(i) for i in range(6)]
    edibles = ['f{}'.format(i) for i in range(6)]

    stopwatch = Stopwatch()
    stopwatch.tic()
    container = ContainerAssignment(containers, capacity, wastes, edibles, explosive, frozen, fresh)
    result = container.backtrack_search()
    stopwatch.toc()
    print("N = {};\ttime={}".format(4, stopwatch))
    print(container)
    return 0


if __name__ == "__main__":
    sys.exit(main())
