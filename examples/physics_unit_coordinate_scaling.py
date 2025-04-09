from load_mods import load_module

# --- Choose the desired scaling ---
#scaling_choice = "si" 
#scaling_choice = "imperial" 
scaling_choice = "natural" 
#scaling_choice = "atomic_electron" 
#scaling_choice = "galactic" 
#scaling_choice = "time" 

scaling_module_path = f"./modular/unit_scaling/{scaling_choice}_scaling.py"
scaling_module_name = f"{scaling_choice}_scaling"

constants     = load_module("../data_sets/constants.py",      "constants") 
scaling       = load_module(scaling_module_path,      scaling_module_name)
rescale_units = load_module("./modular/rescale_units.py", "rescale_units")

process       = load_module("./modular/print_rescaling.py", "print_rescaling")
process.print_rescaling(
         constants.grouped_constants,
         scaling.calculate_scaling_factors(constants.grouped_constants),
         rescale_units.rescale_value_by_units)
