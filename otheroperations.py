import pandas as pd
import numpy as np

my_dict1 = {
    "Name": ["A", "B", "C", "D", "E"],
    "Sports": ["Football", "Basketball", "Tennis", "Running", "Volleyball"],
    "Calories": [100, 200, 300, 400, 500]
}

my_frame1 = pd.DataFrame(my_dict1)
#print(my_frame1)

my_dict2 = {
    "Name": ["F", "G", "H", "I", "J"],
    "Sports": ["Football", "Basketball", "Tennis", "Running", "Volleyball"],
    "Calories": [500, 350, 200, 100, 250]
}

my_frame2 = pd.DataFrame(my_dict2)
#print(my_frame2)

my_dict3 = {
    "Name": ["K", "L", "M", "N", "O"],
    "Sports": ["Football", "Basketball", "Tennis", "Running", "Volleyball"],
    "Calories": [350, 150, 400, 600, 950]
}

my_frame3 = pd.DataFrame(my_dict3)
#print(my_frame3)

#print(pd.concat([my_frame1,my_frame2,my_frame3]))

print(pd.merge(my_frame1, my_frame2, on="Sports"))

