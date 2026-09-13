input=[1000,8,9]
weight_matrix=[
    [5,0.35,-9],
    [20,0.5,6],
    [10,2.5,10]

]
biases = [1000, 200, 0]
def dot_product(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total
layer_outputs = []
for neuron_weights, neuron_bias in zip(weight_matrix, biases):
    neuron_output = dot_product(input, neuron_weights) + neuron_bias
    layer_outputs.append(neuron_output)
print(layer_outputs)