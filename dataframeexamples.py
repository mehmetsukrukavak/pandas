import pandas as pd
import numpy as np

dictionary = {"James": [40, 30, np.nan], "Kirk": [20, np.nan, 50], "Lars": [30, 50, 40]}
dataFrame = pd.DataFrame(dictionary)
print(dataFrame)

print(dataFrame.dropna())

print(dataFrame.dropna(axis=1))

dictionary = {"James": [40, 30, np.nan], "Kirk": [20, np.nan, 50], "Lars": [30, 50, 40], "Rob": [45, np.nan, np.nan]}

dataFrame = pd.DataFrame(dictionary)
print(dataFrame)

print(dataFrame.dropna(axis=1,thresh=2))

print(dataFrame.fillna(0))




