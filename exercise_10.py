## exercise 10 ##

# 1
#Load packages
import pandas
import scipy
import scipy.integrate as si
from plotnine import *


#Define custom function
def popGrowth(y,t0,r,K,N):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]
times=range(0,100)
NO=[.01]
#Set a pool of values for growth rate
growthRates=[-.1,.1,.4,.8,1.0]
#Dataframe for storing model output
store_growthRates=pandas.DataFrame({"time":times,"r1":0,"r2":0,"r3":0,"r4":0,"r5":0})

#Using a for loop to make my life easier
for i in range(0,len(growthRates)):
    pars=(growthRates[i],100,10)
    sim=si.odeint(func=popGrowth,y0=NO,t=times,args=pars)
    store_growthRates.iloc[:,i]=sim[:,0]
print(store_growthRates)    
    
#Plot 1- pop size as function of time
g=(ggplot(data=store_growthRates)
    +geom_line(store_growthRates,aes(x="time",y="r1"))+theme_classic()
    +ylab("population size")
    +geom_line(store_growthRates,aes(x="time",y="r2"),color="green")
    +geom_line(store_growthRates,aes(x="time",y="r3"),color="red")
    +geom_line(store_growthRates,aes(x="time",y="r4"),color="orange")
    +geom_line(store_growthRates,aes(x="time",y="r5"),color="purple"))
print(g)

#set a pool of values for carrying capacity
carryCap=[10,50,100]
#Dataframe for storing model output
store_carryCap=pandas.DataFrame({"time":times,"K1":0,"K2":0,"K3":0})
#for loop for Plot 2
for i in range(0,len(carryCap)):
    pars=(.2,carryCap[i],1)
    sim=si.odeint(func=popGrowth,y0=NO,t=times,args=pars)
    store_carryCap.iloc[:,i]=sim[:,0]
print(store_carryCap) 

#Plot 2- 
k=(ggplot(data=store_carryCap)
    +geom_line(store_carryCap,aes(x="time",y="K1"),color="blue")+theme_classic()
    +ylab("population size")
    +geom_line(store_carryCap,aes(x="time",y="K2"),color="green")
    +geom_line(store_carryCap,aes(x="time",y="K3"),color="purple"))
print(k)

#Set a pool of values for init pop size
initPop=[1,50,100]
#Dataframe for storing model output
store_initPop=pandas.DataFrame({"time":times,"N1":0,"N2":0,"N3":0})

#Using a for loop to make my life easier
for i in range(0,len(initPop)):
    pars=(.1,50,initPop[i])
    sim=si.odeint(func=popGrowth,y0=NO,t=times,args=pars)
    store_initPop.iloc[:,i]=sim[:,0]
print(store_initPop)    
    
#Plot 3- effect of initial Pop size differences
p=(ggplot(data=store_initPop)
    +geom_line(store_initPop,aes(x="time",y="N1"),color="orange")+theme_classic()
    +ylab("population size")
    +geom_line(store_initPop,aes(x="time",y="N2"),color="yellow")
    +geom_line(store_initPop,aes(x="time",y="N3"),color="red"))
print(p)


# 2

def SIR (y,t0,beta,gamma):
    S = y[0]
    I = y[1]
    R = y[2]

    dS = -1*(beta*I*S)
    dI = (beta*I*S)-(gamma*I)
    dR = (gamma*I)

    return dS, dI, dR

times = range(0,500)
params = (.0005, .05)
NO = [999, 1, 0]

infection = pandas.DataFrame({"time":times,"S":0,"I":0,"R":0})
print (infection)

sim = si.odeint(func=SIR, y0=NO, t=times, args=params)

# got the sim working for one beta and gamma value
#need to import the vlaues from the sim list into a dataframe
#need to make a loop that does this for all the beta and gamma values
#need to add calcs to the loop as well.