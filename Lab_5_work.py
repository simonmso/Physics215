"""
For each collision:
Calculate the initial and final momenta of each cart.

Calculate the total initial momentum pi of the system.

Calculate the total final momentum pf of the system.

-----

Do your results for the final momenta agree within their uncertainties to the initial momenta?

Was momentum conserved in each collision?

Was kinetic energy conserved in the elastic collision? Was it conserved in the inelastic collision?
"""
import math

def momentum(masses, initial_vs, final_vs, Vuncert, case):
    #Trying to find:
    initial_ps = [] #initial momenta
    final_ps = [] #final momenta
    initial_p = 0 #total initial momentum
    final_p = 0 #total final momentum
    uncer_ps = [] #final uncertainties
    uncer_p = 0 #final uncertainty for total
    
    for idx in range(len(masses)):
        initial_ps.append(masses[idx] * initial_vs[idx]) #calculate initial momentum, add to array
    for idx in range(len(masses)):
        final_ps.append(masses[idx] * final_vs[idx])
        
    initial_p = sum(initial_ps)
    final_p = sum(final_ps)
    
    for idx in range(len(masses)):  #THIS UNCERTAINTY ONLY WORKS FOR SCENERIOS IN WHICH THE MASSES DO NOT COMBINE
        if (-0.0001 < final_vs[idx] < 0.0001):
            uncer_ps.append(0)
        else:
            uncer_ps.append(masses[idx] * Vuncert)
    #finding uncertainties
    for unc in uncer_ps:
        uncer_p += unc ** 2
    
    uncer_p = math.sqrt(uncer_p)
    
    #print all results
    print('\nCase {}:'.format(case)) 
    print('   Results:')
    print('   Total initial momentum = {:.3f} kg. m/s'.format(initial_p))
    print('   Total final momentum = {:.3f} ± {:.3f} kg. m/s\n'.format(final_p, uncer_p))
    print('   #  Initial P         Final P')
    for idx in range(len(masses)):
        print('   {}  {:.3f} kg. m/s     {:.3f} ± {:.3f} kg. m/s'.format(idx + 1, initial_ps[idx], final_ps[idx], uncer_ps[idx]))
    print('\n   Given values:')
    print('   #  Mass        Initial V    Final V')
    for idx in range(len(masses)):
        print('   {}  {:.3f} kg    {:.3f} m/s    {:.3f} m/s'.format(idx + 1, masses[idx], initial_vs[idx], final_vs[idx]))
    
def kinetic(masses, initial_vs, final_vs, Vunc):
    #Trying to find:
    initial_kes = [] #initial momenta
    final_kes = [] #final momenta
    initial_ke = 0 #total initial momentum
    final_ke = 0 #total final momentum
    unc_kes = []
    unc_ke = 0
    
    
    for idx in range(len(masses)):
        initial_kes.append(.5 * masses[idx] * (initial_vs[idx] ** 2))
    for idx in range(len(masses)):
        final_kes.append(.5 * masses[idx] * (final_vs[idx] ** 2))
        
    initial_ke = sum(initial_kes)
    final_ke = sum(final_kes)
        
    for idx in range(len(final_kes)): #THIS UNCERTAINTY ONLY WORKS FOR SCENERIOS IN WHICH THE MASSES DO NOT COMBINE
        unc_kes.append(.5 * masses[idx] * 2 * final_vs[idx] * Vunc)
        
    
    for unc in unc_kes:
        unc_ke += unc ** 2
    
    unc_ke = math.sqrt(unc_ke)
    
    print('\n   Kinetic Results:')
    print('   Total initial KE: {:.4f} J'.format(initial_ke))
    print('   Total final KE: {:.4f} ± {:.4f} J\n'.format(final_ke, unc_ke))
    for idx in range(len(initial_kes)):
        print('   Initial Kinetic Energy {}: {:.4f} J'.format(idx + 1, initial_kes[idx]))
    for idx in range(len(final_kes)):
        print('   Final Kinetic Energy {}: {:.4f} ± {:.4f} J'.format(idx + 1, final_kes[idx], unc_kes[idx]))
    

mass1 = 0.271 #kg
mass2 = 0.2715 #kg
massArray = [mass1, mass2]
unc_v = 0.04 #m/s

print('------------- Collision type #1 --------------')
#Case 1
momentum(massArray, [0.515, 0], [0, 0.471], unc_v, 1)
kinetic(massArray, [0.515, 0], [0, 0.471], unc_v)
#Case 2
momentum([mass1, mass2 + .250], [0.672, 0], [-0.211, 0.401], unc_v, 2)

print('\n\n------------- Collision type #2 --------------')
momentum(massArray, [0.515, -0.272], [-0.273, 0.454], unc_v, 1)

print('\n\n------------- Collision type #3 --------------')
momentum(massArray, [0.657, 0], [0.301, 0.301], unc_v,  1)
kinetic(massArray, [0.657, 0], [0.301, 0.301], unc_v)

# input()
