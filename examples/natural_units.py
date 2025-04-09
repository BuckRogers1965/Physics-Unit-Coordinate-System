import argparse 
import math

####################################################################################

# we have to do this complex thing in python to import a specific python data file
import importlib.util
import os

# Define the path to the file you want to import
file_path = "../data_sets/constants.py"
module_name = "constants"

# Load the module dynamically
spec = importlib.util.spec_from_file_location(module_name, file_path)
constants = importlib.util.module_from_spec(spec)
spec.loader.exec_module(constants)

####################################################################################

# Access your data
grouped_constants = constants.grouped_constants

parser = argparse.ArgumentParser(
    description="Rescale physical constants and optionally show comments.",  # Main description
    epilog=(
        "Examples:\n"
        "  python rescaleconst05.py -a -f          # Print all entries with formulas\n"
        "  python rescaleconst05.py --comment      # Include comments in the output\n"
        "  python rescaleconst05.py -dd -dn -o     # Print discovery date, discoverer name, and origin fields\n\n\n"
        "  "
    ),
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument('-a', '--all',            action='store_true', help='print all entries')
                                             #^^^^^^  Makes it a flag (True if present, False if not)
parser.add_argument('-c', '--comment',        action='store_true', help='Include comments in the output')
parser.add_argument('-d', '--debug',          action='store_true', help='Include debug in the output')
parser.add_argument('-dd','--date',           action='store_true', help='Print discovery_date field')
parser.add_argument('-dn','--name',           action='store_true', help='Print discoverer_name field')
parser.add_argument('-o', '--origin',         action='store_true', help='Print origin field')
parser.add_argument('-f', '--formula',        action='store_true', help='Include formulas in the output')
parser.add_argument('-p', '--pronunciation',  action='store_true', help='Give pronouciation')
parser.add_argument('-r', '--reference',      action='store_true', help='Print reference field')
args = parser.parse_args() # Parse the arguments provided when running the script

if args.debug:
    print (f"   Comman line arguments found {args}")

####################################################################################

# --- Calculate Scaling Factors ---
# Using a subset of constants from included data file to define the scaling.
# You MUST ensure these keys exist in the 'Core Scaling Constants' group 
c = grouped_constants["Core Scaling Constants"]["speed_of_light_c"]["value"]
h = grouped_constants["Core Scaling Constants"]["planck_constant_h"]["value"]
k = grouped_constants["Core Scaling Constants"]["boltzmann_constant_k"]["value"]
e = grouped_constants["Core Scaling Constants"]["elementary_charge_e"]["value"]
Na = grouped_constants["Core Scaling Constants"]["avogadro_constant_Na"]["value"]
            
# --- Calculate Scaling Factors ---

# natural units - pulling units from each constants to scale the units.
rescale_factors = {
    "s":  1.0, 
    #"Hz": 1.0 / 1.0, # Hz = 1/s
    "m":  c,          # c is the definiton of the meter.
    "kg": h / (c**2), # h contains Hz to kg scaling
    "K":  h / k,      # k contains Hz to K scaling 
    "C":  e,          # e contains C scaling
    "mol": 1.0 / Na,  # mol is a simple human defined count
    "pi": math.pi     # ratio of circle circumfrence to radius
}

# --- Automatically calculate and add/update the Hz scaling factor ---
# Hz = 1/s => S_Hz = 1 / S_s
if "s" in rescale_factors:
    rescale_factors["Hz"] = 1.0 / rescale_factors["s"]
else:
    rescale_factors["s"] = 1.0 
    rescale_factors["Hz"] = 1.0 

####################################################################################

# This is where the magic happens
# we change the coordinate unit scaling of physics here

def rescale_value_by_units(constant_data, rescale_factors):
    original_value = constant_data["value"]
    unit_list = constant_data.get("units", []) # Use .get for safety
    rescaled_value = original_value
    units_applied_list = [] # Store the units that were actually scaled

    for unit_symbol, power in unit_list:
        if unit_symbol in rescale_factors:
            rescale_factor = rescale_factors[unit_symbol]
            # Avoid division by zero or issues with zero factors if they occur
            if rescale_factor != 0:
                 rescaled_value /= (rescale_factor ** power)
            elif original_value != 0 : # If factor is 0 but original value isn't, result is problematic (inf)
                 print(f"Warning: Rescale factor for {unit_symbol} is zero!")
                 rescaled_value = float('inf') # Or handle as an error

            units_applied_list.append(f"{unit_symbol}^{power}") # Record the unit and power applied
        # Optional: Warn if a unit is not found in rescale_factors
        # else:
        #     print(f"Warning: Unit '{unit_symbol}' not found in rescale_factors.")


    return rescaled_value, units_applied_list # Return both value and list of units applied

####################################################################################

# --- Display Original and Rescaled Constants Side-by-Side ---
# Adjusted to iterate through groups
print()
print()
print()
print(f"   {'Symbol':<8} {'Constant Name':<37} {'Original Value':<20} {'Rescaled Value':<20} {'Units Applied'}")
print("   ", end="")
print("-" * 125) # Adjusted width

for group_name, group_data in grouped_constants.items():
    print(f"\n   --- {group_name} ---") # Print group header
    # Sort constants within the group alphabetically by name for consistent output
    #sorted_constants = sorted(group_data.items())
    #for name, data in sorted_constants:
    for name, data in group_data.items():
         # Basic check for valid data structure
         if isinstance(data, dict) and all(k in data for k in ('value', 'units', 'symbol')):
             original_value = data["value"]
             # Use scientific notation for better alignment and readability
             original_value_str = f"{original_value:.10e}"
             rescaled_value, units_applied = rescale_value_by_units(data, rescale_factors)
             rescaled_value_str = f"{rescaled_value:.10e}" # Use scientific notation here too
             units_applied_str = " ".join(units_applied)

             print(f"   {data['symbol']:<8} {name:<37} {original_value_str:<20} {rescaled_value_str:<20} {units_applied_str}")

             # Loop through fields dynamically based on args or print all if --all flag is present
             comment_indent = " " * 11 
             for field, value in vars(args).items():
                 if field in data and (value or args.all):
                     if field == "formula":  # Special case for formula
                         print(f"{comment_indent}{data['symbol']} = {data[field]}")
                     if field == "comment":  # Special case for formula
                         print(f"{comment_indent}# {data['symbol']} = {data[field]}")
                     else:  # Print other fields
                         print(f"{comment_indent} {field} : {data[field]}")

         else:
             print(f"   Skipping malformed entry: {name}") # Error handling for bad entries

print("\n   --- Scaling Factors Used ---")
for unit_symbol, factor_value in rescale_factors.items():
    print(f"   {unit_symbol:<10} {factor_value:.20e}")
