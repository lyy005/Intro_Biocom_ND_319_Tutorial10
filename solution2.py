import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

def ddSim(y,t0,b,y):
    S=y[0]
    I=y[1]
    R=y[3]
    dSdt= -b * I * S
    dIdt = b * I * S - y * I
    dRdt = y * I
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
    