# -----------------------------------------------------------
# uses Open Meteo API to generate a 5 day temperature forecast
# for a specific place: Johannesburg, South Africa
# 
# (C) 2026 Frank Hofmann, Freiburg/Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import required modules
import pandas as pd
import requests
import matplotlib.pyplot as plt

# define the location by a pair of latitude, and longitude
location = {
    'latitude': -34.0448962, 
    'longitude': 18.36028355
}

# define the timezone
timezone = 'Africa/Johannesburg'

# daily forecast variations: minimal, and maximal temperature per day
dailyFcVar = ['temperature_2m_min', 'temperature_2m_max']

# forecast duration
duration = 5

# define request parameters
parameters = {
    'latitude': location["latitude"],
    'longitude': location["longitude"],
    'daily': dailyFcVar,
    'forecast_days': duration,
    'timezone': timezone
}

# define the url to retrieve the data
url = 'https://api.open-meteo.com/v1/forecast'

# connect, and collect the responses
responses = requests.get(url, params=parameters)

# convert response into JSON structure
data = responses.json()

# extract daily data
dailyFc = data.get('daily')

# transform the data into a Pandas Dataframe
dailyFcDf = pd.DataFrame(dailyFc)

# rename the column titles
dailyFcDf.rename(columns={
    'time':'date', 
    'temperature_2m_min':'minimal temperature', 
    'temperature_2m_max':'maximal temperature'
    }, inplace=True
)

# output collected data as table
print(dailyFcDf)

# generate plot
dailyFcDf.plot(kind="bar", stacked=True)

# set label for x, and y axis
plt.xlabel("Date")
plt.ylabel("Temperature in °C")

# show diagram
plt.show()
