import math

#CONFIG 1 WORK
g = 9.8
f_one = g * 0.2 #at 0°
f_two = g * 0.1 #at 120°

#x and y components of force 2
f_two_x = f_two * math.cos((2 / 3) * math.pi)
f_two_y = f_two * math.sin((2 / 3) * math.pi) #aka 120°

f_three = -1 * (f_one + f_two_x) #in the x direction. To convert to degrees, take tha absolute value and note 180°
f_four = -1 * f_two_y #in the y direction


f_three_exp = g * .147
f_four_exp = g * .087
f_three_error = f_three_exp * (0.003 / .147) #no uncertainty for g makes this simple
f_four_error = f_four_exp * (.003 / .087)

print('Config 1:')
print('Force 3: {:.2f}N @ 180°'.format((-1 * f_three)))
print('Force 3 Experimental: {:.2f}N ±{:.2f}N @ 180° ±0.5°'.format(f_three_exp, f_three_error))
print('Force 4: {:.2f}N @ 270°'.format((-1 * f_four)))
print('Force 4 Experimental: {:.2f}N ±{:.2f}N @ 270° ±0.5°'.format(f_four_exp, f_four_error))

#-----------------------------------------

#CONFIG 2 WORK
#asks to combine force three and force 4 into a new force, force
#three prime. As it is a 2d vector, the angle theta will need to be specified
theta_three_prime = (180 * math.atan((f_four / f_three)) / math.pi) + 180 #direction
f_three_prime = math.sqrt((f_three ** 2) + (f_four ** 2)) #magnitude

theta_exp = 209 #degrees
f_three_prime_exp = g * .174
f_three_prime_error = f_three_prime_exp * (0.003 / .174)
theta_error = 1

print('\nConfig 2:')
print('Force 3 prime: {:.2f}N @ {:.2f}°'.format(f_three_prime, theta_three_prime))
print('Force 3 prime Experimental: {:.2f}N ±{:.2f}N @ {:.0f}° ±{:.0f}°'.format(f_three_prime_exp, f_three_prime_error, theta_exp, theta_error))

#--------------------------------------------

#CONFIG 3 WORK
fA = [(g * 0.2), 0, 0, (math.pi/3)] #Newtons, xN, yN, Radians
fB = [(g * 0.122), 0, 0, ((145 / 180) * math.pi)]
fC = [0, 0, 0, 0]

#assigning x and y components
fA[1] = fA[0] * math.cos(fA[3])
fA[2] = fA[0] * math.sin(fA[3])
fB[1] = fB[0] * math.cos(fB[3])
fB[2] = fB[0] * math.sin(fB[3])

fC[1] = -1 * (fA[1] + fB[1])
fC[2] = -1 * (fA[2] + fB[2])
fC[0] = math.sqrt((fC[1] ** 2) + (fC[2] ** 2))
fC[3] =(180 * math.atan((fC[2] / fC[1])) / math.pi) + 180

fEXP = [(g * .245), 0, 269, 1] #newtons, errorN, theta, error°
fEXP[1] = fEXP[0] * (0.003 / .245)

print('\nCongif 3:')
print('Force C: {:.2f}N @ {:.2f}°'.format(fC[0], fC[3]))
print('Force C Experimental: {:.2f}N ±{:.2f}N @ {}° ±{}°'.format(fEXP[0], fEXP[1], fEXP[2], fEXP[3]))
print('Mass C: {:.2f}g'.format((fC[0] / 9.8) * 1000))
print('Mass C Experimental: 245g ±3g')

