#Load packages
import pandas
import scipy
import scipy.integrate as si
from plotnine import *

def SIR (y,t0,beta,gamma):
    S = y[0]
    I = y[1]
    R = y[2]
    dS = -1*(beta*I*S)
    dI = (beta*I*S)-(gamma*I)
    dR = (gamma*I)
    return dS, dI, dR

times = range(0,500)
params = (.0005, .05) #need to change these for diff betas and gammas # need to make an arraay or dataframe

data = [{'beta' : .0005, 'gamma' : .05},
        {'beta': .005, 'gamma': .5},
        {'beta': .0001, 'gamma': .1},
        {'beta': .00005, 'gamma': .1},
        {'beta': .0001, 'gamma': .05},
        {'beta': .0002, 'gamma': .05},
        {'beta': .0001, 'gamma': .06}]
my_data = pandas.DataFrame(data)

NO = [999, 1, 0]

infection = pandas.DataFrame({"time":times,"S":0,"I":0,"R":0})
results = []

# sim
sim = si.odeint(func=SIR, y0=NO, t=times, args=params)
# fill dataframe
infection.iloc[:,2]=sim[:,0]
infection.iloc[:,0]=sim[:,1]
infection.iloc[:,1]=sim[:,2]

# calc max daily incidence
daily_incidence = []
for i in range(0,len(infection),):
    if infection.time[i]==0:
        continue
    else:
        I = infection.iloc[i]['I']
        Iold = infection.iloc[i-1]['I']
        incidence = I-Iold
        daily_incidence.append(incidence)
max_daily_incidence = max(daily_incidence)


# calc max daily prevalence
daily_prev = []
for i in range(0,len(infection),):
    I = infection.iloc[i]['I']
    R = infection.iloc[i]['R']
    S = infection.iloc[i]['S']
    prev = I/(S+I+R)
    daily_prev.append(prev)
max_daily_prev = max(daily_prev)

#calc percent affected over simulation- use last time step (499)
I= infection.iloc[499]['I']
R= infection.iloc[499]['R']
S= infection.iloc[499]['S']
percent_affected = (I+R)/(S+I+R)

# basic reproduction number initial SIR
beta = params[0]
gamma = params[1]
I= infection.iloc[0]['I']
R= infection.iloc[0]['R']
S= infection.iloc[0]['S']
Ro = (beta*(S+I+R))/gamma


#need these to fill into a list or a dataframe
# need to put all this intoa bigger loop





