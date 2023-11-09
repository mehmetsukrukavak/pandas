import pandas as pd
import numpy as np

#series
myDictionary = {"James": 50, "Lars": 60, "Kirk": 55, "Rob": 65}

pandasSeries = pd.Series(myDictionary)
print(pandasSeries)

ageList = [50, 60, 55, 65]
nameList = ["James", "Lars", "Kirk", "Rob"]
print(pd.Series(data=ageList, index=nameList))