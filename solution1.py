import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

def ddSim(y,t0,r,K):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]
    
N0 = [10]
K = 100
listr = (-0.1,0.1, 0.4, 0.8, 1.0)
times = range(0,600)
modelOutput=pandas.DataFrame({"time":times,"r1":0, "r2":0, "r3":0, "r4":0, "r5":0})

for i in range(len(listr)):
    params = (listr[i], K)
    modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    modelOutput.iloc[:,i]=modelSim[:,0]
    
ggplot(modelOutput,aes(x="time",y="r1"))+geom_line()+theme_classic()


listK = (10,50,100)
r = 0.2
N0 = [1]
modelOutput=pandas.DataFrame({"time":times,"K1":0, "K2":0, "K3":0})
for i in range(len(listK)):
    params = (r, listK[i])
    modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    modelOutput.iloc[:,i]=modelSim[:,0]
    
ggplot(modelOutput,aes(x="time",y="K1"))+geom_line()+theme_classic()


listN0 = (1, 50, 100)
params = (0.1, 50)
modelOutput=pandas.DataFrame({"time":times,"N1":0, "N2":0, "N3":0})
for i in range(len(listN0)):
    modelSim=spint.odeint(func=ddSim,y0=listN0[i],t=times,args=params)
    modelOutput.iloc[:,i]=modelSim[:,0]
    
ggplot(modelOutput,aes(x="time",y="N1"))+geom_line()+theme_classic()


