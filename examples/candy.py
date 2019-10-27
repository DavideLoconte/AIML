from regression.logistic import LogisticRegression
import pandas as pd
import numpy as np

from regression.normalizer import ZScore


def const_learning(iterations, cost):
    return 0.01


data: np.ndarray = pd.read_csv('res/datasets/candy_1.csv', header=None).values
training_data = data[:, :-1]
labels = data[:, -1]
normalizer = ZScore(training_data)
sample = np.array((0, 0, 0, 1, 0, 0, 1, 0.87199998, 0.84799999, 49.524113))


for i in range(10):
    model = LogisticRegression(training_data, labels,
                               max_epoch=2**20, normalizer=normalizer, learning_rate=const_learning).train()
    print("Iteration: {}\tResult = {}\t; Cost = {}\t".format(i, model.predict(sample), model.cost()))
    print("Model: {}".format(model))
