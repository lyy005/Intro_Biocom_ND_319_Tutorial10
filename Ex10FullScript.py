#---Part 1---
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


#---Part 2---
import numpy
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *
#SIR model in epidemiology
#N=S+I+R (susceptible-->B-->infected-->g-->resistant); unidirectional
#R0=((B*(S+I+R))/g) ; R0 is how bad the disease is in the population; see YY's notes for where max daily incidence, max daily prevalence, percent affected, and basic reproduction number are found in a graph

#state vairables=I/S=state parameters=r/B
#basic reproduction only initial values

#equations are dS/dt=-BIS, dI/dt=BIS-RI and dR/dt=RI
def epiSim(y,t,B,r):
    I=y[0]
    S=y[1]
    dSdt= (-B*I*S)
    dIdt= (B*I*S)-(r*I)
    dRdt= (r*I)
    return[dSdt,dIdt,dRdt]

#generate a dataframe containing a list of the B and r parameters
parB=[0.0005,0.005,0.0001,0.00005,0.0001,0.0002,0.0001]
parr=[0.05,0.5,0.1,0.1,0.05,0.05,0.06]
#create list for parameters
plotnames=["Parameter 1", "Parameter 2","Parameter 3","Parameter 4","Parameter 5","Parameter 6", "Parameter 7"]
#create list to hold plots
plots=["Plot1", "Plot2","Plot3","Plot4","Plot5","Plot6","Plot7"]
DataOut=pandas.DataFrame(numpy.zeros([7,6]),columns=['MaxIncidence','MaxPrevalence','PercentAffected','R0','Beta','Gamma'])
times=range(0,500)
#extract params from dataframe
for i in range(0,6):
    I0=[1]
    S0=[999,1,0]
    parms=(parB[i],parr[i])
    times=range(0,500)
    #simuate model
    sim=spint.odeint(func=epiSim,y0=S0,t=times,args=parms)
    #put output into dataframe
    sim_df=pandas.DataFrame({"t": times, "dSdt": sim[:,0], "dIdt": sim[:,1], "dRdt": sim[:,2]})
    #plot S, I, and R against time
    ggplot(sim_df, aes(x="t"))+geom_line(aes(y="dSdt"))+theme_classic()+xlab("Time")+ylab("N")+geom_line(aes(y="dIdt"), color = "red")+geom_line(aes(y="dRdt"), color = "blue")+ggtitle(plotnames[i])
    #calculate maximum incidence
    incidence=range(500)
    #creates a list to store incidence values
    for j in range(0, 500):
        #calculate incidence at every time step
        incidence[j]=sim_df.iloc[j,0]-sim_df.iloc[j-1,0]
    DataOut.iloc[i, 1]=max(incidence) #get the max
    #calculate max prevalence
    prevalence=sim_df.iloc[:,0]/1000 
    #calculate prevalence at every time step
    DataOut.iloc[i, 2]=max(prevalence) 
    #calculate percent affected
    DataOut.iloc[i, 3]=(sim_df.iloc[499,0]+sim_df.iloc[499,1])/100
    #calculate R0
    DataOut.iloc[i,4]=(parB[i]*1000)/parr[i]

print(plots)
print(DataOut)

#Gleaned information:
#increases in the gamma value appear to have a inverse-correlation with the calculated values
#increases in the beta values appear to have a direct-correlation with the calculated values 
#Thus...increase beta to increase the spread of the disease
