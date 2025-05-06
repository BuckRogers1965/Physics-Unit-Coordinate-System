import math

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

# Define standard CODATA 2018 values for necessary constants in SI
G_SI = 6.67430e-11
k_e_SI = 8.9875517923e9 # k_e = 1 / (4 * pi * epsilon0)
e_SI = 1.602176634e-19
c_SI = 299792458.0
k_B_SI = 1.380649e-23
h_SI = 6.62607015e-34 # Used for Planck h-based scaling
hbar_SI = h_SI / (2 * math.pi) # Used for standard Planck scaling
amu_SI = 1.66053906660e-27 # SI value of 1 atomic mass unit in kg

# --- Calculate SI values of Stoney Base Units (c=e=G=ke=1) ---
# From definitions: l_S = sqrt(G k_e e^2 / c^4), m_S = sqrt(k_e e^2 / G), t_S = l_S / c, Q_S = e.
# Derived: E_S = m_S c^2, T_S = E_S / k_B.

l_S_SI = math.sqrt(G_SI * k_e_SI * e_SI**2 / c_SI**4) # 1.380787...e-33 m
t_S_SI = l_S_SI / c_SI # 4.605889...e-42 s
m_S_SI = math.sqrt(k_e_SI * e_SI**2 / G_SI) # 1.855595...e-9 kg
Q_S_SI = e_SI # 1.602176634e-19 C

# Derived Stoney scales in SI
E_S_SI = m_S_SI * c_SI**2 # 1.667103...e-10 J
T_S_SI = E_S_SI / k_B_SI # 1.207520...e33 K
A_S_SI = Q_S_SI / t_S_SI # 3.478911...e10 A

def calculate_scaling_factors(constants):

    """
    Calculates scaling factors for Stoney Units (c=e=G=ke=1).
    Factor is (SI value of 1 Stoney Unit).
    Multiplying a quantity in SI by (1 / factor) converts it to Stoney Units.
    """
    rescale_factors = [
        {"symbol": "s",  "factor": t_S_SI, "swap_with": "t_S"},
        {"symbol": "m",  "factor": l_S_SI, "swap_with": "l_S"},
        {"symbol": "kg", "factor": m_S_SI, "swap_with": "m_S"},
        {"symbol": "K",  "factor": T_S_SI, "swap_with": "T_S"},
        {"symbol": "C",  "factor": Q_S_SI, "swap_with": "Q_S"},
        {"symbol": "A",  "factor": A_S_SI, "swap_with": "A_S"},
        {"symbol": "mol","factor": 1.0, "swap_with": "mol"}, 
        {"symbol": "pi", "factor": 1.0, "swap_with": "pi"}, 
    ]

    # load the composite unit module and extract the dictionary
    composite_unit_module = load_module("./modular/composite_units.py", "composite_units")

    return composite_unit_module.rescale_composite_units(rescale_factors, "_S")
