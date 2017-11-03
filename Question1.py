import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

def ddSim (y,t0,r,K):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]
    
K=100
N0=[10]
times=range(0,500)
  
rs=[-0.1,0.1,0.4,0.8,1.0]
store_rs=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0})

for i in range(0,len(rs)):
    params=(rs[i],K)
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    store_rs.iloc[:,i]=sim[:,0]

rates=ggplot(store_rs,aes(x="time",y="N"))
rates=rates+geom_line(store_rs,aes(y="r1"))
rates=rates+geom_line(store_rs,aes(y="r2"))
rates=rates+geom_line(store_rs,aes(y="r3"))
rates=rates+geom_line(store_rs,aes(y="r4"))
rates=rates+geom_line(store_rs,aes(y="r5"))

rates