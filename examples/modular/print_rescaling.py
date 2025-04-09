import argparse 

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
parser.add_argument('-u', '--units',          action='store_true', help='Print unit field')
args = parser.parse_args() # Parse the arguments provided when running the script

if args.debug:
    print (f"   Comman line arguments found {args}")


def format_units_with_ascii_exponents(units):
    formatted_units = []
    for base, power in units:
        if power == 1:
            formatted_units.append(base)
        else:
            superscript = str(power).replace('1', '¹').replace('2', '²').replace('3', '³').replace('4', '⁴').replace('5', '⁵').replace('6', '⁶').replace('7', '⁷').replace('8', '⁸').replace('9', '⁹').replace('0', '⁰').replace('-', '⁻')
            formatted_units.append(f"{base}{superscript}")
    return ' '.join(formatted_units)

def promote_exponents(unit_string):
    # Mapping for ASCII superscripts
    superscripts = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "-": "⁻"
    }
    
    # Split the string into parts to process
    parts = unit_string.split(" ")
    formatted_parts = []
    
    for part in parts:
        if "^" in part:
            # Split the unit from its exponent
            base, exponent = part.split("^")
            # Convert the exponent to superscript
            superscript = "".join(superscripts[char] for char in exponent)
            formatted_parts.append(f"{base}{superscript}")
        else:
            formatted_parts.append(part)
    
    # Join the processed parts back into a single string
    return " ".join(formatted_parts)


def print_rescaling (grouped_constants, rescale_factors, rescale_value_by_units):

    # --- Display Original and Rescaled Constants Side-by-Side ---
    # Adjusted to iterate through groups
    print()
    print()
    print()
    print(f"   {'Symbol':<8} {'Constant Name':<32} {'Original Value':<16} {'Rescaled Value':<16} {'Units Applied':29} {'Ratio'}")
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
    
                 print(f"   {data['symbol']:<8} {name:<32} {original_value_str:<16} {rescaled_value_str:<16} {promote_exponents(units_applied_str):<29} {original_value/ rescaled_value:8.8e}")

                 # Loop through fields dynamically based on args or print all if --all flag is present
                 indent = " " * 11 
                 for field, value in vars(args).items():
                     if field in data and (value or args.all):
                         if field == "formula":  # Special case for formula
                             print(f"{indent}   {data['symbol']} = {data[field]}")
                         elif field == "comment":  # Special case for comment
                             print(f"{indent}   # {data[field]}")
                         elif field == "units":  # Special case for units
                             print(f"{indent}    si units: {format_units_with_ascii_exponents(data[field])}")
                         else:  # Print other fields
                             print(f"{indent}   {field} : {data[field]}")

             else:
                 print(f"   Skipping malformed entry: {name}") # Error handling for bad entries

    print("\n   --- Scaling Factors Used ---")
    for unit_entry in rescale_factors:
        print(f"   {unit_entry['symbol']:<10} {unit_entry['factor']:.20e}")
