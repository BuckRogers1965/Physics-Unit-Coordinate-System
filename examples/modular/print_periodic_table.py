import argparse 
from pprint import pprint  # Import pprint for better formatting

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
'''
83: {'atomic_number': 83,
      'common_uses': ['Alloys', 'Medical treatments', 'Cosmetics'],
      'discovery': {'discoverer': 'Prehistoric',
                    'notes': 'Known since ancient times; thought to be stable '
                             'but faintly radioactive.',
                    'year': None},
      'electron_configuration': '[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³',
      'group': 15,
      'name': 'Bismuth',
      'period': 6,
      'physical_properties': {'atomic_mass': {'notes': 'Dominated by isotope '
                                                       'Bi-209.',
                                              'units': [('amu', 1)],
                                              'value': 208.98},
                              'boiling_point': {'notes': 'Applications in '
                                                         'medical and '
                                                         'industrial uses.',
                                                'units': [('K', 1)],
                                                'value': 1837},
                              'density': {'notes': 'Brittle, lustrous metal.',
                                          'units': [('kg', 1), ('m', -3)],
                                          'value': 9.78},
                              'melting_point': {'notes': 'Used in '
                                                         'low-melting-point '
                                                         'alloys.',
                                                'units': [('K', 1)],
                                                'value': 544.7}},
      'symbol': 'Bi'}}


'''

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

def get_group_name(group_number):
    """Returns the group name for a given group number in the periodic table."""
    group_names = {
        1: "Alkali Metals",
        2: "Alkaline Earth Metals",
        3: "Scandium",
        4: "Titanium",
        5: "Vanadium",
        6: "Chromium",
        7: "Manganese",
        8: "Iron",
        9: "Cobalt",
        10: "Nickel",
        11: "Copper",
        12: "Zinc",
        13: "Boron (Icosagens)",
        14: "Carbon (Crystallogens)",
        15: "Nitrogen (Pnictogens)",
        16: "Oxygen (Chalcogens)",
        17: "Halogens",
        18: "Noble Gases",
        19: "Lanthanides",
        20: "Actinides", 
    }
    return group_names.get(group_number, "Unknown")

def print_periodic_table(periodic_table, rescale_factors, rescale_value_by_units):
    # Handle debug option
    if args.debug:
        print("\n--- Debugging Information ---")
        print(f"Rescale Factors: {rescale_factors}")
        print(f"Periodic Table Data Loaded Successfully: {periodic_table}")
        print()

    print("\n--- Periodic Table ---")
    for atomic_number, element in periodic_table.items():
        print(f"\nElement: {element['name']} ({element['symbol']})")
        print(f"Group: {element['group']} {get_group_name(element['group'])}, Period: {element['period']}, Atomic Number: {atomic_number}")

        # Iterate through other physical properties
        for property_name, property_details in element['physical_properties'].items():
            value, units, notes = property_details['value'], property_details['units'], property_details['notes']
            #print (f"{property_name} {value} {units} {notes}")
            if value:
                scaled_value,  units_applied = rescale_value_by_units( {"value": value, "units": units}, rescale_factors)
                units_str = " ".join(units_applied)
                print (f"{property_name:<14} {scaled_value:<18.8} {promote_exponents(units_str):<13} {notes}")

        #print("\nInspecting `physical_properties`:")
        #pprint(element['physical_properties'])
        #pprint(periodic_table)

        # Print other properties based on flags
        if args.units:
            print("Units:", format_units_with_ascii_exponents(atomic_mass['units']))
        
        if args.date and 'discovery' in element:
            print(f"Discovery Date: {element['discovery'].get('year', 'Unknown')}")

        if args.name and 'discovery' in element:
            print(f"Discoverer: {element['discovery'].get('discoverer', 'Unknown')}")

        if args.origin and 'discovery' in element:
            print(f"Origin Notes: {element['discovery'].get('notes', 'No additional notes')}")

        if args.comment and 'common_uses' in element:
            print(f"Common Uses: {', '.join(element['common_uses'])}")

        # Print formulas if flag enabled
        if args.formula:
            print(f"Electron Configuration: {element.get('electron_configuration', 'Unknown')}")

