import pandas as pd
import numpy as np

salary_dictionary = {"Programming Language": ["Python", "Python", "C#", "C#", "Kotlin", "Swift"], "Name": ["A","B","C","D","E","F"], "Salary": [100, 150, 200, 250, 175, 275]}
salary_dataframe = pd.DataFrame(salary_dictionary)
print(salary_dataframe)

group_object = salary_dataframe.groupby("Programming Language")

print(group_object.count())

print(group_object.min("Salary"))
print(group_object.max("Salary"))
print(group_object.mean("Salary"))
print(group_object.mean(numeric_only=True))

print(group_object.describe())