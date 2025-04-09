from load_mods import load_module

# --- Choose the desired scaling ---
#scaling_choice = "si" 
scaling_choice = "imperial" 
#scaling_choice = "natural" 
#scaling_choice = "atomic_electron" 
#scaling_choice = "galactic" 

scaling_module_path = f"./modular/unit_scaling/{scaling_choice}_scaling.py"
scaling_module_name = f"{scaling_choice}_scaling"

constants      = load_module("../data_sets/constants.py",           "constants") 
periodic_table = load_module("../data_sets/periodic_table.py", "periodic_table") 
scaling        = load_module(scaling_module_path,           scaling_module_name)
unit_scaling   = scaling.calculate_scaling_factors(constants.grouped_constants )
rescale_units  = load_module("./modular/rescale_units.py",      "rescale_units")

process       = load_module("./modular/print_periodic_table.py", "print_periodic_table")
process.print_periodic_table(
         periodic_table.periodic_table,
         unit_scaling,
         rescale_units.rescale_value_by_units)

print("\n   --- Scaling Factors Used ---")
for unit_entry in unit_scaling:
    print(f"   {unit_entry['symbol']:<10} -> {unit_entry['factor']:.20e} -> {unit_entry['swap_with']:<10}")

