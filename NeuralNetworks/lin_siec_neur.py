from neuron import Neuron

example_set = [[3, 4, 3, 4, 5],
               [1, -2, 1, -2, -4],
               [4, 2, 5, 3, 2],
               [0, -1, 0, -3, -3]]
normalized_set = Neuron.normalize(example_set)
result = [[1, -1, 0.8, -0.8],
          [-1, 0.8, -0.8, 1],
          [0.8, -0.8, 1, -1]]

neuron1 = Neuron(input_data=normalized_set[0],
                 weights=Neuron.randomize_weights(-5, 5, len(normalized_set[0])),
                 expected_result=result[0][0])
neuron2 = Neuron(input_data=normalized_set[0],
                 weights=Neuron.randomize_weights(-5, 5, len(normalized_set[0])),
                 expected_result=result[1][0])
neuron3 = Neuron(input_data=normalized_set[0],
                 weights=Neuron.randomize_weights(-5, 5, len(normalized_set[0])),
                 expected_result=result[2][0])
neurons = [neuron1, neuron2, neuron3]

i = 0
generation = 1
while True:
    print(f"generation = {generation}")
    for j, neuron in enumerate(neurons, start=1):
        print(f"Wynik {j} neuronu dla wzorca {normalized_set[i]} jest {neuron.calculated_result}\n"
              f"wynik poprawny {neuron.expected_result} a wiec blad: {neuron.delta}")
    i = i + 1 if i < len(normalized_set) - 1 else 0
    for j in range(len(neurons)):
        neurons[j].recalculate_weights()
        neurons[j] = Neuron(input_data=normalized_set[i],
                            weights=neurons[j].weights,
                            expected_result=result[j][i])
    generation += 1
    yesno = input("Press 'x' to stop, 't' to test and any other key to continue learning..\n")
    if yesno == 'x':
        break

