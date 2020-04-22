#!bin/usr/env python
import pandas as pd

data = pd.read_csv("time_series_covid19_confirmed_global.csv")
print(data.head())
data.drop(["Province/State","Lat","Long"], axis =1, inplace = True)
print(data.head())
nuevo = (data.Country/Region == 'Bolivia')
print(nuevo.head())
