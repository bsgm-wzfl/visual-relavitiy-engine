
import numpy as np

c = 299_792_458  # speed of light in m/s

def gamma(v):
    return 1 / np.sqrt(1 - (v**2 / c**2))

def time_dilation(proper_time, v):
    return gamma(v) * proper_time

def length_contraction(proper_length, v):
    return proper_length / gamma(v)

def lorentz_transform(x, t, v):
    g = gamma(v)
    x_prime = g * (x - v * t)
    t_prime = g * (t - v * x / c**2)
    return x_prime, t_prime