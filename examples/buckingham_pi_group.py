import sympy

# -----------------------------------------------------------------------------
# Step 0: The Knowledge Base (The "config.ini" of Physics)
# -----------------------------------------------------------------------------



# Define base SI constants as positive real symbols for simplification
h, G, c, kB, epsilon_0, mu_0, e, m_e, alpha = sympy.symbols('h G c k_B epsilon_0 mu_0 e m_e alpha', positive=True, real=True)

# Define common physical quantities as real symbols
T, M, M1, M2, r, F, wavelength = sympy.symbols('T M M1 M2 r F lambda', real=True)
E, f, r_s, P, m, a = sympy.symbols('E f r_s P m a', real=True)
v, p, I, R, V, Q, B, omega, x, k, n = sympy.symbols('v p I R V Q B omega x k n', real=True)
sigma, rho, A, L, C, phi, U, S = sympy.symbols('sigma rho A L C phi U S', real=True)

# Define the Complete Set of Planck Units (non-reduced, using h)
# These are the symbolic "basis vectors" of natural units

# Basic Planck units
t_P = sympy.sqrt(h * G / c**5)              # Planck time
l_P = sympy.sqrt(h * G / c**3)              # Planck length  
m_P = sympy.sqrt(h * c / G)                 # Planck mass
T_P = sympy.sqrt(h * c**5 / G) / kB         # Planck temperature

# Derived mechanical Planck units
E_P = sympy.sqrt(h * c**5 / G)              # Planck energy
F_P = c**4 / G                              # Planck force
P_P = c**7 / (h * G**2)                     # Planck pressure/energy density
#a_P = c**7 / (h * G**2)**(1/2) / c**2       # Planck acceleration = c/t_P
a_P = l_P / t_P**2
v_P = c                                     # Planck velocity (speed of light)
p_P = sympy.sqrt(h * c**3 / G)              # Planck momentum

# Electromagnetic Planck units
q_P = sympy.sqrt(4 * sympy.pi * epsilon_0 * h * c)  # Planck charge
V_P = sympy.sqrt(h * c**5 / G) / sympy.sqrt(4 * sympy.pi * epsilon_0 * h * c)  # Planck voltage
I_P = sympy.sqrt(4 * sympy.pi * epsilon_0 * h * c**7 / G)  # Planck current
R_P = sympy.sqrt(h * G / (4 * sympy.pi * epsilon_0 * c**3))  # Planck resistance
B_P = sympy.sqrt(h * c / G) / (4 * sympy.pi * epsilon_0 * h * c)  # Planck magnetic field

# Thermodynamic Planck units
S_P = kB                                    # Planck entropy
U_P = sympy.sqrt(h * c**5 / G)              # Planck internal energy (same as E_P)

# Additional derived units
rho_P = c**5 / (h * G**2)                   # Planck density
sigma_P = c**4 / (h * G)                    # Planck surface density
A_P = h * G / c**3                          # Planck area = l_P^2
Vol_P = (h * G / c**3)**(3/2)               # Planck volume = l_P^3
omega_P = c**5 / (h * G)**(1/2)             # Planck angular frequency = 1/t_P
k_P = c**3 / (h * G)**(1/2)                 # Planck wave number = 1/l_P

# Store all Planck units in a dictionary for easy substitution
planck_units = {
    't_P': t_P, 'l_P': l_P, 'm_P': m_P, 'T_P': T_P,
    'E_P': E_P, 'F_P': F_P, 'P_P': P_P, 'a_P': a_P, 'v_P': v_P, 'p_P': p_P,
    'q_P': q_P, 'V_P': V_P, 'I_P': I_P, 'R_P': R_P, 'B_P': B_P,
    'S_P': S_P, 'U_P': U_P, 'rho_P': rho_P, 'sigma_P': sigma_P,
    'A_P': A_P, 'Vol_P': Vol_P, 'omega_P': omega_P, 'k_P': k_P
}

# -----------------------------------------------------------------------------
# The Automated Formula Forge Engine
# -----------------------------------------------------------------------------

def derive_formula(postulate_string, target_variable, substitutions, description=""):
    """
    A general-purpose engine to derive physical formulas from a dimensionless postulate.
    
    Args:
        postulate_string (str): A string representing the core dimensionless law.
        target_variable (sympy.Symbol): The variable to solve for.
        substitutions (dict): A dictionary mapping symbols to their SymPy objects.
        description (str): Optional description of the physical law being derived.
    
    Returns:
        sympy.Eq: The final derived formula for the target variable.
    """
    
    print(f"--- Deriving formula for: {target_variable} in {description} ---")
    #if description:
        #print(f"    {description}")
    
    # 1. Parse the string and create a SymPy Equality object
    try:
        postulate_eq = sympy.sympify(f"Eq({postulate_string})", locals=substitutions)
    except Exception as e:
        print(f"Error parsing the postulate string: {e}")
        return None
        
    print(f"\n1. Postulate: {postulate_string}")
    print(f"   Symbolic Form: {postulate_eq}")

    # 2. Solve for the target variable symbolically
    try:
        solution_expr = sympy.solve(postulate_eq, target_variable)[0]
    except (IndexError, TypeError):
        print("   Could not solve for the target variable. Check the formula.")
        return None
        
    print(f"2. Solved for {target_variable}: Eq({target_variable}, {solution_expr})")

    # 3. Substitute the full Planck unit definitions
    final_expr = solution_expr.subs(substitutions)
    print(f"3. Substituted Planck definitions...")
    
    # 4. Simplify the final expression
    simplified_expr = sympy.simplify(final_expr)
    final_formula = sympy.Eq(target_variable, simplified_expr)
    
    print(f"4. Simplified Result:")
    print(f"   >>> {final_formula}\n")
    
    return final_formula

# -----------------------------------------------------------------------------
# Main Execution: Testing the Engine on Multiple Problems
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    
    # Define a comprehensive substitution dictionary
    all_symbols = {
        # Physical quantities
        'T': T, 'M': M, 'M1': M1, 'M2': M2, 'r': r, 'F': F, 'E': E, 'wavelength': wavelength,
        'f': f, 'r_s': r_s, 'P': P, 'm': m, 'a': a, 'v': v, 'p': p, 'I': I, 'R': R,
        'V': V, 'Q': Q, 'B': B, 'omega': omega, 'x': x, 'k': k, 'n': n, 'sigma': sigma,
        'rho': rho, 'A': A, 'L': L, 'C': C, 'phi': phi, 'U': U, 'S': S,
        
        # Constants
        'h': h, 'G': G, 'c': c, 'k_B': kB, 'epsilon_0': epsilon_0, 'mu_0': mu_0,
        'e': e, 'm_e': m_e, 'alpha': alpha,
        
        # Planck units
        **planck_units
    }

    print()
    print(" These formulas are derived by dimensional analysis of Π groups,")
    print("     showing the deep unity underlying all of physics.")
    print()

    # ==========================================================================
    print(" # GRAVITATIONAL AND RELATIVISTIC PHYSICS \n")
    # ==========================================================================
    
    # Hawking Temperature
    derive_formula("T/T_P, m_P/M", T, all_symbols, 
                  "Hawking radiation temperature of a black hole")
    
    # Newton's Law of Gravitation
    derive_formula("F/F_P, (M1*M2/m_P**2) * (l_P**2/r**2)", F, all_symbols,
                  "Newton's law of universal gravitation")

    # Schwarzschild Radius
    derive_formula("r_s/l_P, M/m_P", r_s, all_symbols,
                  "Schwarzschild radius of a black hole")

    # Mass-Energy Equivalence (E=mc²)
    derive_formula("E/E_P, M/m_P", E, all_symbols,
                  "Einstein's mass-energy equivalence")

    # ==========================================================================
    print(" # QUANTUM MECHANICS \n")
    # ==========================================================================

    # Planck-Einstein Relation (E=hf)
    derive_formula("E/E_P, f*t_P", E, all_symbols,
                  "Planck-Einstein energy-frequency relation")

    # Thermal de Broglie Wavelength
    derive_formula("wavelength/l_P, 1/sqrt(M*T / (m_P*T_P))", wavelength, all_symbols,
                  "Thermal de Broglie wavelength")

    # Momentum-Wavelength Relation (p = h/λ)
    derive_formula("p/p_P, l_P/wavelength", p, all_symbols,
                  "de Broglie momentum-wavelength relation")

    # Uncertainty Principle (ΔxΔp ≥ ℏ/2, using Δx ~ x, Δp ~ p)
    derive_formula("(x/l_P) * (p/p_P), 1", x, all_symbols,
                  "Heisenberg uncertainty principle (order of magnitude)")

    # ==========================================================================
    print(" # THERMODYNAMICS AND STATISTICAL MECHANICS \n")
    # ==========================================================================

    # Stefan-Boltzmann Law for radiation pressure
    derive_formula("P/P_P, (T/T_P)**4", P, all_symbols,
                  "Stefan-Boltzmann radiation pressure")

    # Blackbody energy density
    derive_formula("rho/rho_P, (T/T_P)**4", rho, all_symbols,
                  "Blackbody energy density")

    # Blackbody energy 
    derive_formula("E/E_P, (T/T_P)**4", E, all_symbols,
                  "Blackbody energy")

    # Wien's Displacement Law (λ_max ∝ 1/T)
    derive_formula("(wavelength/l_P) * (T/T_P), 1", wavelength, all_symbols,
                  "Wien's displacement law")

    # Ideal gas pressure (P ∝ ρT for fixed molecular mass)
    derive_formula("P/P_P, (T/T_P) * (l_P**3/l**3)", P, all_symbols,
                   "Ideal gas pressure")  


#P/P P =N⋅(T/T P)⋅(V P /V)

    # ==========================================================================
    print(" # CLASSICAL MECHANICS \n")
    # ==========================================================================

    print()
    print("These classic formulas the input units match the ouput unit so the ratio of the constants is 1.")
    print()

    # Newton's Second Law (F = ma)
    derive_formula("F/F_P, (m/m_P) * (a/a_P)", F, all_symbols,
                  "Newton's second law of motion")

    # Kinetic Energy (E = ½mv²)
    derive_formula("E/E_P, (m/m_P) * (v/v_P)**2", E, all_symbols,
                  "Classical kinetic energy")

    # Momentum (p = mv)
    derive_formula("p/p_P, (m/m_P) * (v/v_P)", p, all_symbols,
                  "Classical momentum")

    # Gravitational Potential Energy
    derive_formula("E/E_P, (M1*M2/m_P**2) * (l_P/r)", E, all_symbols,
                  "Gravitational potential energy")

    # Simple Harmonic Oscillator frequency
    derive_formula("omega/omega_P, sqrt(F/(m*l_P)) * sqrt(m_P/F_P)", omega, all_symbols,
                  "Simple harmonic oscillator frequency")

    # ==========================================================================
    print(" # ELECTROMAGNETIC THEORY \n")
    # ==========================================================================

    # Coulomb's Law
    derive_formula("F/F_P, (Q**2/(4*sympy.pi*epsilon_0)) * (1/(l_P**2*m_P*c**2)) * (l_P**2/r**2)", F, all_symbols,
                  "Coulomb's electrostatic force")

    # Ohm's Law (V = IR) 
    derive_formula("V/V_P, (I/I_P) * (R/R_P)", V, all_symbols,
                  "Ohm's law")

    # Magnetic force on current (F = BIL)
    derive_formula("F/F_P, (B/B_P) * (I/I_P) * (L/l_P)", F, all_symbols,
                  "Magnetic force on current-carrying conductor")

    # ==========================================================================
    print(" # WAVE PHYSICS \n")
    # ==========================================================================

    # Wave equation (v = fλ)
    derive_formula("v/v_P, (f*t_P) * (wavelength/l_P)", v, all_symbols,
                  "Wave speed relation")

    # Energy of electromagnetic wave
    derive_formula("E/E_P, (B/B_P)**2 * (A_P/A)", E, all_symbols,
                  "Energy stored in magnetic field")

    # ==========================================================================
    print(" # DEMONSTRATION OF UNIVERSALITY \n")
    # ==========================================================================

    # Even empirical relations follow this pattern
    derive_formula("R/R_P, rho * (L/l_P) / (A/A_P)", R, all_symbols,
                  "Electrical resistance of a conductor")

    # Quantum gravity energy scale
    derive_formula("E/E_P, (l_P/L)**2", E, all_symbols,
                 "Quantum gravity energy scale")



    # Gravitational wave strain amplitude
    # derive_formula("h/h_P, (f/F_P)**(2/3) * (M/m_P)**(5/3) * (l_P/r)**2", h, all_symbols,
                 # "Gravitational wave strain amplitude")


    # Planck-scale black hole evaporation rate
    derive_formula("P/P_P, (m_P/M)**2", P, all_symbols,
                  "Planck-scale black hole evaporation power")


    # Planck-scale vacuum energy density
    derive_formula("rho/rho_P, (l_P/L)**4", rho, all_symbols,
                  "Planck-scale vacuum energy density")

    # Planck-scale gravitational field strength
    derive_formula("E/E_P, (m/m_P) * (l_P/r)**2", E, all_symbols,
                  "Planck-scale gravitational field")

