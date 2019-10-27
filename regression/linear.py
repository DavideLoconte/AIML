import numpy as np
import sys
from .model import Model


class BatchLinearRegression(Model):

    # Public

    def cost(self):
        return 0.5 * np.mean((self._predict_function(self.training_set) - self.labels) ** 2)

    # Protected

    def _predict_function(self, data):
        return np.dot(data, self.hypothesis)
