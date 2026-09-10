import pandas as pd
import numpy as np

df1 = pd.read_csv("./bike_rentals.csv")

#print(df1.loc[df1['season']!=2])
#print(df1.iloc[3:8,3:7])
#print(df1.loc[3:7,'workingday':'atemp'])
#print(df1.loc[df1['season'] ==2,'humidity':'registered'])
#print(df1['weather'].value_counts())
#print(df1.loc[(df1['season'] !=2)&(df1['weather'] !=1)])
#temp = (df1.loc[(df1['season'] !=2)&(df1['weather'] !=1)])
#print(temp['weather']==1)
#print(df1.loc[3,'humidity'])

#print(df1.info())
#print(df1.select_dtypes(include='float'))
#print(df1.select_dtypes(exclude='float'))
#print(df1.filter(regex="d..y"))#정규표현식
#print(df1.filter(items=['windspeed','season']))
df2 = df1.set_index('datetime')
#print(df2)
print(df2.filter(like='00:00:00', axis=0))
