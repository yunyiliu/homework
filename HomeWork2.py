import numpy as np
from pip._vendor.msgpack.fallback import xrange

def mse_loss(y_true, y_pred):
    # y_true and y_pred are numpy arrays of the same length
    return ((y_true - y_pred) ** 2).mean()

def relu(x):
    A = np.maximum(0, x)
    return A, x

def deriv_relu(x):
    # Derivative of relu:
    fx = x.relu(x)
    if fx > 0:
       return 1
    else:
       return 0
       
def deriv_nonlin(x):
    return x * (1 - x)

def nonlin(x):
    # activation function: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)

syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

for j in xrange(60000):

    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    l2_error = mse_loss(y, l2)

    if (j % 10000) == 0:
        print("L2_Error:" + str(np.mean(np.abs(l2_error))))

    l2_delta = l2_error * deriv_nonlin(l2)

    l1_error = l2_delta.dot(syn1.T)

    if (j % 10000) == 0:
        print("L1_Error:" + str(np.mean(np.abs(l1_error))))

    l1_delta = l1_error * deriv_nonlin(l1)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
