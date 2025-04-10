
'''
 The rescale_value_by_units function is the heart of the Physics
 Unit Coordinate System (PUCS). Its purpose is to transform physical
 constants or quantities from one unit system to another by applying
 scaling factors derived from the relationships between dimensions
 (e.g., mass, length, time).
 
 This function embodies the core philosophy of PUCS: unit systems are
 coordinate mappings, and physical constants are scaling factors that
 bridge dimensions within those mappings. By dynamically rescaling
 values and their associated units, it simplifies calculations,
 highlights the interconnectedness of physics, and makes it possible
 to work seamlessly across different measurement systems.

 In essence, this function unifies disparate unit systems by treating
 them as scaled representations of a single, underlying universal
 framework, making the complex relationships between constants clear
 and accessible.
'''

def rescale_value_by_units(constant_data, unit_scaling_modes):
    """
    Rescales the value of a physical constant based on unit scaling factors
    and returns the rescaled value along with the updated units.
    
    Parameters:
        constant_data (dict): A dictionary containing the value of the constant 
                              and its associated units, e.g., {"value": 100, "units": [("kg", 1), ("m", -2)]}.
        unit_scaling_modes (list): A list of scaling factor dictionaries, where each entry
                                   contains "symbol" (original unit), "factor" (scaling factor), 
                                   and "swap_with" (target unit).

    Returns:
        tuple: A tuple containing the rescaled value and a list of updated unit representations.
    """
    
    # Extract the original value of the constant
    original_value = constant_data["value"]

    # Retrieve the list of units and their powers from the constant_data dictionary
    # Format: [("unit_symbol", power)]
    unit_list = constant_data.get("units", [])
    
    # Initialize the rescaled value to the original value
    rescaled_value = original_value

    # List to store the new units after applying scaling
    units_applied_list = []

    # Iterate over each unit symbol and its associated power
    for unit_symbol, power in unit_list:
        matched = False  # Flag to determine if the unit matches any scaling mode
        
        # Search for the scaling mode corresponding to the current unit symbol
        for mode in unit_scaling_modes:
            if mode["symbol"] == unit_symbol:  # Found a matching scaling mode
                
                # Apply the scaling factor to rescale the value
                rescale_factor = mode["factor"]
                if rescale_factor != 0:
                    # Adjust the rescaled value by dividing by (rescale_factor^power)
                    rescaled_value /= (rescale_factor ** power)
                elif original_value != 0:
                    # Handle edge case where the rescale factor is zero (invalid)
                    print(f"Warning: Rescale factor for {unit_symbol} is zero!")
                    rescaled_value = float('inf')  # Set value to infinity to indicate a problem

                # Replace the current unit with its corresponding "swap_with" unit
                swapped_unit = mode["swap_with"]
                if power != 1:  # Include the power if it's not 1
                    units_applied_list.append(f"{swapped_unit}^{power}")
                else:
                    units_applied_list.append(f"{swapped_unit}")

                matched = True  # Mark the unit as successfully matched and scaled
                break  # No need to check further modes for this unit symbol

        # If no scaling factor was found for the unit, preserve the original unit and power
        if not matched:
            if power != 1:
                units_applied_list.append(f"{unit_symbol}^{power}")
            else:
                units_applied_list.append(f"{unit_symbol}")

    # Return the rescaled value and the updated unit list
    return rescaled_value, units_applied_list
