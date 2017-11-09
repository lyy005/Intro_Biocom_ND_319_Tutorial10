import pandas
import numpy
import scipy
import scipy.integrate as spint
from plotnine import *

beta=[0.0005,0.005,0.0001,0.00005,0.0001,0.0002,0.0001]
gamma=[0.05,0.5,0.1,0.1,0.05,0.05,0.06]
params_dict = {}
for i in range(len(beta)):
    params_dict[beta[i]] = gamma[i]

def disTrans(y, t, beta, gamma):
    S=y
    I=y
    R=y
    N=1000
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    
    return dSdt
    return dIdt
    return dRdt

for i in params_dict.keys():
    params=(i,params_dict[i])
    S0=999
    I0=1
    R0=0
    times=range(0,500)
    
    modelSim=spint.odeint(func=disTrans,y0=S0,t=times,args=params)
    modelSim2=spint.odeint(func=disTrans,y0=I0,t=times,args=params)
    modelSim3=spint.odeint(func=disTrans,y0=R0,t=times,args=params)
    modelOutput=pandas.DataFrame({"t":times,"S":modelSim[:,0],"I":modelSim2[:,0],"R":modelSim3[:,0]})

print modelOutput

a=ggplot(modelOutput,aes(x="t",y="y0"))+geom_line(aes(x="t",y="S"),color='blue')+geom_line(aes(x="t",y="I"),color='red')+geom_line(aes(x="t",y="R"),color='green')+theme_classic()
a.draw()

for i in I.modelOutput:
    incidence=i-(i-1)

for i in modelOutput:
    prevalence= I(i) / (S(i)+ I(i)+ R(i))

for i in modelOutput:
    percentAffected= (I(i)+ S(i)) / (S(i)+ I(i)+ R(i))
    
for i in modelOutput:
    reproductionNumber= beta[i]* (S(i)+ I(i)+ R(i)) / gamma[i]
    