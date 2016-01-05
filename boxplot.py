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
#
#plot2 =  ggplot(data_no_rain , aes(x= 'ENTRIESn_hourly', color='rain', fill = 'rain')) + \
#geom_histogram(binwidth = 50, alpha=0.6) + scale_x_continuous(limits=(0,10000)) + \
#ggtitle('Subway Ridership on Non-Rainy Days ')+ xlab('Entries Each hour') + ylab('Frequency')

#Eggplot(data , aes(x= 'hour', y='ENTRIESn')) + geom_boxplot()  + ggtitle('Subway Ridership on Non-Rainy Days ')+ xlab('Entries Each hour') + ylab('Frequency')

#convert hour field to a categorical variable.

data_no_rain['hour_cat'] = data_no_rain['hour'].astype('category')
data_rain['hour_cat'] = data_rain['hour'].astype('category')
data['hour_cat'] = data['hour'].astype('category')
data['rain'] = data['rain'].astype('category')

#now plot for data_rain and data_no_rain
#print ggplot(data_rain,aes(y = 'hour_cat',x='ENTRIESn_hourly'))+geom_boxplot()


#print ggplot(data_no_rain,aes(y = 'hour_cat',x='ENTRIESn_hourly'))+geom_boxplot()

print ggplot(data,aes(y = 'hour_cat',x='ENTRIESn_hourly',fill='rain'))+ \
    geom_boxplot()


    



