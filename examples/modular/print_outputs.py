import argparse
import re

# Argument parsing setup
parser = argparse.ArgumentParser(
    description="Rescale physical constants and output in various formats.",
    epilog="Examples:\n"
           "  python converter.py --format=c\n"
           "  python converter.py --format=json\n"
           "  python converter.py --format=latex\n"
           "  python converter.py --format=markdown\n"
           "  python converter.py --format=python\n"
           "  python converter.py --format=text\n"
           "  python converter.py --format=xml\n"

)
parser.add_argument('--format', choices=['json', 'xml', 'python', 'text', 'c', 'latex', 'markdown'], default='json',
#parser.add_argument('--format', choices=['json', 'xml', 'python', 'text', 'c'], default='json',
                   help='Output format (json, xml, python, text, or c)')
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

    elif args.format == 'python':
        print("\n#   --- Output from Physics Unit Coordinate System ---")
        print("\n#   --- Scaling Factors Used ---")
        for unit_entry in rescale_factors:
            print(f"# {unit_entry['symbol']:<10} -> {unit_entry['factor']:.20e} -> {unit_entry['swap_with']:<10}")
        print()
        print()
    
    elif args.format == 'c':
        print("/* PHYSICS_UNIT_COORDINATE_SYSTEM.h */")
        print("#ifndef PUCS_PHYSICS_CONSTANTS_H")
        print("#define PUCS_PHYSICS_CONSTANTS_H")
        print("\n/*   --- Scaling Factors Used ---")
        for unit_entry in rescale_factors:
            print(f"{unit_entry['symbol']:<10} -> {unit_entry['factor']:.20e} -> {unit_entry['swap_with']:<10}")
        print("*/")
        print()
        print()

    elif args.format == 'latex':
        print(r"\documentclass{article}")
        print(r"\usepackage{amsmath, amssymb, geometry}")
        print(r"\begin{document}")
        print(r"\section*{Physics Unit Coordinate System Constants}")
    
    elif args.format == 'markdown':
        print("# Physics Unit Coordinate System Constants")
        print("```")
    
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
                print(f'  "{symbol}": {{"name": "{name}", "value": {rescaled_value}, "units": "{units_str}"}}', end='')
            
            elif args.format == 'xml':
                print(f'  <constant name="{name}" value="{rescaled_value}" units="{units_str}"/>')
            
            elif args.format == 'python':
                print(f"{symbol:<8} = {rescaled_value:<25}# {name:<30} {units_str}")
                symbols.append(symbol)  # Accumulate for later
    
            elif args.format == 'c':
                print(f"#define {symbol:<8}  {rescaled_value:30} /* {name:<30} {units_str} */")

            elif args.format == 'latex':
                #safe_units = units_str.replace("^", "^").replace(" ", r" \cdot ")
                #print (f"   {symbol}   {rescaled_value}    {units_str}    {safe_units}")
                safe_units = re.sub(r"\^(-?\d+)", r"^{\1}", units_str.replace(" ", r" \cdot "))
                print(rf"\[{symbol} = {rescaled_value} \quad \text{{({name})}} \quad \mathrm{{{safe_units}}}\]")
            
            elif args.format == 'markdown':
                print(f"{symbol} = {rescaled_value}   # {name} {units_str}")
    
    # Close structured formats
    if args.format == 'json':
        print("\n}")

    elif args.format == 'xml':
        print("</constants>")

    elif args.format == 'python':
        print("\n# Import all constants:")
        print(f"# from your_module import {', '.join(symbols)}")

    elif args.format == 'c':
        print("\n#endif /* PUCS PHYSICS_CONSTANTS_H */")

    elif args.format == 'latex':
        print(r"\end{document}")

    elif args.format == 'markdown':
        print("```")



