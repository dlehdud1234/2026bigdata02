import pandas as pd
import numpy as np

df1 = pd.read_csv("./bike_rentals.csv")

print(df1.loc[df1['season']!=2])
#print(df1.iloc[3:8,3:7])
#print(df1.loc[3:7,'workingday':'atemp'])

