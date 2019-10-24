from module.regression.linear import BatchLinearRegression
import pandas as pd
import numpy as np
from module.regression.normalizer import ZScore
from module.regression.regularization import l2_norm


def const_learning(iterations, cost):
    return 0.1


data: np.ndarray = pd.read_csv('res/datasets/wine.csv', header=None).values
training_data = data[:, :-1]
labels = data[:, -1]
normalizer = ZScore(training_data)

for i in range(10):
    model = BatchLinearRegression(training_data, labels,
                                  max_epoch=2**14,
                                  normalizer=normalizer,
                                  regularization_factor=0.00001 * (10**i),
                                  regularization=l2_norm).train()
    sample = np.array([6.0, 0.31, 0.47, 3.6, 0.067, 18.0, 42.0, 0.99549, 3.39, 0.66, 11.0])
    prediction = model.predict(sample)
    print("Iteration: {}\tResult = {}\t; Cost = {}\t".format(i, prediction, model.cost()))
    print("Model: {}".format(model))
