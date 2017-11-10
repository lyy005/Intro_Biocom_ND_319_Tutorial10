import pandas
import numpy
import scipy
import scipy.integrate as spint
from plotnine import *
r1=[-0.1,0.1,0.4,0.8,1]
def mgrate(y,to,r1,K):
    N=y[0]  
    dNdt=r1* (1-N/K)* N
    return [dNdt]
for i in r1:
    param1=(i,100)
    N0=10
    times=range(0,1000)
ms1=spint.odeint(func=mgrate,y0=N0,t=times,args=param1)
modelOutput=pandas.DataFrame({"t":times,"N":ms1[:,0]})
mgraph=ggplot(modelOutput,aes(x="t",y="N"))+geom_line()+theme_classic()

K2=[10,50,100]
def carcap(y,to,r,K2):
    N=y[0]
    dNdt=r* (1-N/K2)* N
    return [dNdt]
for i in K2:
    param2=(0.2,i)
    N0=1
    times=range(0,1000)
ms2=spint.odeint(func=carcap,y0=N0,t=times,args=param2)
modelOutput=pandas.DataFrame({"t":times,"N":ms2[:,0]})
cargraph=ggplot(modelOutput,aes(x="t",y="N"))+geom_line()+theme_classic()

N3=[1,50,100]
def PS(y,to,r,K):
    N3=y[0]
    dNdt=r* (1-N3/K)* N3
    return [dNdt]
for i in N3:
    param3=(0.1,50)
    N0=i
    times=range(0,1000)
ms3=spint.odeint(func=PS,y0=N0,t=times,args=param3)
modelOutput=pandas.DataFrame({"t":times,"N":ms3[:,0]})
psgraph=ggplot(modelOutput,aes(x="t",y="N"))+geom_line()+theme_classic()

mgraph.draw()
cargraph.draw()
psgraph.draw()
