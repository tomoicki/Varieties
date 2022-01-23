from neuron import Neuron

example_set = [[2, 2, 2, 2, 2],
               [-2, -2, -2, -2, -2],
               [1, 1, -1, -1, -1],
               [-1, -1, 1, 1, 1]]
normalized_set = Neuron.normalize(example_set)
result = [1, -1, 0.8, -0.8]

neuron = Neuron(input_data=normalized_set[0],
                weights=[-0.1, 0.2, -0.5, 0.3, -0.4],
                expected_result=result[0])
neuron.show()

i = 1
generation = 1
while True:
    neuron.recalculate_weights()
    neuron = Neuron(input_data=normalized_set[i],
                    weights=neuron.weights,
                    expected_result=result[i])
    print(f"Generation = {generation}")
    neuron.show()
    i = i + 1 if i < len(normalized_set) - 1 else 0
    generation += 1
    yesno = input("Press 'x' to stop, 't' to test latest specimen and any other key to continue learning..\n")
    if yesno == 'x':
        break
    elif yesno == 't':
        testing_values = []
        print("Give new values to test on current weights.")
        for i, _ in enumerate(normalized_set[0], start=1):
            testing_value = float(input("Value nr " + str(i) + ": "))
            testing_values.append(testing_value)
        testing_result = float(input("Whats ur expected result: "))
        test_specimen = Neuron(input_data=testing_values,
                               weights=neuron.weights,
                               expected_result=testing_result)
        test_specimen.generation = 'Test generation'
        test_specimen.show()
        break
    else:
        continue
