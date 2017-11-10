import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

def ddSim (y,t0,r,K): #Define basic model for density-dependent growth
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]
    
K=100 #Define a set carrying capacity & initial population size
N0=[10]
times=range(0,500)
  
rs=[-0.1,0.1,0.4,0.8,1.0] #Define a list of growth rates for each individual population
store_rs=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0}) #Initialize a data frame to store population size, with
                                                                             #columns labeled for times, and each growth rate
for i in range(0,len(rs)): #Set up a for loop that runs through each growth rate in the list, and models population growth using
    params=(rs[i],K)       #established parameters
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    store_rs.iloc[:,i]=sim[:,0] #Store population values in the column appropriate for the current growth rate being modeled

rates=ggplot(store_rs,aes(x="time",y="N"))+theme_classic() #Set up a base plot for the population curves
rates=rates+geom_line(store_rs,aes(y="r1")) #Add each population curve to the graph
rates=rates+geom_line(store_rs,aes(y="r2"))
rates=rates+geom_line(store_rs,aes(y="r3"))
rates=rates+geom_line(store_rs,aes(y="r4"))
rates=rates+geom_line(store_rs,aes(y="r5"))

rates #Display the graph

r=0.2 #Define a set growth rate and initial population size
N0=[1]

Ks=[10,50,100] #Define a list of carrying capacities for each individual population
store_Ks=pandas.DataFrame({"time":times,"K1":0,"K2":0,"K3":0}) #Initialize a data frame to store population size with columns for each
                                                               #carrying capacity, and the times modeled
for i in range(0,len(Ks)): #Set up a for loop that runs through each carrying capacity in the list and models population growth using
    params=(r,Ks[i])       #other established parameters
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    store_Ks.iloc[:,i]=sim[:,0] #Store population values in the column appropriate for the current carrying capacity

capacity=ggplot(store_Ks,aes(x="time",y="N"))+theme_classic()#Set up base plot for population curves
capacity=capacity+geom_line(store_Ks,aes(y="K1"))
capacity=capacity+geom_line(store_Ks,aes(y="K2"))
capacity=capacity+geom_line(store_Ks,aes(y="K3"))

capacity #Display graph

r=0.1 #Define a set growth rate and carrying capacity
K=50
times=range(0,500)

N0s=[1,50,100] #Define a list of initial sizes for each individual population
store_N0s=pandas.DataFrame({"time":times,"N01":1,"N02":50,"N03":1500}) #Initialize a data frame to store initial sizes with columns for each
                                                               #initial size, and the times modeled

for i in range(0,len(N0s)): #Set up a for loop that runs through each N0 in the list and models population growth using
    params=(r,K)#other established parameters
    N0=N0s[i] #Assign N0 a single value from the array of initial population sizes
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    store_N0s.iloc[:,i]=sim[:,0] #Store population values in the column appropriate for the current carrying capacity

initpop=ggplot(store_N0s,aes(x="time",y="N"))+theme_classic()#Set up base plot for population curves
initpop=initpop+geom_line(store_N0s,aes(y="N01"))
initpop=initpop+geom_line(store_N0s,aes(y="N02"))
initpop=initpop+geom_line(store_N0s,aes(y="N03"))

initpop #Display graph


