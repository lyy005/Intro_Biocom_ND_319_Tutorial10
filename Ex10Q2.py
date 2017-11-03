import numpy
import pandas
import scipy
from plotnine import *
#SIR model in epidemiology
#N=S+I+R (susceptible-->B-->infected-->g-->resistant); unidirectional
#R0=((B*(S+I+R))/g) ; R0 is how bad the disease is in the population; see YY's notes for where max daily incidence, max daily prevalence, percent affected, and basic reproduction number are found in a graph
