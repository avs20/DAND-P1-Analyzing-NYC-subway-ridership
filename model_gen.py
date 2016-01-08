# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 14:11:19 2016

@author: ashutoshsingh


The file takes the turnstile data and runs a linear regression model on it. 
It also calculates the R-squared values and plots the graph of it
"""

import pandas as pd
import numpy as np
from ggplot import *
from scipy import stats
import matplotlib.pyplot as plt

import statsmodels.api as sm 
import numpy as np
import statsmodels.api as sm
import pylab






features  = [ 'rain' ,  'hour','weekday']

def linear_reg_using_ols(inputs,target):
    #we need an intercept so adding ones
    inputs = sm.add_constant(inputs)
    model = sm.OLS(target,inputs)
    result = model.fit()
    return result
    
    
def r_square_result(data, predicted_values):
    data_mean = np.mean(data)
    ss_total = np.sum((data-predicted_values)**2)
    ss_reg = np.sum((data-data_mean)**2)
    
    r_squared = 1 - (ss_total/ss_reg)
    
    return r_squared



#main function
if __name__ == '__main__':
    
    #first read the files 
    data = pd.read_csv('turnstile_weather_v2.csv')
    
    #generate a features list
    input_features = data[features]
    target = data['ENTRIESn_hourly']
    
    #for dummy units 
    dummy_vars = pd.get_dummies(data['UNIT'])
    input_features = input_features.join(dummy_vars)
    
    result = linear_reg_using_ols(input_features,target)
    
    #print result.summary()
    model = result.params 
    
    print "Intercept : ", model[0]
    
    non_dummy_params = model[1:5]
    print non_dummy_params
    
    predictions = model[0] + np.dot(input_features.values, model[1:])
    
    #print r_square_result(data['ENTRIESn_hourly'].values, predictions)    
    print "R-Squared Value : ",result.rsquared
    
    #plot the residual curve 
    residual_data  = pd.DataFrame(data['ENTRIESn_hourly'].values - predictions, \
                    columns = ['residual'])
    plot = ggplot(residual_data, aes(x = 'residual')) + \
                 geom_histogram() + \
                 ggtitle('Residuals histogram') + \
                 xlab('Residuals') + \
                 ylab('Count') + \
                 xlim(-15000,15000)
                 

    print plot
    ggsave('./plots/residual_curve.png',plot)
    
    #probability plot of the residuals 
    sm.qqplot(residual_data['residual'].values, line='45')
    pylab.show()
    
    
    
    
    
    

