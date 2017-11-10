import pandas as pd
import scipy
import scipy.integrate as spint
from plotnine import *


def diseaseSim(y, t0, B, gam):
    S=y[0]
    I=y[0]
    R=y[0]
    
    dSdt=-B*I*S
    dIdt=(B*I*S)-(gam*I)
    dRdt=gam*I
    
    return(dSdt, dIdt, dRdt)
    
beta=[0.0005,0.005,0.0001,0.00005,0.0001,0.0002,0.0001]
gamma=[0.05,0.5,0.1,0.1,0.05,0.05,0.06]

times=range(0,500)
#case1


#case 1
y0=[999,1,0]
params=(beta[0],gamma[0])
sim=spint.odeint(func=diseaseSim,y0=y0,t=times,args=params)
simDF_1=pd.DataFrame({"t":times,"S":sim[:,0],"I":sim[:,1],"R":sim[:,2]})
plot_1=ggplot(simDF_1,aes(x="t", y="S"))+geom_line(color='blue')+geom_line(simDF_1,aes(x="t",y="I"), color='red')+ geom_line(simDF_1,aes(x="t",y="R"), color='green')+theme_classic()
plot_1
#maximum daily incidence is 292.26, occuring between day 0 and 1
max(simDF_1.iloc[:,0])
#max prevalence is 669.84
percent_infected_1=100*(1000-simDF_1.iloc[499,2])/1000
print(percent_infected_1)
#the percent infected is 99.6%
repno=(beta[0]*(999+1+0))/gamma[0]
print(repno)
#the reproduction number is 10

#case 2
y0=[999,1,0]
params=(beta[1],gamma[1])
sim=spint.odeint(func=diseaseSim,y0=y0,t=times,args=params)
simDF_2=pd.DataFrame({"t":times,"S":sim[:,0],"I":sim[:,1],"R":sim[:,2]})
plot_2=ggplot(simDF_2,aes(x="t", y="S"))+geom_line(color='blue')+geom_line(simDF_2,aes(x="t",y="I"), color='red')+ geom_line(simDF_2,aes(x="t",y="R"), color='green')+theme_classic()
plot_2
#maximum daily incidence is 653.27, occuring on day 1
max(simDF_2.iloc[:,0])
#max prevalence is 669.4
percent_infected_2=100*(1000-simDF_2.iloc[499,2])/1000
print(percent_infected_2)
#the percent infected is 99.99%
repno=(beta[1]*(999+1+0))/gamma[1]
print(repno)
#the reproduction number is 10

#case 3
y0=[999,1,0]
params=(beta[2],gamma[2])
sim=spint.odeint(func=diseaseSim,y0=y0,t=times,args=params)
simDF_3=pd.DataFrame({"t":times,"S":sim[:,0],"I":sim[:,1],"R":sim[:,2]})
plot_3=ggplot(simDF_3,aes(x="t", y="S"))+geom_line(color='blue')+geom_line(simDF_3,aes(x="t",y="I"), color='red')+ geom_line(simDF_3,aes(x="t",y="R"), color='green')+theme_classic()
plot_3
#Nobody ever gets sick, they recover too fast and infections are negative
max(simDF_3.iloc[:,0])
#max prevalence is 1 infected individual
percent_infected_3=100*(1000-simDF_3.iloc[499,2])/1000
print(percent_infected_3)
#the percent infected is 98.04%
repno=(beta[2]*(999+1+0))/gamma[2]
print(repno)
#the reproduction number is 1

#case 4
y0=[999,1,0]
params=(beta[3],gamma[3])
sim=spint.odeint(func=diseaseSim,y0=y0,t=times,args=params)
simDF_4=pd.DataFrame({"t":times,"S":sim[:,0],"I":sim[:,1],"R":sim[:,2]})
plot_4=ggplot(simDF_4,aes(x="t", y="S"))+geom_line(color='blue')+geom_line(simDF_4,aes(x="t",y="I"), color='red')+ geom_line(simDF_4,aes(x="t",y="R"), color='green')+theme_classic()
plot_4
#Nobody ever gets sick, they recover too fast and infections are negative
max(simDF_4.iloc[:,0])
#max prevalence is 1 infected individual
percent_infected_4=100*(1000-simDF_4.iloc[499,2])/1000
print(percent_infected_4)
#the percent infected is 96.15%
repno=(beta[3]*(999+1+0))/gamma[3]
print(repno)
#the reproduction number is 0.5

#case 5
y0=[999,1,0]
params=(beta[4],gamma[4])
sim=spint.odeint(func=diseaseSim,y0=y0,t=times,args=params)
simDF_5=pd.DataFrame({"t":times,"S":sim[:,0],"I":sim[:,1],"R":sim[:,2]})
plot_5=ggplot(simDF_5,aes(x="t", y="S"))+geom_line(color='blue')+geom_line(simDF_5,aes(x="t",y="I"), color='red')+ geom_line(simDF_5,aes(x="t",y="R"), color='green')+theme_classic()
plot_5
#max daily incidence is on 43.13, between day 0 and 1
max(simDF_5.iloc[:,0])
#max prevalence is 153.92 infected individuals
percent_infected_5=100*(1000-simDF_5.iloc[499,2])/1000
print(percent_infected_5)
#the percent infected is 98.04%
repno=(beta[4]*(999+1+0))/gamma[4]
print(repno)
#the reproduction number is 2

#case 6
y0=[999,1,0]
params=(beta[5],gamma[5])
sim=spint.odeint(func=diseaseSim,y0=y0,t=times,args=params)
simDF_6=pd.DataFrame({"t":times,"S":sim[:,0],"I":sim[:,1],"R":sim[:,2]})
plot_6=ggplot(simDF_6,aes(x="t", y="S"))+geom_line(color='blue')+geom_line(simDF_6,aes(x="t",y="I"), color='red')+ geom_line(simDF_6,aes(x="t",y="R"), color='green')+theme_classic()
plot_6
#max daily incidence is on 121.82, between day 0 and 1
max(simDF_6.iloc[:,0])
#max prevalence is 403.68 infected individuals
percent_infected_6=100*(1000-simDF_6.iloc[499,2])/1000
print(percent_infected_6)
#the percent infected is 99.00%
repno=(beta[5]*(999+1+0))/gamma[5]
print(repno)
#the reproduction number is 4

#case 7
y0=[999,1,0]
params=(beta[6],gamma[6])
sim=spint.odeint(func=diseaseSim,y0=y0,t=times,args=params)
simDF_7=pd.DataFrame({"t":times,"S":sim[:,0],"I":sim[:,1],"R":sim[:,2]})
plot_7=ggplot(simDF_7,aes(x="t", y="S"))+geom_line(color='blue')+geom_line(simDF_7,aes(x="t",y="I"), color='red')+ geom_line(simDF_7,aes(x="t",y="R"), color='green')+theme_classic()
plot_7
#max daily incidence is on 34.60, between day 0 and 1
max(simDF_7.iloc[:,0])
#max prevalence is 93.98 infected individuals
percent_infected_7=100*(1000-simDF_7.iloc[499,2])/1000
print(percent_infected_7)
#the percent infected is 98.04%
repno=(beta[6]*(999+1+0))/gamma[6]
print(repno)
#the reproduction number is 1.67


y0=[999,1,0]
params=(0.00001,0.005)
sim=spint.odeint(func=diseaseSim,y0=y0,t=times,args=params)
simDF_8=pd.DataFrame({"t":times,"S":sim[:,0],"I":sim[:,1],"R":sim[:,2]})
plot_8=ggplot(simDF_8,aes(x="t", y="S"))+geom_line(color='blue')+geom_line(simDF_8,aes(x="t",y="I"), color='red')+ geom_line(simDF_8,aes(x="t",y="R"), color='green')+theme_classic()
plot_8
