# Question 1 #

# Loading Packages
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

# Simulating Equation
def ddSim(y, t0, r, K):
    N=y[0]
    dNdt=r*(1-N/K)*N
    return [dNdt]

# Setting up parameters for each r condition
rlist = [-0.1,0.1,0.4,0.8,1]
# N0 and time range
N0 = 10
K = 100
times = range(0,50)
# creating a dataframe to store model outputs with a column for each r value
store_rs=pandas.DataFrame({"time":times, "r1":0, "r2":0, "r3":0, "r4":0, "r5":0})

# setting up the model
for i in range(0,len(rlist)):
    pars=(rlist[i],K)
    sim = spint.odeint(func=ddSim, y0=N0, t=times, args=pars)
    store_rs.iloc[:,i]=sim[:,0]

cols = ["black", "red", "blue", "green", "orange"]
#Simulating plot
p = ggplot(store_rs, aes(x='time', y='r1')) + geom_line()  #r1
p = p + geom_line(aes(x='time', y='r2'), colour = "red") #r2
p = p + geom_line(aes(x='time', y='r3'), colour = "blue") #r3
p = p + geom_line(aes(x='time', y='r4'), colour = "green") #r4
p = p + geom_line(aes(x='time', y='r5'), colour = "orange") #r5
print p 

# Varying Ks
Klist = [10,50,100]
r = 0.2
N0 =1
store_Ks=pandas.DataFrame({"time":times, "K1":0, "K2":0, "K3":0})

for i in range(0,len(Klist)):
    pars=(r,Klist[i])
    sim = spint.odeint(func=ddSim, y0=N0, t=times, args=pars)
    store_Ks.iloc[:,i]=sim[:,0]

p2 = ggplot(store_Ks, aes(x='time', y='K3')) + geom_line()
p2 = p2 + geom_line(aes(x='time',y='K2'), colour = "blue")
p2 = p2 + geom_line(aes(x='time', y='K1'), colour = "red")
print p2

#Varying Ns
Nlist=[1,50,100]
r=0.1
K=50
store_Ns=pandas.DataFrame({"time":times, "N0_1":0, "N0_2":0, "N0_3":0})

for i in range(0,len(Nlist)):
    pars=(r,K)
    sim = spint.odeint(func=ddSim, y0=Nlist[i], t=times, args=pars)
    store_Ns.iloc[:,i]=sim[:,0]

p3 = ggplot(store_Ns, aes(x='time',y='N0_3')) + geom_line()
p3 = p3 + geom_line(aes(x='time',y='N0_2'), colour = "green")
p3 = p3 + geom_line(aes(x='time',y='N0_1'), colour = 'yellow')
print p3

# Question 2 #

# Multifaceted equation
def SIR(y,t0,beta,gamma):
    S = y[0]
    I = y[1]
    R = y[2]
    
    dSdt = -beta*I*S
    dIdt = beta*I*S - gamma*I
    dRdt = gamma*I
    return [dSdt, dIdt, dRdt]

betalist = [0.0005, 0.005, 0.0001, 0.00005,0.0001,0.0002,0.0001]
gammalist = [0.05,0.5,0.1,0.1,0.05,0.05,0.06]
#inital values for S, I, R
SIRvalues = [999,1,0]
times = range(0,500)

#creating a dataframe to store outputs for 7 scenarios
SIRframe = pandas.DataFrame({"beta":betalist, "gamma":gammalist, "MDI":0, "MDP":0, "percent_affected":0, "R0":0})

#calculating the R0 
SIRframe.R0 = (SIRframe.beta * 1000)/SIRframe.gamma

inc = range(0,500) #initializing incidence parameter
prev = range(0,500) #initilaizing prevalence parameter 

for i in range(0,7):
    pars = (betalist[i],gammalist[i])
    sim = spint.odeint(func=SIR, y0=SIRvalues, t=times, args=pars) #simulate model for each beta,gamma pair
    for j in range(500):
        inc[j] = sim[j,1] - sim[j-1,1] #calculate incidence for all time points
        SIRframe.iloc[i,0] = max(inc) #select maximum incidence 
        prev[j] = sim[j,1] / (sim[j,0] + sim[j,1] + sim[j,2]) #calculate prevalence for all time points
        SIRframe.iloc[i,1] = max(prev) #select maximum prevalence
        SIRframe.iloc[i,5] = (sim[499,1] + sim[499,2]) / (sim[499,0] + sim[499,1] + sim[499,2]) #calculate final percent affected


print SIRframe

