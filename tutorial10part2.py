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
    
    y0=S0, I0, R0
    modelSim=spint.odeint(func=disTrans,y0=S0 ,t=times,args=params)
    modelOutput=pandas.DataFrame({"t":times,"y":modelSim[:,0]})

print modelOutput
g=ggplot(modelOutput,aes(x="t",y="y"))+geom_line()+theme_classic()
g.draw()