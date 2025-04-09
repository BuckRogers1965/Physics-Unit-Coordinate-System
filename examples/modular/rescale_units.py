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
                #units_applied_list.append(f"{swapped_unit}^{power}")
                if power != 1:
                    units_applied_list.append(f"{swapped_unit}^{power}")
                else:
                    units_applied_list.append(f"{swapped_unit}")
                break  # Found the unit, no need to check further

    return rescaled_value, units_applied_list
