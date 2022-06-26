import numpy as np
from operator import xor

def generate_dummy_dataset(number_of_samples, operation="AND"):
    """
    Generates a dummy dataset to test various stages of the network developement
    number_of_samples represents the number of rows in the dataset
    operation represents the output of each row

    Example

    >>> AND_dataset = generate_dummy_dataset(5, operation="AND")
    >>> AND_dataset
    [[1, 0, False]
     [0, 0, True]
     [1, 1, True]
     [0, 1, False]
     [1, 1, True]]
    
    """

    #TODO create decorator
    def and_function(x, y):
        return x and y
    
    def or_function(x, y):
        return x or y

    operations = {"AND": and_function, 
                  "OR": or_function, 
                  "XOR": xor}

    dummy_dataset = np.zeros(shape=(number_of_samples, 3))
    for row in range(number_of_samples):
        np.random.seed(row)
        x, y = np.random.randint(0, 1 + 1), np.random.randint(0, 1 + 1)
        result = operations[operation](x, y)

        dummy_dataset[row][0], dummy_dataset[row][1], dummy_dataset[row][2] = x, y, result 
    
    return dummy_dataset