%matplotlib inline

import error_rules as er
import matplotlib.pyplot as plt
import numpy as np

def theorI (M, R):
    return (.5 * M * (R ** 2))

def expT (r, m, g, a): #expirimental torque
    torq = r * m * (g - a)
    return torq
        

g = 9.8 #m/s^2

#-----data------
masses = [0.025, 
      0.045, 
      0.065, 
      0.085, 
      0.105] #kg
unc_mass = 0.0001 #kg
accels = np.array([[0.002287, 0.002254, 0.002117, 0.002179, 0.002176, 0.002019],
               [0.006680, 0.006407, 0.006405, 0.006291, 0.006380, 0.006397],
               [0.01125, 0.01117, 0.01065, 0.01078, 0.01132, 0.0110],
               [0.01602, 0.01595, 0.01577, 0.01609, 0.01622, 0.01546],
               [0.02066, 0.02052, 0.02095, 0.02106, 0.02075, 0.02058]]) #m/s^2
r = 0.01520 #m
unc_r = 0.00002 #m

torqs = []
alphas = []

for (idx, mass) in enumerate(masses):
    torqs.append(expT(r, mass, g, np.average(accels[idx])))

for (idx, accel) in enumerate(accels):
    alphas.append(np.average(accel) / r)

for alpha in alphas:
    print(alpha, "W/s")
    
    
"""
--------------------------Plotting Code (Here - end)------------------------
"""

x = torqs
y = alphas
dy = [0]  #TODO: this should be your error in y array

#----------------------------------------------#

b,m=np.polynomial.polynomial.polyfit(x,y,1,w=dy)

#Write the equation for the best fit line based on the slope and intercept
fit = b+m*x

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

#-----------------------------------------------------------------------#
#Plot data on graph. Plot error bars and place values for slope, error in slope
#and goodness of fit on the plot using "annotate"

plt.figure(figsize=(15,10))
 
plt.plot(x, fit, color='green', linestyle='--')
plt.scatter(x, y, color='blue', marker='o')
 
 
#create labels  YOU NEED TO CHANGE THESE!!!
plt.xlabel('xvariable_changeme')
plt.ylabel('yvariable_changeme')
plt.title('Title_changeme')
 
plt.errorbar(x, y, yerr=dy, xerr=None, fmt="none") #don't need to plot x error bars
 
plt.annotate('Slope (units_changeme) = {value:.{digits}E}'.format(value=m, digits=2),
             (0.05, 0.9), xycoords='axes fraction')
 
plt.annotate('Error in Slope (units_changeme) = {value:.{digits}E}'.format(value=dm, digits=1),
             (0.05, 0.85), xycoords='axes fraction')
 
plt.annotate('Goodness of fit = {value:.{digits}E}'.format(value=N, digits=2),
             (0.05, 0.80), xycoords='axes fraction')

plt.show()
