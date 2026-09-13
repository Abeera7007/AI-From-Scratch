def dot_product(a,b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


inputs  = [1200, 3, 5]
weights = [0.5, 200, -10]
bias = 1000
neuron_output = dot_product(inputs, weights) + bias
print(neuron_output)