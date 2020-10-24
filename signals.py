import numpy as np
from numpy import pi
import math

'''
Library of known signals. They work both for discrete and continuous operations.

Hint: the "args" that you see in every function is used to generalize the signals 
for calculation purposes (see signal_ops.py and scipy.integrate.quad docs).
'''


def delta(x, args=()):
    if round(x,5) == 0:
        return 1
    else:
        return 0

def u(x, args=()):
    if round(x,5) >= 0:
        return 1
    else:
        return 0

def sgn(x, args=()):
    return np.sign(x)

def r(x, args=()):
    N = args[0]
    if 0 <= round(x,5) < N:
        return 1
    else:
        return 0

def tri(x, args=(1,)):
    T = args[0]
    if -T < round(x,5) <= 0:
        return x/T+1
    elif 0 < round(x,5) < T:
        return 1-x/T
    else:
        return 0

def sin(x, args=(1,0)):
    N = args[0]
    theta = args[1]
    return math.sin(((2*pi)*x)/N + theta)

def cos(x, args=(1,0)):
    N = args[0]
    theta = args[1]
    return math.cos(((2*pi)*x)/N + theta)

def exp(x, args=()):
    a = args[0]
    return a**x

def rised_cos(x, args=(1,0.1)):
    T = args[0]
    alpha = args[1]
    if (1-alpha)*T/2 < abs(round(x,5)) < (1+alpha)*T/2:
        return 0.5*(1+np.cos(pi/(T*alpha)*(abs(x)-(1-alpha)*0.5*T)))
    elif abs(round(x,5)) <= (1-alpha)*T*0.5:
        return 1
    else:
        return 0

def sinc(x, args=()):
    if round(x,5) != 0:
        return np.sin(pi*x)/(pi*x)
    elif round(x,5) == 0:
        return 1

def decreasing_exp(x, args=(1,)):
    a = args[0]
    return math.exp(-a*x)*u(x)

def gaus(x, args=()):
    T = args[0]
    return math.exp(-(x**2)/(2*T**2))


'''
import numpy as np
import matplotlib.pyplot as plt
import signals
x = np.arange(-2,2.1,.01)
'''
