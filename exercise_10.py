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
times=range(0,600)

#Set a pool of values for growth rate
rK=[-.1,.1,.4,.8,1.0]
#Dataframe for storing model output
store_rK=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0})

#Using a for loop to make my life easier
for i in range(0,len(gRates)):
    params=(rK[i],K)
    popGrowthSim=spint.odeint(func=ddSim,y0=y0,t=times,args=params)
    store_rK.iloc[:i]=popGrowthSim[:0]













# 2