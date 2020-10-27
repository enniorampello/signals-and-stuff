import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
import signals as s
from signal_ops import *

"""
Here you can find examples on how to properly perform the operations on the signals.

Hint: always create a function to build your signal.
"""


# Example on how to calculate the energy of a compound signal
def signal(x):
    return 2*s.u(x)*s.cos(x, 3)

e = energy(signal, -100, 100, cmplx=False)
print(e)
print(float(4*(50 + 3/4 * np.sin(2*100 / 3)))) # compare with the exact solution of the integral



# Example on how to calculate the energy of a complex compound signal
def complex_signal(x):
    return 5*s.complex_exp(x, 0.7, rotating=True)*s.exp(x)

e = energy(complex_signal, 0, 4, cmplx=True)
print(e)
print(12.5*s.exp(2*4) - 12.5) # compare with the exact solution of the integral