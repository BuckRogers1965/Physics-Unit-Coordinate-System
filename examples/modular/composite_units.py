# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module
rescale_units = load_module("./modular/rescale_units.py", "rescale_units")


def rescale_composite_units(unit_scaling, postpend):

    # load the composite unit module and extract the dictionary
    composite_unit_module = load_module("../data_sets/composite_units.py", "composite_units")
    composite_dictionary = composite_unit_module.composite_units

    for unit_name, unit_definition  in composite_dictionary.items():
        symbol = unit_definition['symbol']
        units = unit_definition['units']
        data = {
           "value": 1,
           "units": units
        }
        rescaled_value, units_applied = rescale_units.rescale_value_by_units(data, unit_scaling)
        entry = {
            "symbol": symbol,
            "factor": 1/rescaled_value,
            "swap_with": symbol + postpend,
        }
        unit_scaling.append(entry)

    return unit_scaling
    
