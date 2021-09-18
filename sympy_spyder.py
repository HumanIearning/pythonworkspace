# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:19:32 2021

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
x = symbols('x')

expr = 2*x

expr.subs(x,2)

# differentiation 미분

f = x**3

from sympy import diff
df1 = diff(f,x)
df2 = diff(df1,x)
df3 = diff(df2,x)


from sympy import sin
f = sin(x)
df1 = diff(f,x)



# integrate 적분
from sympy import integrate
integrate(f,(x,0,2*np.pi))




# limit
from sympy import limit
y = limit(sin(x)/x,x,0) # 식, lim x-> 0
y = np.sin(x)/x                    
x = np.linspace(-10,10,100)
plt.plot(sin(x), x, '-b')     # 왜 안돼 야발


# ODE
from sympy import Function, Eq, dsolve

t = symbols('t')
x = Function('x')
ODE = Eq(x(t).diff(t,t) + x(t))
dsolve(ODE,x(t))





