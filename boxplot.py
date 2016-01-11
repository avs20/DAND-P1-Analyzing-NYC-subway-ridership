import pandas
import numpy as np
from ggplot import *

def floor_decade(date_value):
    #"Takes a date. Returns the decade."
    return (date_value.day // 31) * 10

data = pandas.read_csv('turnstile_weather_v2.csv')

#data_rain = data[data['rain'] > 0]
#data_no_rain = data[data['rain'] == 0]
#data_no_rain = data_no_rain[:9433]


#convert hour field to a categorical variable.

#data_no_rain['hour_cat'] = data_no_rain['hour'].astype('category')
#data_rain['hour_cat'] = data_rain['hour'].astype('category')
#data['hour_cat'] = data['hour'].astype('category')
#data['rain'] = data['rain'].astype('category')

#now plot for data_rain and data_no_rain




#plot the data of both days as a facet
plot =  ggplot(data,aes(y = 'hour',x='ENTRIESn_hourly'))+ \
    geom_boxplot() + \
    facet_grid('rain') + \
    xlab("Number of Entries")+ \
    ylab("Time of Day") + \
    ggtitle("Subway Ridership by Hour of Day on Rainy and Non-Rainy Days")+ \
    xlim(0,10000)

print plot
    



