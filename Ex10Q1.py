import numpy
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *
def ddSim(y,t0,r,K):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]
times=(range(0,1000))    

rs=[-0.1,0.1,0.4,0.8,1]
store_rs=pandas.DataFrame({"time":times,"rl":0,"r2":0,"r3":0,"r4":0,"r5":0})
for i in range(0,len(rs)):
    K=100
    N=10
    pars1=(rs[i],K)
    sim=spint.odeint(func=ddSim,y0=N,t=times,args=pars1)
    store_rs.iloc[:,i]=sim[:,0]
a=ggplot(store_rs,aes(x="time",y="r2"))
a+geom_point()+coord_cartesian()

ks=[10,50,100]
store_ks=pandas.DataFrame({"time":times,"kl":0,"k2":0,"k3":0})
for i in range(0,len(ks)):
    N=1
    pars2=(0.2,ks[i])
    sim2=spint.odeint(func=ddSim,y0=N,t=times,args=pars2)
    store_ks.iloc[:,i]=sim2[:,0]

ns=[1,50,100]
store_ns=pandas.DataFrame({"time":times,"nl":0,"n2":0,"n3":0})
for i in range(0,len(ns)):
    N=1,50,100
    pars3=(0.1,50)
    sim3=spint.odeint(func=ddSim,y0=N[i],t=times,args=pars3)
    store_ns.iloc[:,i]=sim3[:,0]

#Placing models into dataframe    
modelOutputRS=pandas.DataFrame({"t":times,"N":sim[:,0]})
modelOutputKS=pandas.DataFrame({"t":times,"N":sim2[:,0]})
modelOutputNS=pandas.DataFrame({"t":times,"N":sim3[:,0]})

#Plot simulation outputs into ggplot
ggplot(modelOutputKS,aes(x="t",y="N"))+geom_line()+theme_classic()
ggplot(modelOutputRS,aes(x="t",y="N"))+geom_line()+theme_classic()
ggplot(modelOutputNS,aes(x="t",y="N"))+geom_line()+theme_classic()