import error_rules as er
import math


water_density = 1000  # kg/m^3
g = 9.8  # m/s^2

def calc_V(d, er_d, h, er_h):  # returns volume, uncertainty
    
    V = (math.pi / 4) * (d ** 2) * h
    er_V = er.rule_4(V, [d, h], [er_d, er_h], [2, 1])
    
    return V, er_V


def theor_F_boy(diameter, er_diam, height, er_height, density, submerged_percent):  # submerged percent should be decimal ex. 40% would be 0.40
    
    volume, er_volume = calc_V(diameter, er_diam, height, er_height)
    volume = volume * submerged_percent
    
    F_boy = g * water_density * volume
    er_F_boy = er.rule_2((g * water_density), er_volume, volume, 1)
    
    return F_boy, er_F_boy


boyant_force, error_force = theor_F_boy(0.02, 0.0005,  # diameter w/ unc (m)
                                        0.05, 0.0005,  # height w/ unc (m)
                                        7870,  # iron density (kg/m^3)
                                        0.50)  # submerged percent (decimal)

print("Theoretical Boyant Force: {:.5f} ± {:.8f} N".format(boyant_force, error_force))