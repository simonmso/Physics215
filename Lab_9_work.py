import error_rules as er
import math



water_density_theor = 1000  # kg/m^3
g = 9.8  # m/s^2

def calc_V(d, er_d, h, er_h):  # returns volume, uncertainty
    
    V = (math.pi / 4) * (d ** 2) * h
    er_V = er.rule_4(V, [d, h], [er_d, er_h], [2, 1])
    
    return V, er_V


def theor_F_boy(diameter, er_diam, height, er_height, density, density_er, submerged_percent):  # submerged percent should be decimal ex. 40% would be 0.40
    
    volume, er_volume = calc_V(diameter, er_diam, height, er_height)
    volume = volume * submerged_percent
    
    F_boy = g * density * volume
    er_F_boy = er.rule_4(Q=F_boy, values=[density, volume], uncertainties=[density_er, er_volume], exponents=[1, 1])
    
    return F_boy, er_F_boy


def calc_density(V, unc_V, kg, unc_kg):
    density = kg / V
    density_er = er.rule_4(Q=density, values=[V, kg], uncertainties=[unc_V, unc_kg], exponents=[1, -1])
    return density, density_er


print("------------------------- Prelab Quiz------------------------ ")

boyant_force, error_force = theor_F_boy(0.02, 0.0005,  # diameter w/ unc (m)
                                        0.05, 0.0005,  # height w/ unc (m)
                                        water_density_theor, 0,  # theoretical density of water
                                        0.50)  # submerged percent (decimal)

print("Theoretical Boyant Force at 50%: {:.5f} ± {:.8f} N\n".format(boyant_force, error_force))


print("-------------------- Part I - Theoretical --------------------\n")

# cylinder measurements
cyl_height = 0.0772  # m
cyl_er = 0.00005  # m
cyl_markings = [0.01915, 0.0384, 0.05695, 0.0772]  # m
cyl_diam = 0.02555  # m

# Submerged percentages
sub_cents = []
for mark in cyl_markings:
    sub_cents.append(mark / cyl_height)

# water measurements
water_V = 326 * (10 ** -6)  # m^3
water_V_er = 1 * (10 ** -6)  # m^3
water_mass = 0.4834 - 0.1617  # kg
water_mass_er = 0.0001
water_density, water_density_er = calc_density(water_V, water_V_er, water_mass, water_mass_er)


theor_boy_Fs = []
theor_boy_F_ers = []

for (idx, marking) in enumerate(cyl_markings):
    theor_f, theor_f_er = theor_F_boy(diameter=cyl_diam, er_diam=cyl_er,  # diameters
                                      height=cyl_height, er_height=cyl_er,  # heights
                                      density=water_density, density_er=water_density_er,  # densities
                                      submerged_percent=sub_cents[idx])  # submerged percent
    
    theor_boy_Fs.append(theor_f)
    theor_boy_F_ers.append(theor_f_er)
    
for (idx, f) in enumerate(theor_boy_Fs):
    print("F at {:.1f}% submerged: {:.3f} ± {:.8f} N".format(sub_cents[idx] * 100, f, theor_boy_F_ers[idx]))


print("\n-------------------- Part II - Theoretical -------------------\n")

# cylinder measurements
air_mass = 0.1113  # kg
masses = [0.1021, 0.0919, 0.0826, 0.0726]  # kg
m_unc = 0.0001

Fs = []
F_ers = []

for mass in masses:
    F = (air_mass - mass) * g
    F_er = er.rule_3([m_unc, m_unc])
    
    Fs.append(F)
    F_ers.append(F_er)


for (idx, f) in enumerate(Fs):
    print("F at {:.1f}% submerged: {:.3f} ± {:.8f} N".format(sub_cents[idx] * 100, f, F_ers[idx]))

"""
Output:
------------------------- Prelab Quiz------------------------ 
Theoretical Boyant Force at 50%: 0.07697 ± 0.00784933 N

-------------------- Part I - Theoretical --------------------

F at 24.8% submerged: 0.095 ± 0.00154649 N
F at 49.7% submerged: 0.190 ± 0.00162805 N
F at 73.8% submerged: 0.282 ± 0.00175040 N
F at 100.0% submerged: 0.383 ± 0.00192322 N

-------------------- Part II - Theoretical -------------------

F at 24.8% submerged: 0.090 ± 0.00014142 N
F at 49.7% submerged: 0.190 ± 0.00014142 N
F at 73.8% submerged: 0.281 ± 0.00014142 N
F at 100.0% submerged: 0.379 ± 0.00014142 N
"""
