# Define the constants
c = 299792458.0  # m/s
h = 6.62607015e-34  # J*s
k = 1.380649e-23  # J/K
G   = 6.67430e-11


# This code calculates unit scaling factors derived from the fundamental constants
# of physics (c, h, k). These scaling factors demonstrate the relationships
# between different units (e.g., kilograms and Joules, Hertz and Kelvin)
# in the context of natural units.

# the unit scaling factors have the format of in_out for the unit conversions
# with the units of out/in

# Calculate the unit scaling factors
# and then their inverses
kg_J = c**2                # J/kg
J_kg = 1 / kg_J            # kg/J

Hz_kg = h / kg_J           # kg/Hz
kg_Hz = 1 / Hz_kg          # Hz/kg

K_Hz = k / (Hz_kg * kg_J)  # Hz/K
Hz_K = 1 / K_Hz            # K/Hz

Hz_J = Hz_kg * kg_J        # J/Hz
J_Hz = 1 / Hz_J            # Hz/J

K_J  = K_Hz * Hz_kg * kg_J # J/K
J_K  = 1/K_J               # K/J

K_kg = K_Hz * Hz_kg        # kg/K
kg_K = 1 / K_kg            # K/kg


# imperial unit scalings

kg_lbm = 2.20462           # lbm/kg
lbm_kg = 1 / kg_lbm        # kg/lbm

kg_slug = 0.0685218        # slug/kg
slug_kg = 1 / kg_slug      # kg/slug

ft_m = 0.3048              # m/ft
m_ft = 1 / ft_m            # ft/m

R_K = 5 / 9                # K/R
K_R = 9 / 5                # R/K

# Handle G Definition
G_n   = G * Hz_kg / c**3   # s^2
t_Ph  = G_n**(1/2)         # s
l_Ph  = c * t_Ph           # m
m_Ph  = Hz_kg/t_Ph         # kg
T_Ph  = Hz_K/t_Ph          # K

