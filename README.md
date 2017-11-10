# Intro_Biocom_ND_319_Tutorial10


#Ex 10_2

I might have been doing something wrong, but I noticed that the provided parameter values to test for Beta and Gamma would result in negative infections in
certain cases. This happened when gamma was much higher than beta, and when beta was pretty low. These conditions would prevent an outbreak from happening since the
recovery rate (gamma) is higher than the infection rate (beta), but I believe it is an error in my implementation or a limitation of the model itself that the # of
infected individuals can dip below 0. I also noticed that all of the provided parameter values resulted in the highest rate of incidence change occuring on the
first day of infection. I'm not sure why case #3 and case #4 never see infected individuals, they both have a small beta value and a relatively large gamma.