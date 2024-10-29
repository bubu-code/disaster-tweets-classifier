import numpy as np

class LogisticRegression:
  def __init__(self):
    self.weights = np.random.randn(2, 1)
    self.bias = 0
