# -*- coding: utf-8 -*-
"""Onion price using Random Forest Regression Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O_KJqL_AZoKuEPNQkb7Ci-nwOm0fca7X
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import seaborn as sns
import matplotlib.cbook as cbook
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso

!gdown --id 1gWE04_0flPuydo7xBoprNa-ScEi8xqnK --output Onion_dataset.csv

onion_data = pd.read_csv("Onion_dataset.csv")

onion_data.head()

onion_data.tail()

onion_data.isnull().sum()

onion_data.shape

onion_data.info()

onion_data.describe()

correlation = onion_data.corr()

plt.figure(figsize = (8,8))
sns.heatmap(correlation,cbar=True, square=True , fmt='.2f',annot =True,annot_kws ={'size': 8},cmap='Blues')

print(correlation['Red Onion Price'])

sns.distplot (onion_data['Red Onion Price'],color ='blue')

X = onion_data.drop(['Date','Red Onion Price'],axis=1)
Y = onion_data['Red Onion Price']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state=5)

print(X_train,X_test)
print(Y_train,Y_test)

"""**Random Forest Regressor** """

regressor = RandomForestRegressor(n_estimators=1000)

regressor.fit(X_train,Y_train)

test_data_prediction = regressor.predict(X_test)

print(test_data_prediction)

error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared error : ", error_score)

mape = np.mean(np.abs((Y_test - test_data_prediction) / Y_test)) * 100
print("Testing MAPE: {}".format(mape))

Y_test = list(Y_test)

plt.figure(figsize=(8,4))
plt.xlim(0, 180)
plt.ylim(0, 600)
plt.plot(Y_test, color='blue', label = 'Actual Value')
plt.plot(test_data_prediction, color='red', label='Predicted Value')
plt.title('Red Onion Price Prediction using Random Forest Regression Model')
plt.xlabel('Time Steps (Days)')
plt.ylabel('Red Onion Price')
plt.legend()
plt.show()

