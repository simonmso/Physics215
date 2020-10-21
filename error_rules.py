import math

"""
--------------------- Uncertainty Funcitons -----------------
"""

#Rule 1 (for Q = cA)
def rule_1(constant, unc_A):
    return abs(constant) * unc_A

#Rule 2 (for Q = c(A^m))
def rule_2(constant, unc_A, A, exp_m):
    return abs(constant * exp_m * (A ** (exp_m - 1))) * unc_A

#Rule 3 (for Q = A + B + ... or Q = A - B - ...)
def rule_3(uncertainties): #using an array allows this to work for any number of terms
    temp_sum = 0
    for uncertainty in uncertainties:
        temp_sum += uncertainty ** 2
    return (math.sqrt(temp_sum))

#Rule 4 (for Q = c(A^m)(B^n)...)
def rule_4(Q, values, uncertainties, exponents): #using arrays allows this to work for any number of terms
    temp_sum = 0
    for idx in range(len(values)):
        temp_sum += (exponents[idx] * (uncertainties[idx] / values[idx])) ** 2
    return abs(Q) * math.sqrt(temp_sum)

