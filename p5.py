import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

# X =[[1, 2, 3, 2.5],
#     [2.0, 5.0, -1.0, 2.0],
#     [-1.5, 2.7, 3.3, -0.8]]

X, y = spiral_data(100,3)

class Layer_Dens:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)# To prevent transposing
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights + self.biases)

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.expt(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(expt_values, axis=1, keepdims=True)
        self.output = probabilities
 
layer1 = Layer_Dens(2, 5)
activation1 = Activation_ReLU()
layer1.forward(X)
#print(layer1.output)
activation1.forward(layer1.output)
# layer2 = Layer_Dens(5, 2)
print(activation1.output)