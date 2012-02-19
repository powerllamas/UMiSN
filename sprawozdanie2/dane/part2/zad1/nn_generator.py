from random import random
import sys
'''
Simple NN generator 
Given number of neurons in each layer it generates feed-forward network in f1 notation, with random weights.
First layer is input layer: number of neurons in the first layer is equal to number of inputs of the network.
'''
def generate(neuron_type, layers):        
    print"""org:
name: Anonymous framstick
genotype:~"""
    genotype = "X"
    inputs_no = 0  
    for layer, layer_size in enumerate(layers):
        if(layer > 0):
            inputs_no = layers[layer - 1]
        first_input = 1
        for neuron in range(layer_size):
            genotype += "[%s" % (neuron_type)
            for input_neuron in range(first_input, first_input + inputs_no):
                weight = random()
                genotype += ", %d:%f" % (-input_neuron, weight)
            genotype += "]"
            first_input +=  1
    print genotype
    print "~\n"
            

if __name__ == '__main__':
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print """
        Simple NN generator 
        Given number of neurons in each layer it generates
        feed-forward network in f1 notation, with random weights.
        
        usage:
            nn_generator.py N a b c
        where:
            N - number of genotypes to generate
            a - number of neurons in first layer
            b - number of neurons in second layer
            c - ...
         example:
            nn_generator.py 5 3 4 1
         will generate 5 genotypes, each with neural network of architecture 3-4-3."""
    else:
        N = int(sys.argv[1])
        layers = [int(c) for c in sys.argv[2:]]
        neuron_type = "Nu"
        for i in range(0,N):
            generate(neuron_type, layers)
