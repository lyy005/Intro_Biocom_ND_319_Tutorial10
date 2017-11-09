import pandas
import numpy
import scipy
import scipy.integrate as spint
from plotnine import *

r_list=[-0.1,0.1,0.4,0.8,1]

def growthRate(y,to,r,K):
    N=y[0]
    dNdt=r* (1-N/K)* N

    return [dNdt]

for i in r_list:
    params=(i,100)
    N0=10
    times=range(0,1000)
    
modelSim=spint.odeint(func=growthRate,y0=N0,t=times,args=params)
modelOutput=pandas.DataFrame({"t":times,"N":modelSim[:,0]})
a=ggplot(modelOutput,aes(x="t",y="N"))+geom_line()+theme_classic()
a.draw()

K_list=[10,50,100]
def carryingCapacity(y,to,r,K):
    N=y[0]
    dNdt=r* (1-N/K)* N

    return [dNdt]
    
for i in K_list:
    params=(0.2,i)
    N0=1
    times=range(0,1000)

modelSim=spint.odeint(func=carryingCapacity,y0=N0,t=times,args=params)
modelOutput=pandas.DataFrame({"t":times,"N":modelSim[:,0]})
b=ggplot(modelOutput,aes(x="t",y="N"))+geom_line()+theme_classic()
b.draw()

N_list=[1,50,100]
def popSize(y,to,r,K):
    N=y[0]
    dNdt=r* (1-N/K)* N

    return [dNdt]

for i in N_list:
    params=(0.1,50)
    N0=i
    times=range(0,1000)

modelSim=spint.odeint(func=popSize,y0=N0,t=times,args=params)
modelOutput=pandas.DataFrame({"t":times,"N":modelSim[:,0]})
c=ggplot(modelOutput,aes(x="t",y="N"))+geom_line()+theme_classic()
c.draw
