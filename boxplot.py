import pandas
import numpy as np
from ggplot import *

def floor_decade(date_value):
    #"Takes a date. Returns the decade."
    return (date_value.day // 31) * 10

data = pandas.read_csv('turnstile_weather_v2.csv')

data = data[data['ENTRIESn_hourly'] > 1]
data_rain = data[data['rain'] > 0]
data_no_rain = data[data['rain'] == 0]
data_no_rain = data_no_rain[:9433]

#plot2 =  ggplot(data_no_rain , aes(x= 'ENTRIESn_hourly', color='rain', fill = 'rain')) + \
#geom_histogram(binwidth = 50, alpha=0.6) + scale_x_continuous(limits=(0,10000)) + \
#ggtitle('Subway Ridership on Non-Rainy Days ')+ xlab('Entries Each hour') + ylab('Frequency')

ggplot(data , aes(x= 'hour', y='ENTRIESn')) + geom_boxplot()  + ggtitle('Subway Ridership on Non-Rainy Days ')+ xlab('Entries Each hour') + ylab('Frequency')

