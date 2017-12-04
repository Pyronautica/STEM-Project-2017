import random
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def neuralNetworkXOR(inputN,outputN, hiddenLayerCount, numberOfTrials):
    currentTrial = 0
    currentLayer = 0
    neuronAmount = 0
    synapseDictionary = {} # L = LAYER && N = NEURON!
    neuronBaseValue = {}
    neuronNewValue = {}
    calculatedOutput = {}
    while currentTrial == 0:
        while currentLayer == 0:
            nextLayer = currentLayer + 1
            neuronAmount = input("How many neurons on next layer?: ")
            for i in range(neuronAmount):
                neuronBaseValue['L{0}N{1}'.format(nextLayer,i)] = 0
                for j in range(len(inputN)):
                    currentSynapseValue = random.uniform(0.0,1.0)
                    synapseDictionary['L{0}N{1}->L{2}N{3}'.format(currentLayer,j,nextLayer,i)] = currentSynapseValue
                    neuronBaseValue['L{0}N{1}'.format(nextLayer,i)] = neuronBaseValue['L{0}N{1}'.format(nextLayer,i)] + currentSynapseValue * inputN[j]
                    print neuronBaseValue
                neuronNewValue['L{0}N{1}'.format(nextLayer,i)] = sigmoid(neuronBaseValue['L{0}N{1}'.format(nextLayer,i)]) 
                print'Sigmoid attached: {0}'.format(neuronNewValue)
            currentLayer = currentLayer + 1        
        while currentLayer < hiddenLayerCount and currentLayer != 0:
            previousNeuron = neuronAmount
            nextLayer = currentLayer + 1
            neuronAmount = input("How many neurons next on next layer?: ")
            for i in range(neuronAmount):
                neuronBaseValue['L{0}N{1}'.format(nextLayer,i)] = 0
                for j in range(previousNeuron):
                    currentSynapseValue = random.uniform(0.0,1.0)
                    synapseDictionary['L{0}N{1}->L{2}N{3}'.format(currentLayer,j,nextLayer,i)] = currentSynapseValue
                    neuronBaseValue['L{0}N{1}'.format(nextLayer,i)] = neuronBaseValue['L{0}N{1}'.format(nextLayer,i)] + currentSynapseValue * neuronNewValue['L{0}N{1}'.format(currentLayer,j)]
                    print neuronBaseValue
                neuronNewValue['L{0}N{1}'.format(nextLayer,i)] = sigmoid(neuronBaseValue['L{0}N{1}'.format(nextLayer,i)])
                print'Sigmoid attached: {0}'.format(neuronNewValue)
            currentLayer = currentLayer + 1
        while currentLayer == hiddenLayerCount:
            calculatedOutput['Trial{0}'.format(currentTrial)] = 0
            previousNeuron = neuronAmount
            nextLayer = currentLayer + 1
            neuronAmount = len(outputN)
            for i in range(neuronAmount):
                neuronBaseValue['L{0}N{1}'.format(nextLayer,i)] = 0
                for j in range(0,previousNeuron):
                    currentSynapseValue = random.uniform(0.0,1.0)
                    synapseDictionary['L{0}N{1}->L{2}N{3}'.format(currentLayer,j,nextLayer,i)] = currentSynapseValue
                    neuronBaseValue['L{0}N{1}'.format(nextLayer,i)] = neuronBaseValue['L{0}N{1}'.format(nextLayer,i)] + currentSynapseValue *  neuronNewValue['L{0}N{1}'.format(currentLayer,j)]
                neuronNewValue['L{0}N{1}'.format(nextLayer,i)] = sigmoid(neuronBaseValue['L{0}N{1}'.format(nextLayer,i)])
                calculatedOutput['Trial{0}'.format(currentTrial)] = neuronNewValue['L{0}N{1}'.format(nextLayer,i)]
                print neuronBaseValue
                print neuronNewValue
            currentLayer = currentLayer + 1
        currentTrial = currentTrial + 1
    while currentTrial < numberOfTrials:
        print "hi"
        currentTrial = currentTrial + 1
    while currentTrial == numberOfTrials:
        return calculatedOutput 
        currentTrial = currentTrial + 1
    
def backPropagation():
    print neuralNetworkXOR([1,1],[0],1,1)