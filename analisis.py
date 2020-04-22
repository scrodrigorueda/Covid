#!bin/usr/env python
import pandas as pd

data = pd.read_csv("time_series_covid19_confirmed_global.csv")
print(data.head())
data.drop(["Province/State","Lat","Long"], axis =1, inplace = True)
print(data.head())
LA = (
(data['Country/Region'] == 'Argentina')|
(data['Country/Region'] == 'Bolivia')|
(data['Country/Region'] == 'Brazil')|
(data['Country/Region'] == 'Chile')|
(data['Country/Region'] == 'Colombia')|
(data['Country/Region'] == 'Paraguay')|
(data['Country/Region'] == 'Peru')|
(data['Country/Region'] == 'Uruguay')
)
data = data[LA]
print(data.tail())
