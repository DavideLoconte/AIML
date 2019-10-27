import time


class Stopwatch:
    """
    Simple class to measure time
    Automatically format time if converted to string
    """
    def __init__(self):
        self.time = 0.0

    def tic(self):
        """
        Start time
        """
        self.time = time.time_ns()

    def toc(self):
        """
        Stop time
        """
        self.time = time.time_ns() - self.time

    def measure(self, function):
        """
        Measure time of execution of a function
        :param function: Callable to execute
        :return self: You can call get_ns, get_ms or get_sec to get execution time
        """
        self.tic()
        function()
        self.toc()
        return self

    def get_ns(self):
        """
        :return: time in nanoseconds
        """
        return self.time

    def get_ms(self):
        """
        :return: time in milliseconds
        """
        return self.time / 1000000.0

    def get_sec(self):
        """
        :return: time in seconds
        """
        return self.get_ms() / 1000.0

    def __hash__(self):
        return self.time.__hash__()

    def __eq__(self, other):
        return self.time == other.time

    def __lt__(self, other):
        return self.time < other.time

    def __repr__(self):
        if self.get_ns() < 1000000:
            return "{} ns".format(self.get_ns())
        elif self.get_ms() < 1000:
            return "{} ms".format(self.get_ms())
        else:
            return "{} s".format(self.get_sec())
