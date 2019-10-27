from .model import Model
import numpy as np


class LogisticRegression(Model):

    def cost(self):
        prediction = self._predict_function(self.training_set)
        first_class_cost = np.dot(self.labels, np.log(prediction))
        second_class_cost = np.dot(1 - self.labels, np.log(1 - prediction))
        return (-1) * (first_class_cost + second_class_cost) / self.rows

    # Override

    def _predict_function(self, data):
        x = np.dot(data, self.hypothesis)
        return 1 / (1 + np.exp(-x))
