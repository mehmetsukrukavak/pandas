import pandas as pd
import numpy as np

datas = np.array([[10, 20, 30], [20, 30, 40], [20, 50, 10], [10, 15, 20]])
print(datas)

names = ["James", "Lars", "Kirk", "Rob"]
months = ["Jan", "Feb", "Mar"]

dataFrame = pd.DataFrame(datas, index=names, columns=months)
print(dataFrame)

print(dataFrame["Feb"])

feb_series = dataFrame["Feb"]
print(feb_series.mean())
print(feb_series.max())

print(dataFrame.loc["Lars"])
print(dataFrame.loc["Lars"].mean())
print(dataFrame.iloc[3])

dataFrame["Apr"] = dataFrame["Mar"] * 2
print(dataFrame)
print(dataFrame.drop("Rob", axis=0))
print(dataFrame)
dataFrame.drop("Rob", axis=0,inplace=True)
print(dataFrame)

print(dataFrame[dataFrame > 30])
print(dataFrame[dataFrame["Mar"] > 10])

dataFrame["NewIndex"] = ["L.G", "B.G", "R.G"]
print(dataFrame.set_index("NewIndex"))




