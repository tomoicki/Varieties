from neuron import Neuron
from math import sin

# Neuron.activation_function = Neuron.tangensoid_function
Neuron.activation_function = Neuron.bipolar_function

x_list = [0.4 * i for i in range(14)]
neurons = []
for x in x_list:
    neuron = Neuron(input_data=x,
                    weights=Neuron.randomize_weights(-5, 5, 1)[0],
                    expected_result=sin(x))
    neurons.append(neuron)

generation = 1
while True:
    print(f"generation = {generation}")
    for j, neuron in enumerate(neurons, start=1):
        print(f"Wynik {j} neuronu dla wagi {neuron.weights} jest {neuron.calculated_result} "
              f"wynik poprawny {neuron.expected_result} a wiec blad: {neuron.delta}")
    for j in range(len(neurons)):
        neurons[j].recalculate_weights()
        neurons[j] = Neuron(input_data=neurons[j].input_data,
                            weights=neurons[j].weights,
                            expected_result=neurons[j].expected_result)
    generation += 1
    yesno = input("Press 'x' to stop, 't' to test and any other key to continue learning..\n")
    if yesno == 'x':
        break
