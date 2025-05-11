from Modular_Unit_Scaling import c,h,k,kg_J,J_kg,Hz_kg,kg_Hz,K_Hz,Hz_K,Hz_J,J_Hz,K_J,J_K,K_kg,kg_K,G_n,t_Ph,G_n,t_Ph,l_Ph,m_Ph,T_Ph,G

# Print the values with at least 12 digits of accuracy
print()
print()
print()
print(f"   How constants c, h, and k act as unit scaling factors.")
print()
print()

print(f"   E=mc^2   E=m kg_J where kg_J = c^2 with units of J/kg")
print(f"   kg_J  = {kg_J:.12g} J/kg      J_kg = {J_kg:.12g} kg/J")
print(f"   This unit scaling exists because there are {c} meters in each light second.")
print()

print(f"   E=hf    h = Hz_kg kg_J  therefore Hz_kg = h/kg_J")
print(f"   Hz_J  = {Hz_J:.12g} J/Hz         J_Hz = {J_Hz:.12g} Hz/J")
print(f"   Hz_kg = {Hz_kg:.12g} kg/Hz     kg_Hz = {kg_Hz:.12g} Hz/kg")
print(f"   Hz_kg exists because there are {Hz_kg} kg in each Hz.")
print()

print(f"   E=kT    k = K_Hz Hz_kg kg_J therefore K_Hz = k/(Hz_kg kg_J)")
print(f"   K_J   = {K_J:.12g} J/K            J_K = {J_K:.12g} K/J")
print(f"   K_Hz  = {K_Hz:.12e} Hz/K     Hz_K = {Hz_K:.12g} K/Hz")
print(f"   K_Hz exists because there are {K_Hz} Hz in each Kelvin.")
print()

print(f"        In SI units: {1/K_Hz:.12g} K = 1 Hz = {Hz_kg:.12g} kg = {Hz_J:.12g} J")
print(f"   In natural units:        1 K_n        = 1 Hz =        1 kg_n        =         1 J_n")
print()

print(f"   The constants (c, h, k) have the values they do because SI units are defined far")
print(f"   from natural units, where these scaling factors would be unity.") # Clarified to include h and k
print(f"   In natural units (where 1 Hz = 1 kg = 1 K = 1 J), these scaling factors (kg_J, Hz_J, K_J) would all be 1.") 
print(f"   It is only by rescaling our units of measure to unity with each other that c=h=k=1 is true.")
print(f"   This shows that c, h, and k's SI values are solely unit conversion artifacts,") 
print(f"   not indicators of mysterious 'quantum magic' or deeply fundamental values beyond unit scaling.") 
print(f"   This does not diminish the constants, understanding their true nature makes them more important.")
print()

print(f"   T ~ f ~ m ~ J are all equivalences.")
print(f"   T <-- K_Hz --> Hz <-- Hz_kg --> kg <-- kg_J --> J")
print(f"   Since the units are equivalent you can simply scale between any unit")
print(f"   No one unit of measure is more important than any other.")

print()
print()

# Handle G Definition
print(f"   This is the definition of the Gravity constant")
print(f"   G   = t_Ph**2 * c**3 / Hz_kg  = {G:.12g} s^2")
print()
print(f"   First we remove the kg and meter defintions from G_SI.")
print(f"   G_n   = G * Hz_kg / c**3 = {G_n:.12g} s^2")
print()
print(f"   Then we isolate Planck time scale from the natural gravity time scale.")
print(f"   t_Ph  = G_n**(1/2) = {t_Ph:.12g} s")
print(f"   Note: This is the non reduced Planck time that G encodes.")
print(f"   Unit scaling has nothing to do with 1/2pi.")
print()
print("    Finally we remove the SI unit scaling for each unit of measure and scale by Planck time.")
print(f"   l_Ph = c * t_P   = {l_Ph:.12g} m")
print(f"   m_Ph = Hz_kg/t_P = {m_Ph:.12g} kg")
print(f"   T_Ph = Hz_K/t_P  = {T_Ph:.12g} K")

print()
print()

#print(f" {1:.6e} {2:.6e} {3:.6e} {4:.6e} {5:.6e} {6:.6e} {7:.6e} {8:.6e} {9:.6e} {10:.6e}  ")
#print(f" {c:.6e} {c**2:.6e} {c**3:.6e} {c**4:.6e} {c**5:.6e} {c**6:.6e} {c**7:.6e} {c**8:.6e} {c**9:.6e} {c**10:.6e}  ")
#print(f" {1/c:.6e} {1/c**2:.6e} {1/c**3:.6e} {1/c**4:.6e} {1/c**5:.6e} {1/c**6:.6e} {1/c**7:.6e} {1/c**8:.6e} {1/c**9:.6e} {1/c**10:.6e}  ")
#print()
#print()
