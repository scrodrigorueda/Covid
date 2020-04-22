#!bin/usr/env python
#importamos la libreria pandas para trabajar con csv
import pandas as pd
import numpy as np
#Realizamos la lectura de el CSV de cantidad de casos de covid
df = pd.read_csv("time_series_covid19_confirmed_global.csv")

#Nos permite visualizar que los datos fueron creados de forma eficiente
#print(df.head())

#Quitamos los datos que no nos son necesarios de las columnas
df.drop(["Province/State","Lat","Long"], axis =1, inplace = True)
#Comprobamos si se realizo con exito
#print(df.head())

LA = (
(df['Country/Region'] == 'Argentina')|
(df['Country/Region'] == 'Bolivia')|
(df['Country/Region'] == 'Brazil')|
(df['Country/Region'] == 'Chile')|
(df['Country/Region'] == 'Colombia')|
(df['Country/Region'] == 'Paraguay')|
(df['Country/Region'] == 'Peru')|
(df['Country/Region'] == 'Uruguay')
)
#Convertimos la tabla para que contenga paises latinoamericanos
df = df[LA]

print(df)
