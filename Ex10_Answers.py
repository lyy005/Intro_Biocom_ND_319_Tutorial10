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

r=0.2 #Define a set growth rate and iitial population size
N0=[1]
times=range(0,500)

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
K=[50]
times=range(0,500)

N0s=[1,50,100] #Define a list of initial sizes for each individual population
store_N0s=pandas.DataFrame({"time":times,"N01":1,"N02":50,"N03":1500}) #Initialize a data frame to store initial sizes with columns for each
                                                               #initial size, and the times modeled
for i in range(0,len(N0s)): #Set up a for loop that runs through each N0 in the list and models population growth using
    params=(r,K)       #other established parameters
    sim=spint.odeint(func=ddSim,y0=N0,t=times,args=params)
    store_N0s.iloc[:,i]=sim[:,0] #Store population values in the column appropriate for the current carrying capacity

capacity=ggplot(store_N0s,aes(x="time",y="N"))+theme_classic()#Set up base plot for population curves
capacity=capacity+geom_line(store_N0s,aes(y="N01"))
capacity=capacity+geom_line(store_N0s,aes(y="N02"))
capacity=capacity+geom_line(store_N0s,aes(y="N03"))

capacity #Display graph

# Question 2


import pandas
import scipy
import scipy.integrate as spint
from plotnine import *
import numpy as np
from scipy.integrate import odeint


N=1000
S=999
I=1
R=0
T=range(0,500)

B=[.0005]
gamma=[.05]

params= (N, B, gamma)

def ddSim(y, t, N, B, gamma):
    y = S, I, R
    dSdt=(-B*I*S)
    dIdt=(B*I*S-(gamma*I))
    dRdt=(gamma*I)
    return (dSdt, dIdt, dRdt)

y0= S, I, R
ret=odeint(func=ddSim,y0=N,t=T,args=params)
S, I, R =ret.T

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axis_bgcolor='#dddddd', axisbelow=True)
ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()



incidence=(It0-It1)
prevalence=(I/(S+I+R))
percentAffected=((I+R)/(S+I+R))
basicReproductionNumber=(((B(S+I+R))/gamma))



#########################################################
import scipy
import scipy.integrate as spint
import numpy
import matplotlib.pyplot as plt

def SIR_model(y, t, beta, gamma):
    S, I, R = y
    
    dSdt=(-beta*I*S)
    dIdt=(beta*I*S-(gamma*I))
    dRdt=(gamma*I)
    
    return (dSdt, dIdt, dRdt)

N=1000
S0=999
I0=1
R0=0
beta=[.0005]
gamma0=[.05]
t=numpy.linspace(0,500)

solution=scipy.integrate.odeint(SIR_model, [S0, I0, R0], t, args=(beta, gamma))
solution= numpy.array(solution)

plt.figure(figsize=[6,4])
plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="R(t)")
plt.show()





