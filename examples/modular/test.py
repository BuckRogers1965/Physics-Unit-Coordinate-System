unit_scaling_modes = [
    {"symbol": "s", "factor": 1.0, "swap_with": "s"},
    {"symbol": "m", "factor": 3.28084, "swap_with": "ft"},
    {"symbol": "kg", "factor": 2.20462, "swap_with": "lbm"},
    {"symbol": "K", "factor": 1.8, "swap_with": "R"},
    {"symbol": "C", "factor": 1.7288905439770867, "swap_with": "impC"},
    {"symbol": "mol", "factor": 1.0, "swap_with": "mol"},
    {"symbol": "pi", "factor": 1.0, "swap_with": "pi"}
]

def rescale_value_by_units(constant_data, unit_scaling_modes):
    original_value = constant_data["value"]
    unit_list = constant_data.get("units", [])  # Unit list has [("symbol", power)]
    rescaled_value = original_value
    units_applied_list = []  # Stores swapped symbols for units

    for unit_symbol, power in unit_list:
        for mode in unit_scaling_modes:
            if mode["symbol"] == unit_symbol:
                # Apply scaling
                rescale_factor = mode["factor"]
                if rescale_factor != 0:
                    rescaled_value /= (rescale_factor ** power)
                elif original_value != 0:
                    print(f"Warning: Rescale factor for {unit_symbol} is zero!")
                    rescaled_value = float('inf')  # Handle as problematic

                # Record swapped unit symbol with power
                swapped_unit = mode["swap_with"]
                units_applied_list.append(f"{swapped_unit}^{power}")
                break  # Found the unit, no need to check further

    return rescaled_value, units_applied_list

constant_data = {
    "value": 10.0,
    "units": [("m", 1), ("kg", -1), ("K", 2)]  # Example: 10 m * kg^-1 * K^2
}

rescaled_value, units_applied = rescale_value_by_units(constant_data, unit_scaling_modes)
print(f"Rescaled Value: {rescaled_value}")
print(f"Units Applied: {', '.join(units_applied)}")
