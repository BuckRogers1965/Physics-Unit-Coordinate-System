import math

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

def calculate_scaling_factors(constants):
    rescale_factors = [
        {"symbol": "s",  "factor": 1.0,                "swap_with": "s"},
        {"symbol": "m",  "factor": 1/3.28084,          "swap_with": "ft"},
        {"symbol": "kg", "factor": 0.45359237,         "swap_with": "lbm"},
        #{"symbol": "kg", "factor": 1/2.20462,          "swap_with": "lbm"},
        {"symbol": "K",  "factor": 1.8,                "swap_with": "R"},
        {"symbol": "C",  "factor": 1.7288905439770867, "swap_with": "impC"},
        {"symbol": "mol","factor": 1.0,                "swap_with": "mol"},
        {"symbol": "pi", "factor": 1.0,                "swap_with": "pi"},
    ]

    composite_unit_module = load_module("./modular/composite_units.py", "composite_units")

    return composite_unit_module.rescale_composite_units(rescale_factors, "_i")


''' Some conceptual ideas to properly handle composite unit scaling to imperial properly

# Inside rescale_factors/imperial_scaling.py

import math
import scaling_calculator # Import your shared module

# Define conversion factors (SI to Imperial)
SI_kg_to_lbm = 1 / 0.45359237
SI_m_to_ft = 1 / 0.3048
SI_s_to_s = 1.0
# ... other base unit conversions (K to R, A to ?, mol to ?) ...

# Specific composite unit conversions (SI to NAMED Imperial)
SI_N_to_lbf = 0.2248089431
SI_J_to_ftlbf = 0.7375621493
# ... others (Pa to psi, W to hp, etc.) ...

# *** Define the system's postpend flag (empty string for Imperial) ***
postpend_flag = ""

def calculate_scaling_factors(constants, composite_units_data):
    # ... (extract constants if needed for base unit calculations) ...

    # --- 1. Initialize list with Base Unit entries and their scalings ---
    # Mapping from SI base units to Imperial base units
    rescale_factors_list = [
        {"symbol": "kg", "factor": SI_kg_to_lbm, "swap_with": "lbm"},
        {"symbol": "m",  "factor": SI_m_to_ft,  "swap_with": "ft"},
        {"symbol": "s",  "factor": SI_s_to_s,   "swap_with": "s"},
        # ... add other base units ...
         {"symbol": "Hz", "factor": 1.0 / SI_s_to_s, "swap_with": "Hz"}, # Hz is 1/s, Imperial uses the same Hz
        # Note: Imperial often uses Fahrenheit or Rankine for temperature.
        # Rankine is based on Kelvin, conversion is R = K * 9/5
        # So SI_K_to_R = 9/5 = 1.8
        {"symbol": "K",  "factor": 1.8, "swap_with": "R"},
    ]

    # --- 2. Add Specific NAMED Imperial Composite Conversions ---
    # These map directly from SI composite symbols to Imperial names
    rescale_factors_list.append({"symbol": "N", "factor": SI_N_to_lbf, "swap_with": "lbf"})
    rescale_factors_list.append({"symbol": "J", "factor": SI_J_to_ftlbf, "swap_with": "ft-lbf"})
    # ... add other specific Imperial composite entries ...

    # --- 3. Create a lookup for BASE unit factors (needed for generic composite calculation) ---
    # Mapping original SI base unit symbols to their Imperial *factors*
    # e.g., {'kg': SI_kg_to_lbm, 'm': SI_m_to_ft, 's': SI_s_to_s}
    base_unit_factors_dict = {item['symbol']: item['factor'] for item in rescale_factors_list if item['symbol'] in ['kg', 'm', 's', 'K', 'A', 'mol', 'cd']} # Only base units


    # --- 4. Loop through Composite Unit definitions and append generic scalings (Optional) ---
    # This part handles composites that *don't* have specific named Imperial units.
    # Decide if you want to include these 'dimensional' Imperial units.
    # If Yes:
    # for unit_name, unit_definition in composite_units_data.items():
    #     symbol = unit_definition['symbol']
    #     # Check if this unit was already handled by a specific conversion (N, J, etc.)
    #     if symbol not in [item['symbol'] for item in rescale_factors_list]:
    #         units_list = unit_definition['units']
    #         rescaled_value = scaling_calculator.calculate_composite_factor(units_list, base_unit_factors_dict)
    #         if rescaled_value is not None:
    #              # Use a clear name for these dimensional units
    #              entry = {
    #                  "symbol": symbol,
    #                  "factor": rescaled_value,
    #                  "swap_with": symbol + "_dimensional_imp",
    #              }
    #              rescale_factors_list.append(entry)

    # --- 5. Return the complete list and the postpend flag ---
    return rescale_factors_list, postpend_flag


'''
