import numpy as np
from numpy import pi
import math
import cmath

"""
Library of known signals. They work both for discrete and continuous operations.

Hint: the "args" that you see in every function is used to generalize the signals 
for calculation purposes (see signal_ops.py and scipy.integrate.quad docs).
"""


def delta(x):
    if round(x,5) == 0:
        return 1
    else:
        return 0

def u(x):
    if round(x,5) >= 0:
        return 1
    else:
        return 0

def sgn(x):
    return np.sign(x)

def r(x, N):
    if 0 <= round(x,5) < N:
        return 1
    else:
        return 0

def tri(x, T=1):
    if -T < round(x,5) <= 0:
        return x/T+1
    elif 0 < round(x,5) < T:
        return 1-x/T
    else:
        return 0

def sin(x, N=1, theta=0):
    return math.sin(x/N + theta)

def cos(x, N=1, theta=0):
    return math.cos(x/N + theta)

def exp(x, a=np.e):
    return a**x

def rised_cos(x, T=1, alpha=0.1):
    if (1-alpha)*T/2 < abs(round(x,5)) < (1+alpha)*T/2:
        return 0.5*(1+np.cos(pi/(T*alpha)*(abs(x)-(1-alpha)*0.5*T)))
    elif abs(round(x,5)) <= (1-alpha)*T*0.5:
        return 1
    else:
        return 0

def sinc(x):
    if round(x,5) != 0:
        return np.sin(pi*x)/(pi*x)
    elif round(x,5) == 0:
        return 1

def decreasing_exp(x, a):
    return math.exp(-a*x)*u(x)

def gaus(x, T):
    return math.exp(-(x**2)/(2*T**2))



def complex_exp(x, omega=1, rotating=False):
    """
    :return: access to the returned value must be done separately, i.e. doing z.real
    or z.imag. You can also use cmath to perform more complex operations. The returned
    value is equal to exp(j*freq*2pi*x) if rotating and to exp(j*omega*x) otherwise.
    """
    if rotating:
        frequency = omega
        re = math.cos(frequency * 2*pi * x)
        im = math.sin(frequency * 2*pi * x)
    else:
        re = math.cos(omega*x)
        im = math.sin(omega*x)
    return complex(re, im)
