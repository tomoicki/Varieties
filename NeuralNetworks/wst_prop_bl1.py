from neuron import Neuron

example_set = [[0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1],
               [1, 1, 0, 0, 0],
               [1, 0, 1, 0, 1]]
result = [1, 0, 0.3, 0.7]


class Hidden(Neuron):
    pass


Hidden.activation_function = Hidden.sigmoid_function
hidden1 = Hidden(input_data=example_set[0],
                 weights=[4, -3, 0.5, 1, 0.7])
hidden2 = Hidden(input_data=example_set[0],
                 weights=[3, 0.5, -2, 0.7, 1])
outer = Neuron(input_data=[hidden1.calculated_result, hidden2.calculated_result],
               weights=[-0.4, -2],
               expected_result=result[0])

i = 1
generation = 1
while True:
    print(f"generation = {generation}")
    hidden1.recalculate_weights()
    print(hidden1.weights)
    hidden1 = Hidden(input_data=example_set[i],
                     weights=hidden1.weights)
    hidden2.recalculate_weights()
    hidden2 = Hidden(input_data=example_set[i],
                     weights=hidden2.weights)
    outer.recalculate_weights()
    outer = Neuron(input_data=[hidden1.calculated_result, hidden2.calculated_result],
                   weights=outer.weights,
                   expected_result=result[i])
    print(f"Błąd na {i+1} wzorcu wynosi {outer.delta}")
    i = i + 1 if i < len(example_set) - 1 else 0
    generation += 1
    yesno = input("Press 'x' to stop, 't' to test and any other key to continue learning..\n")
    if yesno == 'x':
        break

