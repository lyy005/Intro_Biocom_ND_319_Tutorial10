## exercise 10 ##

# 1
#Load packages
import pandas
import scipy
import scipy.integrate as si
from plotnine import *


#Define custom function
def popGrowth(y,t0,r,K,N):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]
times=range(0,100)
NO=[.01]
#Set a pool of values for growth rate
growthRates=[-.1,.1,.4,.8,1.0]
#Dataframe for storing model output
store_growthRates=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0})

#Using a for loop to make my life easier
for i in range(0,len(growthRates)):
    pars=(growthRates[i],100,10)
    sim=si.odeint(func=popGrowth,y0=NO,t=times,args=pars)
    store_growthRates.iloc[:,i]=sim[:,0]













# 2