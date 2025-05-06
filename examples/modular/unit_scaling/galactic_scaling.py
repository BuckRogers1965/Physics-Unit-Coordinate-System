import math

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

def calculate_scaling_factors(constants):
    c = constants["Core Scaling Constants"]["speed_of_light_c"]["value"]
    h = constants["Core Scaling Constants"]["planck_constant_h"]["value"]
    k = constants["Core Scaling Constants"]["boltzmann_constant_k"]["value"]
    e = constants["Units of Measure"]["elementary_charge_e"]["value"]
    Na = constants["Units of Measure"]["avogadro_constant_Na"]["value"]
    

    # Define the conversion constants for clarity
    seconds_in_year = 31557600.0
    meters_in_parsec = 3.08567758149e16
    kg_in_solar_mass = 1.98847e30 # CODATA 2018 recommended value times G/G_N from IAU 2015 Resolution B3

    rescale_factors = [
        # --- Core Astrophysical Scaling ---
        {"symbol": "s",  "factor": seconds_in_year,     "swap_with": "ly"},
        {"symbol": "m",  "factor": meters_in_parsec,    "swap_with": "parsec"}, 
        {"symbol": "kg", "factor": kg_in_solar_mass,    "swap_with": "Msol"}, 
    
        # --- Other Base Units (kept at SI scale as requested) ---
        {"symbol": "K",  "factor": 1.0,                 "swap_with": "K"},
        {"symbol": "C",  "factor": 1.0,                 "swap_with": "C"},
        {"symbol": "A",  "factor": 1.0,                 "swap_with": "A"},
        {"symbol": "mol","factor": kg_in_solar_mass,    "swap_with": "mol_g"},

        # --- Dimensionless Ratio ---
        {"symbol": "pi", "factor": 1.0,                 "swap_with": "pi"},

        # --- Removed 'amu' scaling as it conflicts with direct 'kg' scaling ---
        # The definition of 'amu' would need to be revisited in the context of Msun_g.
    ]

    composite_unit_module = load_module("./modular/composite_units.py", "composite_units")

    return composite_unit_module.rescale_composite_units(rescale_factors, "_g")
