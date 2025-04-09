import math
def calculate_scaling_factors(constants):
    rescale_factors = [
        {"symbol": "s",  "factor": 1.0, "swap_with": "s"},
        {"symbol": "m",  "factor": 1.0, "swap_with": "m"},
        {"symbol": "kg", "factor": 1.0, "swap_with": "kg"},
        {"symbol": "K",  "factor": 1.0, "swap_with": "K"},
        {"symbol": "C",  "factor": 1.0, "swap_with": "C"},
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
