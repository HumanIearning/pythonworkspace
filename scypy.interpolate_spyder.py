# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:33:14 2021

@author: user
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
%matplotlib QT5
# QT5

x = np.array([1,2,3,4,5])
y = np.array([1.,0.8,0.4,0.3,0.2])


plt.plot(x,y,"*")

f_lin = interpolate.interp1d(x,y) # x,y 에 맞는 1차함수를 만들어줌
x_new = np.arange(1,5,0.1)
y_lin = f_lin(x_new)


tick = interpolate.splrep(x,y,s=0)
y_spl = interpolate.splev(x_new,tick,der=0)

fig, ax = plt.subplots()
ax.plot(x,y,'o',label='Data')
ax.plot(x_new,y_lin,label='linear')
ax.plot(x_new,y_spl,label='spline')
ax.legend()



    