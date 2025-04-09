# Physics Unit Coordinate Scaling Program with Periodic Table Integration
#
# This program expands on the Physics Unit Coordinate System (PUCS) framework
# by rescaling the periodic table alongside physical constants. It dynamically loads modules 
# for scaling factors, constants, periodic table data, and utilities, integrating them to reveal
# the relationships between elements and unit systems. The program uses modular design principles 
# to explore rescaled unit systems such as SI, Imperial, Natural Units, and others.

# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

# -----------------------------------------------------------------------
# STEP 1: Define the unit system to use
#
# Similar to the previous program, the choice of `scaling_choice` determines which 
# predefined unit system will be used for scaling. Options include:
# - SI: The International System of Units
# - Imperial: A widely used system in the US
# - Natural: Planck units where fundamental constants equal 1
# - Atomic Electron: Units centered on electron scales
# - Galactic: Astrophysical-scale unit systems
#
# Adjust `scaling_choice` to experiment with different systems of measurement.
# -----------------------------------------------------------------------

#scaling_choice = "si" 
#scaling_choice = "imperial" 
scaling_choice = "natural" 
#scaling_choice = "atomic_electron" 
#scaling_choice = "galactic" 

# -----------------------------------------------------------------------
# STEP 2: Define the module paths for the chosen scaling system
#
# The program dynamically identifies the module path and name based on `scaling_choice`.
# This flexibility allows seamless integration of additional scaling modules in the future.
# -----------------------------------------------------------------------

scaling_module_path = f"./modular/unit_scaling/{scaling_choice}_scaling.py"
scaling_module_name = f"{scaling_choice}_scaling"

# -----------------------------------------------------------------------
# STEP 3: Load constants and periodic table datasets
#
# By dynamically loading external data modules, this program combines physical constants
# with periodic table information, facilitating analysis of their interrelationships.
# -----------------------------------------------------------------------

# Load the constants dataset
constants = load_module("../data_sets/constants.py", "constants") 

# Load the periodic table dataset
periodic_table = load_module("../data_sets/periodic_table.py", "periodic_table") 

# -----------------------------------------------------------------------
# STEP 4: Load the scaling module and calculate scaling factors
#
# Scaling factors link different dimensional coordinates, ensuring consistency in unit conversions.
# These factors are calculated based on the loaded constants and the chosen unit system.
# -----------------------------------------------------------------------

# Load the scaling module
scaling = load_module(scaling_module_path, scaling_module_name)

# Calculate scaling factors for the chosen unit system
unit_scaling = scaling.calculate_scaling_factors(constants.grouped_constants)

# -----------------------------------------------------------------------
# STEP 5: Load the rescaling utility
#
# The `rescale_units` module facilitates value transformations based on the calculated scaling factors.
# This is critical for converting numerical values of constants and periodic table properties between systems.
# -----------------------------------------------------------------------

rescale_units = load_module("./modular/rescale_units.py", "rescale_units")

# -----------------------------------------------------------------------
# STEP 6: Process and print the rescaled periodic table
#
# The `print_periodic_table` module generates a detailed report of the periodic table after rescaling.
# This process showcases how unit systems transform atomic and physical properties of elements.
# -----------------------------------------------------------------------

process = load_module("./modular/print_periodic_table.py", "print_periodic_table")
process.print_periodic_table(
         periodic_table.periodic_table,
         unit_scaling,
         rescale_units.rescale_value_by_units)

# -----------------------------------------------------------------------
# STEP 7: Print the scaling factors used
#
# Finally, the program outputs the scaling factors applied, providing transparency
# in how units were transformed during rescaling. This enables users to verify the coordinate mappings.
# -----------------------------------------------------------------------

print("\n   --- Scaling Factors Used ---")
for unit_entry in unit_scaling:
    print(f"   {unit_entry['symbol']:<10} -> {unit_entry['factor']:.20e} -> {unit_entry['swap_with']:<10}")

# -----------------------------------------------------------------------
# END OF PROGRAM
#
# This program represents an extension of the PUCS framework, integrating data from the periodic table
# and demonstrating unit scaling across different measurement systems. By rescaling physical constants
# and element properties, it emphasizes the interconnectedness of physics and chemistry within unified coordinate mappings.
# -----------------------------------------------------------------------
