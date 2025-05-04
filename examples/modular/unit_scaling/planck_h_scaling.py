import math

# Define standard CODATA 2018 values for necessary constants in SI
G   = 6.67430e-11
e   = 1.602176634e-19
c   = 299792458.0
k_B = 1.380649e-23
h   = 6.62607015e-34 
k   = 1.3806490000e-23

Hz_kg = h / c**2
K_Hz  = k / h
G_n   = G * Hz_kg / c**3
t_P   = G_n**(1/2)
e_scaling = (  1e7 * Hz_kg * c  )**(1/2)

def calculate_scaling_factors(constants):

    rescale_factors = [
        {"symbol": "s",  "factor": t_P,             "swap_with": "t_P"},
        {"symbol": "m",  "factor": t_P * c,         "swap_with": "l_P"},
        {"symbol": "kg", "factor": Hz_kg/t_P,       "swap_with": "m_P"},
        {"symbol": "K",  "factor": 1/(t_P *  K_Hz), "swap_with": "T_P"},
        {"symbol": "C",  "factor": e_scaling,       "swap_with": "C_P"},
        {"symbol": "A",  "factor": e_scaling / t_P, "swap_with": "A_P"},
        {"symbol": "mol","factor": Hz_kg/t_P,       "swap_with": "mol_P"},
        {"symbol": "pi", "factor": 1.0,             "swap_with": "pi"},
        {"symbol": "Hz", "factor": 1.0,             "swap_with": "Hz"},
        {"symbol": "amu","factor": 1.0,             "swap_with": "amu"},
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
