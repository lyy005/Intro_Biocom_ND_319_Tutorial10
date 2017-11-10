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
    
g1=ggplot(modelOutput,aes(x="time",y="r1"))+geom_line()+geom_line(aes(y="R2"))+geom_line(aes(y="R3"))+geom_line(aes(y="R4"))+geom_line(aes(y="R5"))
g1+theme_classic()


listK = (10,50,100)
r = 0.2
N0 = [1]
modelOutput=pandas.DataFrame({"time":times,"K1":0, "K2":0, "K3":0})
for i in range(len(listK)):
    params = (r, listK[i])
    modelSim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    modelOutput.iloc[:,i]=modelSim[:,0]
    
g2=ggplot(modelOutput,aes(x="time",y="K1"))+geom_line()+geom_line(aes(y="K2"))+geom_line(aes(y="K3"))
g2+theme_classic()

listN0 = (1, 50, 100)
params = (0.1, 50)
modelOutput=pandas.DataFrame({"time":times,"N1":0, "N2":0, "N3":0})
for i in range(len(listN0)):
    modelSim=spint.odeint(func=ddSim,y0=listN0[i],t=times,args=params)
    modelOutput.iloc[:,i]=modelSim[:,0]
    
g3=ggplot(modelOutput,aes(x="time",y="N1"))+geom_line()+geom_line(aes(y="N2"))+geom_line(aes(y="N3"))
g3+theme_classic()

#We dont know how to get all the plots outputted, but the code is there to make them all. We asked stuart but he didn't help us with this specifically
