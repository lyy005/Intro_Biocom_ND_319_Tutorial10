## exercise 10 ##

# 1
#Load packages
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *


#Define custom function
def popGrowth(y,t0,r,K):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]
params=(0.3,10)
NO=[0.01]
times=range(0,600)
modelSim=spint.odeint(func=ddSim,y0=NO,t=times,args=params)
modelOutput=pandas.DataFrame({"t":times,"N":modelSim[:,0]})












# 2