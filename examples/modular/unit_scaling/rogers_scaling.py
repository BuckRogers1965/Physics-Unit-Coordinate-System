import math
def calculate_scaling_factors(constants):
    c = constants["Core Scaling Constants"]["speed_of_light_c"]["value"]
    h = constants["Core Scaling Constants"]["planck_constant_h"]["value"]
    time = 1.8262416298**(1/2)
    charge = 1e5/4.5244383353e+14**(1/2)

    rescale_factors = [
        {"symbol": "s",  "factor": time, "swap_with": "s"},
        {"symbol": "m",  "factor": time * c/1e10, "swap_with": "m"},
        {"symbol": "kg", "factor": 7.3724973238e-51/(1e-50 * time), "swap_with": "kg"},
        {"symbol": "K",  "factor": 1e10/(2.0836619123e+10 * time), "swap_with": "K"},
        {"symbol": "C",  "factor": charge , "swap_with": "C"},
        {"symbol": "A",  "factor": charge, "swap_with": "A"},
        {"symbol": "mol","factor": 1.0, "swap_with": "mol"},
        {"symbol": "pi", "factor": 1.0, "swap_with": "pi"},
        {"symbol": "Hz", "factor": 1.0, "swap_with": "Hz"},
        {"symbol": "amu", "factor": 1/1.66053906660e-27 , "swap_with": "kg"},
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
