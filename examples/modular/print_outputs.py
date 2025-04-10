import argparse

# Argument parsing setup
parser = argparse.ArgumentParser(
    description="Rescale physical constants and output in various formats.",
    epilog="Examples:\n"
           "  python converter.py --format=json\n"
           "  python converter.py --format=xml\n"
           "  python converter.py --format=python"
           "  python converter.py --format=text"
)
parser.add_argument('--format', choices=['json', 'xml', 'python', 'text'], default='json',
                   help='Output format (json, xml, python, or text)')
parser.add_argument('--suffix', default='', help='Suffix to append to symbol names')
args = parser.parse_args()


def print_outputs(grouped_constants, rescale_factors, rescale_value_by_units):
    """Process and stream out constants one fucking line at a time"""
    first = True
    symbols=[]
    
    # JSON needs opening/closing braces
    if args.format == 'json':
        print("{")
    
    # XML needs root element
    elif args.format == 'xml':
        print("<constants>")

    # XML needs root element
    elif args.format == 'python':
        print("\n#   --- Output from Physics Unit Coordinate System ---")
        print("\n#   --- Scaling Factors Used ---")
        for unit_entry in rescale_factors:
            print(f"# {unit_entry['symbol']:<10} -> {unit_entry['factor']:.20e} -> {unit_entry['swap_with']:<10}")
        print()
        print()
    
    
    for group_name, group_data in grouped_constants.items():
        for name, data in group_data.items():
            if not isinstance(data, dict):
                continue
            
            # Process one constant
            rescaled_value, units_applied = rescale_value_by_units(data, rescale_factors)
            symbol = data['symbol'] + args.suffix
            units_str = " ".join(units_applied)
            
            # Handle JSON commas
            if args.format == 'json' and not first:
                print(",")
            first = False
            
            # Stream output immediately
            if args.format == 'text':
                print(f"{symbol} {rescaled_value} {units_str}")
            
            elif args.format == 'json':
                print(f'  "{symbol}": {{"value": {rescaled_value}, "units": "{units_str}"}}', end='')
            
            elif args.format == 'xml':
                print(f'  <constant name="{name}" value="{rescaled_value}" units="{units_str}"/>')
            
            elif args.format == 'python':
                print(f"{symbol} = {rescaled_value}  # {units_str}")
                symbols.append(symbol)  # Accumulate for later
    
    # Close structured formats
    if args.format == 'json':
        print("\n}")
    elif args.format == 'xml':
        print("</constants>")
    elif args.format == 'python':
        print("\n# Import all constants:")
        print(f"# from your_module import {', '.join(symbols)}")



