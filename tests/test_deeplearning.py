#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_deeplearning
----------------------------------

Tests for `deeplearning` module.
"""

import pytest
import numpy as np
from click.testing import CliRunner

from deeplearning import functions, network
from deeplearning import cli


@pytest.fixture
def my_network():
    return network.NeuralNetwork(2)

def test_network_initalization_parameters():

    test_network = network.NeuralNetwork(5)
    assert test_network.weight_initialization == "Normal"
    assert test_network.neurons_in_input_layer == 5
    assert isinstance(test_network._NeuralNetwork__network_layout, list)
    assert isinstance(test_network._NeuralNetwork__weights, list)
    assert isinstance(test_network._NeuralNetwork__biases, list)
    assert isinstance(test_network._NeuralNetwork__weighted_inputs, list)
    assert isinstance(test_network._NeuralNetwork__layer_node_values, list)

    assert test_network._NeuralNetwork__network_layout[0]["name"] == "input_layer"
    assert test_network._NeuralNetwork__network_layout[0]["number_of_neurons"] == 5

    assert test_network._NeuralNetwork__number_of_layers == 1

def test_error_raised_on_initialization():

    # Must be tested that the class raises error if zero or negative value is passed to constructor

    with pytest.raises(ValueError) as value_error:
        test_network = network.NeuralNetwork(-1)

    with pytest.raises(ValueError) as value_error:
        test_network = network.NeuralNetwork(0)

def test_feed_forward_output(my_network):

    """
    Must be tested that the feed_forward functions algorithm computes the 
    matrices the right way and with right matrix shapes
    """

    def mock_initialize_weight_and_biases(rows, columns):
        mock_weights = np.ones(shape=(rows, columns))
        mock_biases = np.ones(shape=(rows, 1))
        return mock_weights, mock_biases

    # Monkey patch to control initialized weigths and biases to be 1s
    my_network._NeuralNetwork__initialize__weights_and__biases = mock_initialize_weight_and_biases
    my_network.add_layer(5, "ReLU")
    my_network.add_layer(4, "ReLU")
    my_network.add_layer(3, "ReLU")
    my_network.add_layer(2, "ReLU")


    output = my_network.feed_forward(np.array([[0, 0]]).T)

    assert np.array_equal(np.array([[76, 76]]).T, output)

def test_back_propagation_output():
    pass




# def test_command_line_interface():
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'deeplearning.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
