import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.asarray(x)
    return np.asarray( 1/ (1 + np.exp(-x)))