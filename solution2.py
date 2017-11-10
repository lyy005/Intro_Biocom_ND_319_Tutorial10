import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

def ddSim(y,t0,b,a):
    S=y[0]
    I=y[1]
    R=y[2]
    dSdt= -b * I * S
    dIdt = b * I * S - a * I
    dRdt = a * I
    return [dSdt, dIdt, dRdt]
    
listb = (0.0005, 0.005, 0.0001, 0.00005, 0.0001, 0.0002, 0.0001)
listy = (0.05, 0.5, 0.1, 0.1, 0.05, 0.05, 0.06)

days = range(0,500)
susceptible = 999
infected = 1
resistant = 0
initial = [susceptible, infected, resistant]

for i in range(len(listb)):
    params = (listb[i], listy[i])
    modelSim=spint.odeint(func=ddSim,y0=initial,t=days,args=params)
    modelOutput = pandas.DataFrame({"Days":days,"S":modelSim[:,0], "I":modelSim[:,1], "R":modelSim[:,2]})
    incidence = []
    prevalence = []
    for j in range(0,500):
        if j != 0:
           incidence.append(modelOutput.loc[j, "I"] - modelOutput.loc[j-1, "I"])
            
        prevalence.append(modelOutput.loc[j, "I"] / (modelOutput.loc[j, "I"] + modelOutput.loc[j, "S"] + modelOutput.loc[j, "R"]))
    incidence.sort()
    prevalence.sort()
    
    print("B: " + str(listb[i]) + " y: " + str(listy[i]))
    print("Max incidence: " + str(incidence[0]))
    print("Max prevalence: " + str(prevalence[0]))
    pctAffected = (modelOutput.loc[499, "I"] + modelOutput.loc[499, "R"]) / (modelOutput.loc[499, "S"] + modelOutput.loc[499, "I"] + modelOutput.loc[499, "R"])
    print("Percent affected: " + str(pctAffected))
    bscReproduction = listb[i] * (modelOutput.loc[499, "S"] + modelOutput.loc[499, "I"] + modelOutput.loc[499, "R"]) / listy[i]
    print("Basic reproduction number: " + str(bscReproduction))
    print("############################################")
        
        
