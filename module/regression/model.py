import numpy as np
from .regularization import l2_norm


class Model:

    # Public methods

    def train(self):
        for i in range(self.max_epoch):
            alpha = self.learning_rate(i, self.cost()) if self.learning_rate is not None else 0.1
            self.hypothesis -= alpha * self._update()
            if self.regularization is not None:
                self.hypothesis -= self.regularization_factor * self.regularization(self.hypothesis)
        return self

    def predict(self, sample):
        return self._predict_function(self._prepare_data(sample))

    # Abstract

    def cost(self):
        raise NotImplementedError

    def _predict_function(self, data):
        raise NotImplementedError

    # Protected

    def _update(self):
        prediction = self._predict_function(self.training_set)
        return np.dot((prediction - self.labels), self.training_set) / self.rows

    def _add_costant_feature(self, sample):
        if sample.ndim == 1:
            sample = np.insert(sample, 0, 1.0)
        elif sample.ndim == 2:
            sample = np.insert(sample, 0, np.ones(len(sample)), axis=1)
        else:
            raise Exception("Wrong data format")
        return sample

    def _normalize_data(self, data):
        if self.normalizer is not None:
            return self.normalizer.normalize(data)
        else:
            return data

    def _prepare_data(self, data):
        return self._add_costant_feature(self._normalize_data(data))

    # Constructor and overloading

    def __init__(self, training_set: np.ndarray, labels: np.ndarray, normalizer=None,
                 learning_rate=None, max_epoch=2**16, regularization_factor=0, regularization=l2_norm):

        self.regularization_factor = regularization_factor
        self.regularization = regularization
        self.normalizer = normalizer
        self.labels = labels
        self.training_set = self._prepare_data(training_set)
        self.rows, self.columns = self.training_set.shape

        if self.rows != len(self.labels):
            raise Exception("Wrong format")

        self.hypothesis = np.random.rand(self.columns)
        self.learning_rate = learning_rate
        self.max_epoch = max_epoch

    def __repr__(self):
        return self.hypothesis.__repr__()
