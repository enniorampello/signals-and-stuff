from scipy.integrate import quad
from scipy.stats import norm
import numpy as np
from numpy import pi
import cmath

"""
All the basic operations and calculations that work with the signals of signals.py.
"""


def time_average(signal, t0, t1):
    return round((1/(t1-t0))*quad(lambda x : signal(x), t0, t1)[0], 5)


def time_average_discrete(signal, t0, t1):
    return round((1/(t1-t0))*np.array([signal(n) for n in range (t0, t1+1)]).sum(), 5)


def energy(signal, t0, t1, cmplx=False):
    if cmplx:
        return round(quad(lambda x : signal(x).real**2 + signal(x).imag**2, t0, t1)[0], 5)
    else:
        return round(quad(lambda x : np.abs(signal(x))**2, t0, t1)[0], 5)


def energy_discrete(signal, t0, t1, cmplx=False):
    if cmplx:
        round(np.array([signal(n).real**2 + signal(n).imag**2 for n in range(t0, t1 + 1)]).sum(), 5)
    else:
        return round(np.array([np.abs(signal(n))**2 for n in range (t0, t1+1)]).sum(), 5)


def avg_power(signal, t0, t1, cmplx=False):
    return round((1/(t1-t0))*energy(signal, t0, t1, cmplx=cmplx), 5)


def avg_power_discrete(signal, t0, t1, cmplx=False):
    return round((1/(t1-t0))*energy_discrete(signal, t0, t1, cmplx=cmplx), 5)
