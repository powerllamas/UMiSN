from random import random

'''
Simple NN generator - given number of neurons in each layer it generates feed-forward network in f1 notation, with random weights.
First layer is input layer: ale neurons in this layer have no inputs, therefore number of neurons in the first layer is equal to number of inputs of the network.
'''
def generate(neuron_type, layers):        
    print "X"
    inputs_no = 0
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
            

if __name__ == '__main__':
    layers = [3, 4, 3]
    neuron_type = "N"
    generate(neuron_type, layers)
