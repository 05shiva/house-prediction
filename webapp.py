# -*- coding: utf-8 -*-
"""webapp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZVmPgNP782dVqNhXP2ADy5Ki5dJKDCrQ
"""

from google.colab import drive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
drive.mount('/content/gdrive')
df=pd.read_excel('/content/gdrive/MyDrive/test flies/test_data2.xlsx')

x=df.drop(['property_value'],axis=1).values
y=df['property_value'].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.33, random_state=0)

from sklearn import linear_model
regressionobject=linear_model.LinearRegression()
regressionobject.fit(x_train,y_train)

!pip install anvil-uplink

import anvil.server
anvil.server.connect("WDYT3MGMY72MUVUPP7EVS2PE-NCUWEQZGUHUCYTKI")

@anvil.server.callable
def predicting_function(hs,ls,nofr,nofb,llr,ps,ha,fg,sp,dts,wf,waf,dfs,ce,rs):
  return "The predicted value=" , regressionobject.predict([[hs,ls,nofr,nofb,llr,ps,ha,fg,sp,dts,wf,waf,dfs,ce,rs]])

anvil.server.wait_forever()