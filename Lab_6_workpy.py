%matplotlib inline

import math
import numpy as np
import matplotlib.pyplot as plt


print("-------------- Part 1 --------------")

g = 9.8 #m/s^2
M_hanging = .0859 #kg
unc_M_hanging = .0001 #kg
m_hooks = 0.2083 #kg
unc_m_hooks = .0001 #kg

f_tension = M_hanging * g #N
unc_f_tension = unc_M_hanging * g

print('Tension force = {:.2f} ± {:.5f} N'.format(f_tension, unc_f_tension))

print("\n-------------- Part 2 --------------")

radii = [0.206, 0.187, 0.164, 0.151] #m
periods_ten = np.array([[14.19, 14.45, 14.2, 14.21, 14.19], 
                    [13.61, 13.59, 13.47, 13.66, 13.67], 
                    [12.62, 12.47, 12.42, 12.88, 12.23], 
                    [12.14, 12.28, 12.43, 12.23, 12.28]])
periods_one = [] #s
unc_periods = [] #uncertainty for each radius in sec

for periods in periods_ten:
    periods_one.append((sum(periods) / len(periods)) / 10) #Average data to get 4 distinct periods for 1 rotation
    
for periods in periods_ten:   
    unc = np.std(periods) / math.sqrt(len(periods))
    unc_periods.append(unc / 10)

periods_squared = []

for period in periods_one:
   periods_squared.append(period ** 2)

x = np.array(radii)
y = np.array(periods_squared)
dy = np.array(unc_periods)

#Find the intercept and slope, b and m
b,m=np.polynomial.polynomial.polyfit(x, y, 1 ,w=dy)

#Write the equation for the best fit line
fit = b+m*x    

f_centripital = (1 / m) * m_hooks * (math.pi ** 2) * 4 

                                                                                #Calculate the error in slope and intercept 
#def Delta(x, dy) is a function, and we will learn how to write our own at a later date. They are very useful!
def Delta(x, dy):
    D = (sum(1/dy**2))*(sum(x**2/dy**2))-(sum(x/dy**2))**2
    return D
 
D=Delta(x, dy)
 
dm = np.sqrt(1/D*sum(1/dy**2)) #error in slope
db = np.sqrt(1/D*sum(x**2/dy**2)) #error in intercept

#Calculate the "goodness of fit" from the linear least squares fitting document
def LLSFD2(x,y,dy):
    N = sum(((y-b-m*x)/dy)**2)
    return N
                      
N = LLSFD2(x,y,dy)

unc_f_centripital = f_centripital * math.sqrt(((unc_m_hooks / m_hooks) ** 2) + ((dm / m) ** 2))

print('Tension force = {:.2f} ± {:.5f} N'.format(f_centripital, unc_f_centripital))



"""
--------------------------Plotting Code (Here - end)------------------------
"""


#Plot data on graph.

plt.figure(figsize=(15,10))
 
plt.plot(x, fit, color='green', linestyle='--')
plt.scatter(x, y, color='blue', marker='o')
 
 
#create labels 
plt.xlabel('Radius (m)')
plt.ylabel('Period Squared (sec)')
plt.title('Period Squared over Radius')
 
plt.errorbar(x, y, yerr=dy, xerr=None, fmt="none") #don't need to plot x error bars
 
plt.annotate('Slope (sec^2 / m) = {value:.{digits}E}'.format(value=m, digits=2),
             (0.05, 0.9), xycoords='axes fraction')
 
plt.annotate('Error in Slope (sec^2 / m) = {value:.{digits}E}'.format(value=dm, digits=1),
             (0.05, 0.85), xycoords='axes fraction')

plt.annotate('Goodness of fit = {value:.{digits}E}'.format(value=N, digits=2),
             (0.05, 0.80), xycoords='axes fraction')

plt.show()