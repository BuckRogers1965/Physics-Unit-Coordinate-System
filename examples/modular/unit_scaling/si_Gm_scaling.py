import math

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

def calculate_scaling_factors(constants):
    c = constants["Core Scaling Constants"]["speed_of_light_c"]["value"]
    h = constants["Core Scaling Constants"]["planck_constant_h"]["value"]

    G= 6.674300e-11

    rescale_factors = [
        {"symbol": "s",  "factor": 1.0, "swap_with": "s"},
        {"symbol": "m",  "factor": G**(1/3), "swap_with": "m_g"},
        {"symbol": "kg", "factor": 1.0, "swap_with": "kg"},
        {"symbol": "K",  "factor": 1.0, "swap_with": "K"},
        {"symbol": "C",  "factor": 1.0, "swap_with": "C"},
        {"symbol": "mol","factor": 1.0, "swap_with": "mol"},
        {"symbol": "pi", "factor": 1.0, "swap_with": "pi"},
        {"symbol": "amu", "factor": 1/1.66053906660e-27 , "swap_with": "kg"},
    ]

    composite_unit_module = load_module("./modular/composite_units.py", "composite_units")

    return composite_unit_module.rescale_composite_units(rescale_factors, "_g")
