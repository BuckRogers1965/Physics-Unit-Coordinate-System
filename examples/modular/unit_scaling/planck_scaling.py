import math
def calculate_scaling_factors(constants):

    rescale_factors = [
        {"symbol": "s",  "factor": 5.391247E-44, "swap_with": "t_P"},
        {"symbol": "m",  "factor": 1.616255E-35, "swap_with": "l_P"},
        {"symbol": "kg", "factor": 2.176434E-8, "swap_with": "m_P"},
        {"symbol": "K",  "factor": 1.416784E+32, "swap_with": "T_P"},
        {"symbol": "C",  "factor": 3.2043532679e-19, "swap_with": "C_P"},
        {"symbol": "A",  "factor": 3.2043532679e-19, "swap_with": "A_P"},
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
