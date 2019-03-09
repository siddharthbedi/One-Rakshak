

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:23:36 2018

@author: siddharth
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py






#importing thwe dataset
dataset = pd.read_csv("dataset_new.csv")
dataset.head()
X= dataset.iloc[:,4:6].values
Y=dataset.iloc[:,6:7].values

lat= dataset.iloc[:,4:5].values
long = dataset.iloc[:,5:6].values


'''X1= dataset.iloc[:,4:5].values
X2= dataset.iloc[:,5:6].values'''




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py






#importing thwe dataset
dataset = pd.read_csv("yo.csv")
dataset.head()
X= dataset.iloc[:,4:6].values
Y=dataset.iloc[:,6:7].values

lat= dataset.iloc[:,4:5].values
long = dataset.iloc[:,5:6].values
countb=0
countr=0
countg=0
arrG=[]
#plottiing of graph

for num in range(0,15495):
    if Y[num] >= 18:
        k='red'
        countr=countr+1
                
        
    elif Y[num] >= 9 and Y[num] < 18:
        k='blue'
        countb=countb+1
        
    elif Y[num] < 9:
        k='green'
        countg=countg+1
        arrG.append(num)
       
    plt.scatter(lat[num],long[num],s=5,Color=k)  
X1_green = []
for num1 in arrG:
    X1_green.append(lat[num1]) 
X2_green = []
for num2 in arrG:
    X2_green.append(long[num2]) 

      
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X1_green, X2_green)
#plt.scatter(X1_green, X2_green, color = 'red')
#plt.scatter(X1_green, regressor.predict(X1_green),s=1,color = 'orange')

print(countr)
print(countb)
print(countg)

