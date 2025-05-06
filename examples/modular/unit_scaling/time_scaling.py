import math

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

def calculate_scaling_factors(constants):

    rescale_factors = [
        {"symbol": "s",  "factor": 1/1000, "swap_with": "s_n"},
        {"symbol": "m",  "factor": 1.0, "swap_with": "m_n"},
        {"symbol": "kg", "factor": 1.0, "swap_with": "kg_n"},
        {"symbol": "K",  "factor": 1.0, "swap_with": "K_n"},
        {"symbol": "C",  "factor": 1.0, "swap_with": "C_n"},
        {"symbol": "mol","factor": 1.0, "swap_with": "mol_n"},
        {"symbol": "pi", "factor": 1.0, "swap_with": "pi_n"},
        {"symbol": "amu", "factor": 1/1.66053906660e-27 , "swap_with": "kg_n"},
    ]

    composite_unit_module = load_module("./modular/composite_units.py", "composite_units")

    return composite_unit_module.rescale_composite_units(rescale_factors, "_n")
