import math

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

def calculate_scaling_factors(constants):
    rescale_factors = [
        {"symbol": "s",  "factor": 1.0,                "swap_with": "s"},
        {"symbol": "m",  "factor": 1/3.28084,          "swap_with": "ft"},
        {"symbol": "kg", "factor": 1/2.20462,          "swap_with": "lbm"},
        {"symbol": "K",  "factor": 1.8,                "swap_with": "R"},
        {"symbol": "C",  "factor": 1.7288905439770867, "swap_with": "impC"},
        {"symbol": "mol","factor": 1.0,                "swap_with": "mol"},
        {"symbol": "pi", "factor": 1.0,                "swap_with": "pi"},
    ]

    composite_unit_module = load_module("./modular/composite_units.py", "composite_units")

    return composite_unit_module.rescale_composite_units(rescale_factors, "_i")
