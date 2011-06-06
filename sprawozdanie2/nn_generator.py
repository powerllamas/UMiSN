from random import random

inputs_no = 0
layers = [4, 3, 3]
neuron_type = "N"

print "X"
first_input = 0
for layer, layer_size in enumerate(layers):
    if(layer > 0):
        inputs_no = layers[layer - 1]
    for neuron in range(layer_size):
        print "[%s" % (neuron_type, ),
        for input_neuron in range(first_input, first_input + inputs_no):
            weight = random()
            print ", %d:%f" % (input_neuron, weight),
        print "]"
    first_input +=  inputs_no
            
