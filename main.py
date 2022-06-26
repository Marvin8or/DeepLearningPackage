from deep_learning_package_from_scratch.utilities import *
from deep_learning_package_from_scratch.datasets import generate_dummy_dataset
import numpy as np
        
if __name__ == "__main__":

    # Create dummy dataset
    AND_operation_recognition_dataset = generate_dummy_dataset(10, "XOR")
    print(AND_operation_recognition_dataset)
    
    # Build neural network
    simple_network = NeuralNetwork(2)
    simple_network.add_layer(number_of_neurons=5, activation_function="ReLU")
    simple_network.add_layer(number_of_neurons=4, activation_function="ReLU")
    simple_network.add_layer(number_of_neurons=3, activation_function="ReLU")
    simple_network.add_layer(number_of_neurons=2, activation_function="ReLU")

    # Print network layout
    simple_network.print_layout()

    # Feed forward
    X, y = AND_operation_recognition_dataset[0, :2], AND_operation_recognition_dataset[0, 2]
    first_input = np.array([X]).T
    first_output = np.array([y]).T

    print(f"input: {first_input}")
    output = simple_network.feed_forward(first_input)
    print(f"output: {output}")

    dC_dw, dC_db = simple_network.back_propagation(first_output)
    print(dC_dw)

    
    