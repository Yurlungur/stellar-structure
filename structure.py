#!/usr/bin/env python2

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2016-05-10 23:40:40 (jmiller)>

# This is a simple script to calculate and plot the pressure in a star
# as a function of radius. Uses first-order Euler and the shooting
# method.

# Imports
# ------------------------------------------------
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# ------------------------------------------------

# Constants
# ------------------------------------------------
K=1.0 # polytrope K
n=3.0 # polytropic index
G=1.0 # Newton's constant
# ------------------------------------------------


def get_rho(P):
    """The equation of state gives ensity a function of pressure.
    We assume a polytropic equation of state:
    P = K*rho**((n+1)/n)
    which we invert"""
    out = P/K
    exponent = ((n+1)/n)
    rho = np.abs(out)**(-exponenent)
    return rho

def rhs(r,v):
    """Right-hand side
    takes in vector (M,P)
    and returns dM/dr, dP/dr
    also requires radius r"""
    M,P = v
    rho = get_rho(p)
    dmdr=4*np.pi*r*r*rho
    dpdr = - G*M*rho/(r*r)
    return np.array([dmdr,dpdr])

    
    
    
