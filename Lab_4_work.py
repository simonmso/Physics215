import math
import numpy as np

"""
-----------------------Method 1-----------------------------------
"""
#Starting values
m = 0.0657 #ball mass (kg)
M = 0.1917 #pendulum mass (kg)
R = 0.277 #Length of pendulum (m)
g = 9.8 #m/s^2

#Gathered data
angles = [45, 46, 45.5, 46, 46, 46, 46, 46, 46, 46] #degrees


#Finding initial velocity
def findv( height ):
    return ((m + M) / m) * (math.sqrt(2*g*R*height))

dhs = [] #Delta Height values (radians)

for angle in angles: #converts angles to radians, appends difference in height
    rad = (angle / 180) * math.pi
    h = 1 - math.cos(rad)
    dhs.append(h)

avg_dh = sum(dhs) / len(dhs)

#This code was used to find the initial velocity using an incorrect method
# vis = []

# for dh in dhs: #finds 10 individual initial velocities
#     v = findv(dh)
#     vis.append(v)
    
# avg_vi = sum(vis) / len(vis) #ten initial, take the average

other_vi = findv(avg_dh) #computed once, using the avg dh

#Finding uncertainties
unc_m = 0.001 #ball mass uncertainty(kg)
m_exp = -1
unc_M = 0.001 #pendulum mass uncertainy (kg)
unc_R = 0.002 #m
R_exp = 0.5
unc_mSum = math.sqrt((unc_m ** 2) + (unc_M ** 2))
unc_h = np.std(dhs) / math.sqrt(len(dhs))
h_exp = 0.5

unc_vi = other_vi * math.sqrt(((unc_mSum / (m + M)) ** 2) + ((m_exp * (unc_m / m)) ** 2) + ((R_exp * (unc_R / R)) ** 2) + ((h_exp * (unc_h / h)) ** 2))

print('Method 1')
# print('Initial velocity (averaging 10 initial velocities): {:.2f} m/s'.format(avg_vi))
print('Initial velocity: {:.2f} ± {:.2f} m/s \n'.format(other_vi, unc_vi))

"""
--------------------------Method 2 ------------------------
"""
#Starting variables
y1 = .915 #m
y2 = .076 #m
y = y1 + y2 #m
dist1 = 1.937 #m
dist2 = .181 #m

#Gathered data
dists = [6, 6.5, 7, 7.2, 7.3, 8.5, 8.6, 8.8, 9, 9.2, 9.8] #cm

for idx in range(len(dists)): #converts dists to total distances (delta x)
    dists[idx] = (dists[idx] / 100) + dist1 + dist2

#Computing initial velocity
def findv_two( dist_avg):
    return dist_avg * math.sqrt(g / (2 * y))

avg_x = sum(dists) / len(dists)

method_two_vi = findv_two(avg_x)

#Finding Uncertainties
unc_y1 = .001 #m
unc_y2 = unc_y1 #height (m)
unc_y = math.sqrt((unc_y1 ** 2) + (unc_y2 ** 2))
unc_x = np.std(dists) / math.sqrt(len(dists))

unc_vi_two = method_two_vi * math.sqrt(((unc_x / avg_x) ** 2) + ((-0.5 * (unc_y / y)) ** 2))


print('Method 2')
print('Initial Velocity: {:.2f} ± {:.2f} m/s'.format(method_two_vi, unc_vi_two))









