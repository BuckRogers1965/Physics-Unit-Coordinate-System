import math

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

'''
The goal of this unit scaling system is different: to create a system that is simultaneously human-scaled, decimal-aligned (for mathematical modularity), AND explicitly demonstrates the unit scaling nature of constants. This specific combination of goals for a unit system design is novel.

Numerically the equivalent properties only change power as they convert between Temperture, frequency, mass, and energy.

Also both G and k_e are numerically 1, but scaled in power.
'''

def calculate_scaling_factors(constants):
    c = constants["Core Scaling Constants"]["speed_of_light_c"]["value"]
    h = constants["Core Scaling Constants"]["planck_constant_h"]["value"]
    k = constants["Core Scaling Constants"]["boltzmann_constant_k"]["value"]
    e = constants["Units of Measure"]["elementary_charge_e"]["value"]

    Hz_kg  = h/c**2
    K_Hz   = k/h
    time   = 1.8262416298**(1/2) 
    pi  = 3.141592653589793238

    # this sets the charge ratio to the same ratio as charge between two protons compared to the same G.
    #charge = (2.268661439176435e+39 / 8.2627176393e+20)**(1/2)

    # This matches charge k_e to the G force at macroscopic level.
#    charge = (1e-9/8.2627176393e+11)**(1/2)
    charge = e**2

    rescale_factors = [
        {"symbol": "s",   "factor": time ,                 "swap_with": "s_r"},
        {"symbol": "m",   "factor": time * c / 1e8 / pi,      "swap_with": "m_r"},
        {"symbol": "kg",  "factor": Hz_kg/(1e-50 * time) * 9.8696044011/pi , "swap_with": "kg_r"},
        {"symbol": "K",   "factor": (1e10/(K_Hz * time)) / (1),   "swap_with": "K_r"},
        {"symbol": "A",   "factor": charge,               "swap_with": "A_r"},
        {"symbol": "mol", "factor": Hz_kg/(1e-50 * time), "swap_with": "mol_r"},
        {"symbol": "pi",  "factor": 1.0,                  "swap_with": "pi"},
        {"symbol": "amu", "factor": Hz_kg/(1e-50 * time), "swap_with": "amu_r"},
    ]

    composite_unit_module = load_module("./modular/composite_units.py", "composite_units")

    return composite_unit_module.rescale_composite_units(rescale_factors, "_r")

