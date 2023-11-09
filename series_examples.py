import pandas as pd
import numpy as np

numpy_array = np.random.randint(0, 50, 10)
print(numpy_array)

pd_series = pd.Series(numpy_array)
print(pd_series)

quiz_result1 = pd.Series(data=[50, 60, 80], index= ["A", "B", "C"])
quiz_result2 = pd.Series(data=[70, 80, 50], index= ["A", "B", "C"])
print((quiz_result1 * 0.4 + quiz_result2 * 0.6) / 2)