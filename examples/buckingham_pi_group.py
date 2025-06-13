import sympy

# -----------------------------------------------------------------------------
# Step 0: The Knowledge Base (The "config.ini" of Physics)
# -----------------------------------------------------------------------------

# Define base SI constants as positive real symbols for simplification
h, G, c, kB = sympy.symbols('h G c k_B', positive=True, real=True)

# Define common physical quantities as real symbols
T, M, M1, M2, r, F, wavelength = sympy.symbols('T M M1 M2 r F lambda', real=True)

E, f, r_s = sympy.symbols('E f r_s', real=True)
P = sympy.symbols('P', real=True)

# Define the Planck Units (non-reduced, using h) in terms of the constants
# These are the symbolic "basis vectors"
T_P = sympy.sqrt(h * c**5 / G) / kB
m_P = sympy.sqrt(h * c / G)
l_P = sympy.sqrt(h * G / c**3)
F_P = (c**4 / G) # Planck Force
E_P = sympy.sqrt(h * c**5 / G) 
t_P = sympy.sqrt(h * G / c**5)
P_P = c**7 / (h * G**2)

# Store Planck units in a dictionary for easy substitution by the engine
planck_units = {
    'T_P': T_P,
    'm_P': m_P,
    'l_P': l_P,
    'F_P': F_P,
    'E_P': E_P,
    'm_P': m_P,
    't_P': t_P
}

# -----------------------------------------------------------------------------
# The Automated Formula Forge Engine
# -----------------------------------------------------------------------------

def derive_formula(postulate_string, target_variable, substitutions):
    """
    A general-purpose engine to derive physical formulas from a dimensionless postulate.
    
    Args:
        postulate_string (str): A string representing the core dimensionless law.
        target_variable (sympy.Symbol): The variable to solve for.
        substitutions (dict): A dictionary mapping symbols in the string to their
                              SymPy objects (e.g., {'T_P': T_P}).
    
    Returns:
        sympy.Eq: The final derived formula for the target variable.
    """
    
    print(f"--- Deriving formula for: {target_variable} ---")
    
    # 1. Parse the string and create a SymPy Equality object
    # This turns the human-readable postulate into a symbolic equation
    try:
        postulate_eq = sympy.sympify(f"Eq({postulate_string})", locals=substitutions)
    except Exception as e:
        print(f"Error parsing the postulate string: {e}")
        return None
        
    print(f"\n1. Postulate: {postulate_string}")
    print(f"   Symbolic Form: {postulate_eq}")

    # 2. Solve for the target variable symbolically
    try:
        # We use solve() which returns a list of solutions
        solution_expr = sympy.solve(postulate_eq, target_variable)[0]
    except IndexError:
        print("   Could not solve for the target variable. Check the formula.")
        return None
        
    print(f"\n2. Solved for {target_variable}: Eq({target_variable}, {solution_expr})")

    # 3. Substitute the full Planck unit definitions
    # This is the "algebraic crank" that reveals the SI constant structure
    final_expr = solution_expr.subs(substitutions)
    print(f"\n3. Substituted Planck definitions...")
    
    # 4. Simplify the final expression
    simplified_expr = sympy.simplify(final_expr)
    final_formula = sympy.Eq(target_variable, simplified_expr)
    
    print(f"\n4. Simplified Result:")
    print(f"   >>> {final_formula}\n")
    
    return final_formula

# -----------------------------------------------------------------------------
# Main Execution: Testing the Engine on Three Different Problems
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    
    # Define a substitution dictionary that includes all our symbols
    # This allows the sympify function to correctly parse the strings
    all_symbols = {
        'T': T, 'M': M, 'M1': M1, 'M2': M2, 'r': r, 'F': F, 'E':E, 'wavelength': wavelength,
        'T_P': T_P, 'm_P': m_P, 'l_P': l_P, 'F_P': F_P, 'E_P': E_P, 'm_P': m_P, 'r_s': r_s, 't_P': t_P,
        'P': P, 'P_P': P_P 
    }

    print()
    print(" These are all calculated by dimensional analysis of Π groups,")
    print("     so this does not account for geometric ratios.")
    print()

    # --- Test Case 1: Hawking Temperature ---
    # Postulate: T/T_P = m_P/M
    postulate_hawking = "T/T_P, m_P/M"
    derive_formula(postulate_hawking, T, all_symbols)
    
    # --- Test Case 2: Newton's Law of Gravitation ---
    # Postulate: F/F_P = (M1*M2/m_P**2) * (l_P**2/r**2)
    postulate_gravity = "F/F_P, ((M1*M2/m_P**2) * (l_P**2/r**2))"
    derive_formula(postulate_gravity, F, all_symbols)

    # --- Test Case 3: Thermal de Broglie Wavelength ---
    # Postulate: wavelength/l_P = 1 / sqrt(M*T / (m_P*T_P))
    # Note: We use M for mass and T for temperature here.
    postulate_debroglie = "wavelength/l_P, 1/sqrt(M*T / (m_P*T_P))"
    derive_formula(postulate_debroglie, wavelength, all_symbols)


    # --- Test Case 4: Mass-Energy Equivalence (E=mc²) ---
    # Conceptual Postulate: The dimensionless energy ratio is equal to the dimensionless mass ratio.
    # Formal Postulate: E/E_P = M/m_P
    postulate_emc2 = "E/E_P, M/m_P"
    derive_formula(postulate_emc2, E, all_symbols)
    
    # --- Test Case 5: Planck-Einstein Relation (E=hf) ---
    # Conceptual Postulate: The dimensionless energy ratio is equal to the dimensionless frequency ratio.
    # Note: Frequency ratio is f / f_P where f_P = 1/t_P. So, f_ratio = f * t_P
    # Formal Postulate: E/E_P = f*t_P
    postulate_ehf = "E/E_P, f*t_P"
    derive_formula(postulate_ehf, E, all_symbols)

    # --- Test Case 6: Schwarzschild Radius (r_s = 2GM/c²) ---
    # Conceptual Postulate: The critical radius is where the escape velocity ratio is 1.
    # From our previous work, we know this leads to the dimensionless relation: r_s/l_P = 2 * (M/m_P).
    # (We omit the 2 for simplicity as it's a geometric factor, focusing on the dimensional part)
    # Formal Postulate: r_s/l_P = M/m_P
    postulate_schwarzschild = "r_s/l_P, M/m_P"
    derive_formula(postulate_schwarzschild, r_s, all_symbols)


    # --- Test Case 7: Radiation Pressure (Stefan-Boltzmann Law) ---
    # Conceptual Postulate: Pressure is proportional to Temperature to the fourth power.
    # Formal Postulate: P/P_P = (T/T_P)**4
    postulate_pressure = "P/P_P, (T/T_P)**4"
    derive_formula(postulate_pressure, P, all_symbols)
