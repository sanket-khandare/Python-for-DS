# Import numpy
import numpy as np

# ----------------------------------------------------------------

# - Simulate the data
height = np.round(np.random.normal(1.75, 0.2, 200), 2)
weight = np.round(np.random.normal(60.32,15, 200), 2)
np_city = np.column_stack((height, weight))

print(np_city)
print(np_city.shape)

# ----------------------------------------------------------------

# Print out the mean of height
print('Mean - ' + str(np.mean(height)))

# Print out the median of height
print('Median - ' + str(np.median(height)))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_city[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_city[:,0], np_city[:,1])
print("Correlation: " + str(corr))


# Create numpy array: conversion
conversion = [0.0254,0.453592]

# Print out product of np_baseball and conversion
print(np_city * conversion)

# Plot charts
import matplotlib.pyplot as plt
plt.scatter(height, weight)
plt.show()