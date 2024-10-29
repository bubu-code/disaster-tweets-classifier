import numpy as np

def sigmoid(t):
  """Implements the sigmoid activation function"""
  return 1 / (1 + np.exp(-t))
