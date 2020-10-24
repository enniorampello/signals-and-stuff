from scipy.integrate import quad
import numpy as np
from numpy import pi

'''
All the basic operations and calculations that work with the signals of signals.py.
'''


def energy(signal, a, b, args=()):
    return quad(lambda x : np.abs(signal(x))**2, a, b, args=args)[0]

def energy_discrete(signal, a, b, args=()):
    return np.array([np.abs(signal(n, args))**2 for n in range (a, b+1)]).sum()