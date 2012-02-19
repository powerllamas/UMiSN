from random import random
import sys
'''
Simple NN generator - given number of neurons in each layer it generates feed-forward network in f1 notation, with random weights.
First layer is input layer: all neurons in this layer have no inputs, therefore number of neurons in the first layer is equal to number of inputs of the network.
'''
def generate(neuron_type, layers):        
    print "\nX",
    inputs_no = 0  
    for layer, layer_size in enumerate(layers):
        if(layer > 0):
            inputs_no = layers[layer - 1]
        first_input = 1
        for neuron in range(layer_size):
            print "[%s" % (neuron_type, ),
            for input_neuron in range(first_input, first_input + inputs_no):
                weight = random()
                print ", %d:%f" % (-input_neuron, weight),
            print "]",
            first_input +=  1
            

if __name__ == '__main__':
    layers = [int(c) for c in sys.argv[1:]]
    print layers
    neuron_type = "Nu"
    for i in range(0,2):
        generate(neuron_type, layers)
