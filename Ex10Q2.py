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

    
    #inc=sim[1:500,1]-sim[0:499,1]
    #maxinc=numpy.max(inc)#create a model using odeint
    #prevalence=((sim[:,1])/(sim[:,0]+sim[:,1]+sim[:,2]))
    #maxprev=numpy.max(prevalence)
    #affected=((sim[499,1]+sim[499,2])/(sim[499,0]+sim[499,1]+sim[499,2]))
    #R0=(parB[i])*1000/parr[i]/parr[i]
    #DataOut.iloc[i,0]=maxinc
    #DataOut.iloc[i,1]=maxprev
    #DataOut.iloc[i,2]=affected
    #DataOut.iloc[i,3]=R0
    #DataOut.iloc[i,4]=parB[i]
    #DataOut.iloc[i,5]=parr[i]
