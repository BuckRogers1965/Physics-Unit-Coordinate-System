import math

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

def calculate_scaling_factors(constants):
    # Beware, here be dragons! 
    c = constants["Core Scaling Constants"]["speed_of_light_c"]["value"]
    h = constants["Core Scaling Constants"]["planck_constant_h"]["value"]
    k = constants["Core Scaling Constants"]["boltzmann_constant_k"]["value"]
    e = constants["Units of Measure"]["elementary_charge_e"]["value"]
    Na = constants["Units of Measure"]["avogadro_constant_Na"]["value"]
    e_rescale = e
    #e_rescale = e / 0.0072973525693**(1/2)
    
    rescale_factors = [
        {"symbol": "s",  "factor": 1.0,        "swap_with": "s_n"},
        {"symbol": "m",  "factor": c,          "swap_with": "m_n"},
        {"symbol": "kg", "factor": h / (c**2), "swap_with": "kg_n"},
        {"symbol": "K",  "factor": h / k,      "swap_with": "K_n"},
        {"symbol": "C",  "factor": e_rescale,  "swap_with": "C_n"},
        {"symbol": "A",  "factor": e_rescale,  "swap_with": "A_n"},
        {"symbol": "mol","factor": 1.0/ Na,    "swap_with": "mol_n"},
        {"symbol": "pi", "factor": math.pi,    "swap_with": "pi_n"},
        {"symbol": "amu", "factor": 1/1.66053906660e-27 * h / (c**2) , "swap_with": "kg_n"},
    ]

    composite_unit_module = load_module("./modular/composite_units.py", "composite_units")

    return composite_unit_module.rescale_composite_units(rescale_factors, "_n")
