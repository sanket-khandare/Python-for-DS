# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# Print np_baseball
print(np_baseball)

# ----------------------------------------------------------------

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]

# Print np_baseball
print(np_weight)

# ----------------------------------------------------------------

# Create numpy array: conversion
conversion = [0.0254,0.453592]

# Print out product of np_baseball and conversion
print(np_baseball * conversion)

corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))