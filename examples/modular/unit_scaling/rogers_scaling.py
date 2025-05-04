import math

'''
The goal of this unit scaling system is different: to create a system that is simultaneously human-scaled, decimal-aligned (for mathematical modularity), AND explicitly demonstrates the unit scaling nature of constants. This specific combination of goals for a unit system design is novel.

Numerically the equivalent properties only change power as they convert between Temperture, frequency, mass, and energy.

Also both G and k_e are numerically 1, but scaled in power.
'''



def calculate_scaling_factors(constants):
    c = constants["Core Scaling Constants"]["speed_of_light_c"]["value"]
    h = constants["Core Scaling Constants"]["planck_constant_h"]["value"]
    time = 1.8262416298**(1/2)
    charge = 1e5/4.5244383353e+14**(1/2)

    rescale_factors = [
        {"symbol": "s",   "factor": time,                            "swap_with": "s_r"},
        {"symbol": "m",   "factor": time * c/1e10,                   "swap_with": "m_r"},
        {"symbol": "kg",  "factor": 7.3724973238e-51/(1e-50 * time), "swap_with": "kg_r"},
        {"symbol": "K",   "factor": 1e10/(2.0836619123e+10 * time),  "swap_with": "K_r"},
        {"symbol": "C",   "factor": charge,                          "swap_with": "C_r"},
        {"symbol": "A",   "factor": charge,                          "swap_with": "A_r"},
        {"symbol": "mol", "factor": 7.3724973238e-51/(1e-50 * time), "swap_with": "mol_r"},
        {"symbol": "pi",  "factor": 1.0,                             "swap_with": "pi"},
        {"symbol": "Hz",  "factor": 1.0,                             "swap_with": "Hz"},
        {"symbol": "amu", "factor": 1.0,                             "swap_with": "amu"},
    ]

    # Find the scaling factor for "s"
    second_factor = next((entry["factor"] for entry in rescale_factors if entry["symbol"] == "s"), None)
    if second_factor is not None:
        # Check if Hz already exists in the list
        existing_Hz = next((entry for entry in rescale_factors if entry["symbol"] == "Hz"), None)
        if existing_Hz:
            # Update the existing Hz entry
            existing_Hz["factor"] = 1.0 / second_factor
        else:
            # Add a new Hz entry if it doesn't exist
            rescale_factors.append({
                "symbol": "Hz",
                "factor": 1.0 / second_factor,
                "swap_with": "Hz"
            })

    return rescale_factors
