#!bin/usr/python
# Shelby Luttrell

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy

#euclidean
def euclideanDist(instance1, instance2):
    square = 0
    if instance1 == None or instance2 == None:
        return float("inf")
    for i in range(1, len(instance1)):
        sub = instance1[i]-instance2[i]
        square += sub**2
    euclidean = math.sqrt(square)
    return euclidean

#manhattan
def manhattanDist(instance1, instance2):
    manhattan = 0
    if instance1 == None or instance2 == None:
        return float("inf")
    for i in range(1, len(instance1)):
        sub = instance1[i]-instance2[i]
        manhattan += abs(sub)
    return manhattan

def readCSV(path):
    data = []
    with open(path, mode='r') as file:
        for line in file:
            line = line.rstrip().split(',')
            data.append(float(line[0])), float((line[1]))
    return data
            

def kmeans(k, ):
#assign each data pt to to the nearest center and obtain new clusters
#calculate the distance
#newListy = copy.deepcopy(listy)




#read in the file
dataPts = readCSV('q1.csv')

#q1
#define the centroids
centroids[(4,6),(5,4)]
method = 'm'

#q2
centroids[(4,6),(5,4)]
method = 'e'

#q3
centroids[(3, 3),(8, 3)]
