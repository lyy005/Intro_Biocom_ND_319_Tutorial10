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
times=range(0,100)
  
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

r=0.2 #Define a set growth rate and iitial population size
N0=[1]
times=range(0,50)

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
## number 1 part 3

r=0.1 #Define a set growth rate and carrying capacity
K=50
times=range(0,100)

N0s=[1,50,100] #Define a list of initial sizes for each individual population
store_N0s=pandas.DataFrame({"time":times,"N01":0,"N02":0,"N03":0}) #Initialize a data frame to store initial sizes with columns for each
                                                               #initial size, and the times modeled
for i in range(0,len(N0s)): #Set up a for loop that runs through each N0 in the list and models population growth using
    params=(r,K)       #other established parameters
    sim=spint.odeint(func=ddSim,y0=N0s[i],t=times,args=params)
    store_N0s.iloc[:,i]=sim[:,0] #Store population values in the column appropriate for the current carrying capacity

popsize=ggplot(store_N0s,aes(x="time",y="N"))+theme_classic()#Set up base plot for population curves
popsize=popsize+geom_line(store_N0s,aes(y="N01"))
popsize=popsize+geom_line(store_N0s,aes(y="N02"))
popsize=popsize+geom_line(store_N0s,aes(y="N03"))

popsize #Display graph

# Question 2

#########################################################

import scipy
import scipy.integrate as spint
import numpy
import matplotlib.pyplot as plt

def SIR_model(y, t, beta, gamma):
    S = y[0]
    I = y[1]
    R = y[2]
    
    dSdt=(-beta*I*S)
    dIdt=(beta*I*S-(gamma*I))
    dRdt=(gamma*I)
    
    return (dSdt, dIdt, dRdt)

N = [999, 1, 0]
S0=999
I0=1
R0=0
beta=numpy.array([.0005, .005, .0001, .00005, .0001, .0002, .0001])
gamma=numpy.array([.05, .5, .1, .1, .05, .05, .06])

store_S=pandas.DataFrame({"time":times,"beta1":0,"beta2":0,"beta3":0,"beta4":0,"beta5":0,"beta6":0,"beta7":0})
store_I=pandas.DataFrame({"time":times,"beta1":0,"beta2":0,"beta3":0,"beta4":0,"beta5":0,"beta6":0,"beta7":0})
store_R=pandas.DataFrame({"time":times,"beta1":0,"beta2":0,"beta3":0,"beta4":0,"beta5":0,"beta6":0,"beta7":0})

t=numpy.linspace(0,100)

for i in range(0,len(beta)):
    params=(beta[i],gamma[i])
    sim=spint.odeint(func=SIR_model,y0=N,t=times,args=params)
    store_S.iloc[:,i]=sim[:,0]
    store_I.iloc[:,i]=sim[:,1]
    store_R.iloc[:,i]=sim[:,2]


plt.figure(figsize=[6,4])
plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="R(t)")
plt.show()

#max daily incidence
mdi=np.diff(store_I.iloc[:,1])
Imax=numpy.max(mdi)
print("max daily incidence")
print(Imax)

#max daily prevelance
mdp=Imax/1000
print("max daily prevalence")
print(mdp)

#percent affected over simulation
smallS=numpy.min(store_S.iloc[:,0])
pas=(1/smallS)
print("percent affected over simulation")
print(pas)

#basic reproduction number
S0=999
I0=1
R0=0
beta=numpy.array([.0005, .005, .0001, .00005, .0001, .0002, .0001])
gamma=numpy.array([.05, .5, .1, .1, .05, .05, .06])
basicReproductionNumber=(((beta*(S0+I0+R0))/gamma))
print("BasicReproductionNumber")
print(basicReproductionNumber)
