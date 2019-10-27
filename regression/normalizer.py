import numpy as np


class Normalizer:
    def __init__(self, dataset):
        self.dataset = dataset
        self.rows, self.columns = self.dataset.shape


class ZScore(Normalizer):
    def __init__(self, dataset):
        super().__init__(dataset)
        self.mean = np.mean(dataset, axis=0)
        self.std = np.std(dataset, axis=0)

    def normalize(self, data):
        return (data - self.mean) / self.std


# TODO
class MinMax(Normalizer):
    def __init__(self, dataset):
        super().__init__(dataset)
        raise NotImplementedError

    def normalizer(self, data):
        raise NotImplementedError
