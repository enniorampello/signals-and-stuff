from scipy.integrate import quad
from scipy.stats import norm
import numpy as np
from numpy import pi

"""
All the basic operations and calculations that work with the signals of signals.py.
"""


def time_average(signal, t0, t1, args=()):
    return round((1/(t1-t0))*quad(lambda x : signal(x), t0, t1, args=args)[0], 5)

def time_average_discrete(signal, t0, t1, args=()):
    return round((1/(t1-t0))*np.array([signal(n, args) for n in range (t0, t1+1)]).sum(), 5)

def energy(signal, t0, t1, args=()):
    return round(quad(lambda x : np.abs(signal(x))**2, t0, t1, args=args)[0], 5)

def energy_discrete(signal, t0, t1, args=()):
    return round(np.array([np.abs(signal(n, args))**2 for n in range (t0, t1+1)]).sum(), 5)

