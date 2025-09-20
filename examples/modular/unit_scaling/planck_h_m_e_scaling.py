


import math

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

# Define standard CODATA 2018 values for necessary constants in SI
G   = 6.67430e-11
e   = 1.602176634e-19
c   = 299792458.0
k_B = 1.380649e-23
h   = 6.62607015e-34 
k   = 1.3806490000e-23
m_e = 1.6697578400e-23 * 9.9999999998e-01# planck mass scaling

Hz_kg = h / c**2
K_Hz  = k / h
G_n   = G * Hz_kg / c**3
t_P   = G_n**(1/2) / m_e
e_scaling = (  1e7 * Hz_kg * c  )**(1/2) 
#e_scaling = (  1e7 * Hz_kg * c )**(1/2) * 3.4079462030e-02 ** (1/4)
#e_scaling = (  1e7 * Hz_kg * c / 0.26397533357678554*(2))**(1/2) 
e_scaling = (  1e7 * Hz_kg * c  )**(1/2) / 3.4079462030e-02 
e_scaling = 1.6021766340e-19

def calculate_scaling_factors(constants):

    rescale_factors = [
        {"symbol": "s",  "factor": t_P,             "swap_with": "t_Ph"},
        {"symbol": "m",  "factor": t_P * c ,         "swap_with": "l_Ph"},
        {"symbol": "kg", "factor": Hz_kg/t_P ,       "swap_with": "m_Ph"},
        {"symbol": "K",  "factor": 1/(t_P *  K_Hz ), "swap_with": "T_Ph"},
        #{"symbol": "C",  "factor": e_scaling,       "swap_with": "C_Ph"},
        {"symbol": "A",  "factor": e_scaling / t_P , "swap_with": "A_Ph"},
        {"symbol": "mol","factor": Hz_kg/t_P ,       "swap_with": "mol_Ph"},
        {"symbol": "pi", "factor": 1.0,             "swap_with": "pi"},
        {"symbol": "amu","factor": 1.0,             "swap_with": "amu"},
    ]

    composite_unit_module = load_module("./modular/composite_units.py", "composite_units")

    return composite_unit_module.rescale_composite_units(rescale_factors, "_Ph")



