# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module
rescale_units = load_module("./modular/rescale_units.py", "rescale_units")

def check_deps_fails(units, unit_scaling):
    known_symbols = {entry['symbol'] for entry in unit_scaling if 'symbol' in entry}
    for unit, _ in units:
        if unit not in known_symbols:
            return 1
    return 0

# reads the composite unit list and processes them, appending to the unit scaling list which gets returned
def rescale_composite_units(unit_scaling, postpend):

    # load the composite unit module and extract the dictionary
    composite_unit_module = load_module("../data_sets/composite_units.py", "composite_units")
    composite_dictionary = composite_unit_module.composite_units

    for unit_definition  in composite_dictionary:
        symbol = unit_definition['symbol']
        units = unit_definition['units']
        count = unit_definition.get('count', 0)
        data = {
           "value": 1,
           "units": units
        }

        if check_deps_fails(units, unit_scaling):
            if count == 0: 
                # defer processing for composite unit whose units have not all been processed yet.
                deferred_entry = {
                    "symbol": symbol,
                    "units": units,
                    "count": 1,
                }
                composite_dictionary.append(deferred_entry)
            else:
                print (f" {symbol} has dependency issue in units: {units}")
            continue

        # otherwise the check was good process composite unit
        rescaled_value, units_applied = rescale_units.rescale_value_by_units(data, unit_scaling)
        entry = {
            "symbol": symbol,
            "factor": 1/rescaled_value,
            "swap_with": symbol + postpend,
        }
        unit_scaling.append(entry)

    return unit_scaling
    
