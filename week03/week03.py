import pandas as pd
import numpy as np

df1 = pd.read_csv("./bike_rentals.csv")

df1.rename({'registered' : 'registered_user', 'casual' : 'registered_user'}, axis=1, inplace=True)
#print(df1.head())
#print(df1.describe(include='str'))
#print(df1.describe(include='float'))
print(df1.describe(include='int'))