import math

def calculate_scaling_factors(constants):
    c = constants["Core Scaling Constants"]["speed_of_light_c"]["value"]
    h = constants["Core Scaling Constants"]["planck_constant_h"]["value"]
    k = constants["Core Scaling Constants"]["boltzmann_constant_k"]["value"]
    e = constants["Core Scaling Constants"]["elementary_charge_e"]["value"]
    Na = constants["Core Scaling Constants"]["avogadro_constant_Na"]["value"]
    
    rescale_factors = [
        {"symbol": "s",  "factor": 1.0,        "swap_with": "s_a"},
        {"symbol": "m",  "factor": c,          "swap_with": "m_a"},
        {"symbol": "kg", "factor": (h / c**2)* 1.2355899638e+20 , "swap_with": "kg_a"},
        {"symbol": "K",  "factor": h / k,      "swap_with": "K_a"},
        {"symbol": "C",  "factor": e,          "swap_with": "C_a"},
        {"symbol": "mol","factor": 1.0/ Na,    "swap_with": "mol_a"},
        {"symbol": "pi", "factor": math.pi,    "swap_with": "pi_a"},
        {"symbol": "Hz", "factor": 1.0,        "swap_with": "Hz_a"},
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
