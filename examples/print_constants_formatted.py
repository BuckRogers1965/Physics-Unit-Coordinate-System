# Physics Unit Coordinate Scaling Program
# 
# This program demonstrates the core principles of the Physics Unit Coordinate System (PUCS).
# It applies coordinate scaling to physical constants, revealing their relationships within various unit systems.
#
# The goal is to generate scaled output in various formats to generate scaled output for input to other programs.
#
# The program dynamically loads modules for scaling factors, constants, and rescaling utilities,
# allowing users to switch between predefined unit systems (SI, Imperial, Natural, etc.) by simply adjusting a parameter.


# Dynamically loads reusable modules from specified file paths to keep the program modular and extensible.
from load_mods import load_module

# -----------------------------------------------------------------------
# STEP 1: Define the unit system to use
#
# The choice of `scaling_choice` determines which predefined unit system
# will be used to calculate scaling factors. Examples include:
# - SI: International System of Units (meters, kilograms, seconds)
# - Imperial: Commonly used in the US (feet, pounds, Fahrenheit)
# - Natural: Planck units where fundamental constants c=ħ=k=G=1
# - Atomic Electron: Units relevant to electron scales
# - Galactic: Units relevant to astrophysical scales
# - Time: A focus on temporal units
#
# Adjust the `scaling_choice` value to explore different systems of measurement.
# -----------------------------------------------------------------------

#scaling_choice = "si" 
#scaling_choice = "imperial" 
#scaling_choice = "natural" 
#scaling_choice = "rogers"
scaling_choice = "planck_h" 
#scaling_choice = "planck" 
#scaling_choice = "atomic_electron" 
#scaling_choice = "galactic" 
#scaling_choice = "time" 

# -----------------------------------------------------------------------
# STEP 2: Define the module paths for the chosen scaling system
#
# Based on the `scaling_choice`, the program dynamically loads the corresponding
# scaling module. This modular design ensures flexibility and extensibility,
# allowing additional scaling systems to be added without modifying the core logic.
# -----------------------------------------------------------------------

scaling_module_path = f"./modular/unit_scaling/{scaling_choice}_scaling.py"
scaling_module_name = f"{scaling_choice}_scaling"

# -----------------------------------------------------------------------
# STEP 3: Load constants and scaling factors
#
# The program loads a predefined dataset of grouped physical constants (`constants.grouped_constants`)
# and calculates the scaling factors for the chosen unit system. These scaling factors define
# how base units (e.g., meter, kilogram, second) are converted within the specified system.
# -----------------------------------------------------------------------

# Load the constants dataset
constants = load_module("../data_sets/constants.py", "constants") 

# Load the scaling module for the chosen unit system
scaling = load_module(scaling_module_path, scaling_module_name)

# Calculate scaling factors for the chosen unit system
unit_scaling = scaling.calculate_scaling_factors(constants.grouped_constants)

# -----------------------------------------------------------------------
# STEP 4: Load the rescaling utility
#
# The `rescale_units` module provides functionality for transforming physical constants
# based on the calculated scaling factors. It ensures numerical values are converted
# appropriately between unit systems while preserving their physical relationships.
# -----------------------------------------------------------------------

rescale_units = load_module("./modular/rescale_units.py", "rescale_units")

# -----------------------------------------------------------------------
# STEP 5: Process and print the rescaled constants in different output formats
#
# The `print_outputs` module handles the output, generating rescaled values of physical constants.
# This programs purpose is to generate output in various formats for use in other programs.
# -----------------------------------------------------------------------

process = load_module("./modular/print_outputs.py", "print_output")
process.print_outputs(
         constants.grouped_constants,
         unit_scaling,
         rescale_units.rescale_value_by_units)

#
# -----------------------------------------------------------------------
# END OF PROGRAM
#
# This program is part of the Physics Unit Coordinate System (PUCS) framework,
# which aims to redefine physical constants and unit systems as coordinate mappings,
# offering clarity and simplicity in understanding the relationships between dimensions.
# -----------------------------------------------------------------------
