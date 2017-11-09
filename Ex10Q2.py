import numpy
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *
#SIR model in epidemiology
#N=S+I+R (susceptible-->B-->infected-->g-->resistant); unidirectional
#R0=((B*(S+I+R))/g) ; R0 is how bad the disease is in the population; see YY's notes for where max daily incidence, max daily prevalence, percent affected, and basic reproduction number are found in a graph

#state vairables=I/S=state parameters=r/B
#basic reproduction only initial values

#equations are dS/dt=-BIS, dI/dt=BIS-RI and dR/dt=RI
def epiSim(y,t,B,r):
    I=y[0]
    S=y[1]
    
    dSdt= (-B*I*S)
    dIdt= (B*I*S)-(r*I)
    dRdt= (r*I)
    
    return[dSdt,dIdt,dRdt]

#generate a dataframe containing a list of the B and r parameters
parB=[0.0005,0.005,0.0001,0.00005,0.0001,0.0002,0.0001]
parr=[0.05,0.5,0.1,0.1,0.05,0.05,0.06]
par_array=numpy.column_stack([parB,parr])
par_df=pandas.DataFrame(par_array,columns=['B','r'])

#extract params from dataframe
for i in range(0,6):
    I0=[1]
    S0=[999,1,0]
    params=(par_df.B[i],par_df.r[i])
    times=range(0,500)
    #create a model using odeint
    modelSim=spint.odeint(func=epiSim,y0=S0,t=times,args=params)
#maxDailyIncidence is the maxInfectivityRate
#maxDailyPrevalence is the half-max of the equation
maxDailyIncidence=
maxDailyPrevalence=