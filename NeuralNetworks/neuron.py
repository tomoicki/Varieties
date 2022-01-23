import random
from math import exp


class Neuron:
    learning_factor = 0.1

    def __init__(self, input_data, weights, expected_result=0):
        self.input_data = input_data
        self.weights = weights
        self.expected_result = expected_result
        # hokus-pokus
        self.learning_factor = self.learning_factor
        # calculations
        self.calculate_results()

    def calculate_results(self):
        if hasattr(self.input_data, '__iter__'):
            unactivated_value = sum([value * weight for value, weight in zip(self.input_data, self.weights)])
        else:
            unactivated_value = self.input_data * self.weights
        activated_value = Neuron.activation_function(unactivated_value)
        self.calculated_result = activated_value
        self.delta = self.expected_result - self.calculated_result

    def recalculate_weights(self):
        if hasattr(self.input_data, '__iter__'):
            self.weights = [weight + self.learning_factor * self.delta * value for weight, value
                            in zip(self.weights, self.input_data)]
        else:
            self.weights = self.weights + self.learning_factor * self.delta * self.input_data

    def reclock_weight_and_reproduce(self):
        self.recalculate_weights()
        return Neuron(input_data=self.input_data,
                      weights=self.weights,
                      expected_result=self.expected_result)

    def show(self):
        print(f"values: {self.input_data}\n"
              f"weights: {self.weights}\n"
              f"calculated result: {self.calculated_result}\n"
              f"expected result: {self.expected_result}\n"
              f"delta: {self.delta}\n")

    @staticmethod
    def activation_function(input_value):
        return input_value

    @staticmethod
    def bipolar_function(input_value):
        return 2 / (1 + exp(-input_value)) - 1

    @staticmethod
    def sigmoid_function(input_value):
        return 1 / (1 + exp(-input_value))

    @staticmethod
    def tangensoid_function(input_value):
        return (1 - exp(-input_value)) / (1 + exp(-input_value))

    @staticmethod
    def threshold_function(input_value, threshold=0, upper_value=1, bottom_value=-1):
        return upper_value if input_value >= threshold else bottom_value

    @staticmethod
    def normalize(unnormalized_set):
        norm = [sum([value ** 2 for value in row]) ** 0.5 for row in unnormalized_set]
        return [[value / norm for value in row] for row, norm in zip(unnormalized_set, norm)]

    @staticmethod
    def randomize_weights(bottom_value, upper_value, length):
        return [random.uniform(bottom_value, upper_value) for _ in range(length)]
