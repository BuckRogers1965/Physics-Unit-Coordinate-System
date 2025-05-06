import math

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

def calculate_scaling_factors(constants):
    c = constants["Core Scaling Constants"]["speed_of_light_c"]["value"]
    h = constants["Core Scaling Constants"]["planck_constant_h"]["value"]
    k = constants["Core Scaling Constants"]["boltzmann_constant_k"]["value"]
    e = constants["Units of Measure"]["elementary_charge_e"]["value"]
    Na = constants["Units of Measure"]["avogadro_constant_Na"]["value"]
    
    rescale_factors = [
        {"symbol": "s",  "factor": 1.0,        "swap_with": "s_a"},
        {"symbol": "m",  "factor": c,          "swap_with": "m_a"},
        {"symbol": "kg", "factor": (h / c**2)* 1.2355899638e+20 , "swap_with": "kg_a"},
        {"symbol": "K",  "factor": h / k,      "swap_with": "K_a"},
        {"symbol": "C",  "factor": e,          "swap_with": "C_a"},
        {"symbol": "mol","factor": 1.0/ Na,    "swap_with": "mol_a"},
        {"symbol": "pi", "factor": math.pi,    "swap_with": "pi_a"},
    ]

    composite_unit_module = load_module("./modular/composite_units.py", "composite_units")

    return composite_unit_module.rescale_composite_units(rescale_factors, "_z")
