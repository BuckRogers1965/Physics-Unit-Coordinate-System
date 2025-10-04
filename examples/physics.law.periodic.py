import sympy
import itertools
from collections import defaultdict

# Copy your exact definitions
h, G, c, kB, epsilon_0, mu_0, e, m_e, alpha = sympy.symbols('h G c k_B epsilon_0 mu_0 e m_e alpha', positive=True, real=True)
T, M, M1, M2, r, F, wavelength = sympy.symbols('T M M1 M2 r F lambda', real=True)
E, f, r_s, P, m, a = sympy.symbols('E f r_s P m a', real=True)
v, p, I, R, V, Q, B, omega, x, k, n = sympy.symbols('v p I R V Q B omega x k n', real=True)
sigma, rho, A, L, C, phi, U, S = sympy.symbols('sigma rho A L C phi U S', real=True)

# Define the Complete Set of Planck Units (copied from your code)
t_P = sympy.sqrt(h * G / c**5)
l_P = sympy.sqrt(h * G / c**3)
m_P = sympy.sqrt(h * c / G)
T_P = sympy.sqrt(h * c**5 / G) / kB
E_P = sympy.sqrt(h * c**5 / G)
F_P = c**4 / G
P_P = c**7 / (h * G**2)
a_P = l_P / t_P**2
v_P = c
p_P = sympy.sqrt(h * c**3 / G)
q_P = sympy.sqrt(4 * sympy.pi * epsilon_0 * h * c)
V_P = sympy.sqrt(h * c**5 / G) / sympy.sqrt(4 * sympy.pi * epsilon_0 * h * c)
I_P = sympy.sqrt(4 * sympy.pi * epsilon_0 * h * c**7 / G)
R_P = sympy.sqrt(h * G / (4 * sympy.pi * epsilon_0 * c**3))
B_P = sympy.sqrt(h * c / G) / (4 * sympy.pi * epsilon_0 * h * c)
S_P = kB
U_P = sympy.sqrt(h * c**5 / G)
rho_P = c**5 / (h * G**2)
sigma_P = c**4 / (h * G)
A_P = h * G / c**3
Vol_P = (h * G / c**3)**(3/2)
omega_P = (c**5 / (h * G))**(1/2)
k_P = c**3 / (h * G)**(1/2)

planck_units = {
    't_P': t_P, 'l_P': l_P, 'm_P': m_P, 'T_P': T_P,
    'E_P': E_P, 'F_P': F_P, 'P_P': P_P, 'a_P': a_P, 'v_P': v_P, 'p_P': p_P,
    'q_P': q_P, 'V_P': V_P, 'I_P': I_P, 'R_P': R_P, 'B_P': B_P,
    'S_P': S_P, 'U_P': U_P, 'rho_P': rho_P, 'sigma_P': sigma_P,
    'A_P': A_P, 'Vol_P': Vol_P, 'omega_P': omega_P, 'k_P': k_P
}

# Your exact derive_formula function
def derive_formula(postulate_string, target_variable, substitutions, description=""):
    """
    A general-purpose engine to derive physical formulas from a dimensionless postulate.
    """
    
    # 1. Parse the string and create a SymPy Equality object
    try:
        postulate_eq = sympy.sympify(f"Eq({postulate_string})", locals=substitutions)
    except Exception as e:
        return None, f"Error parsing: {e}"
        
    # 2. Solve for the target variable symbolically
    try:
        solution_expr = sympy.solve(postulate_eq, target_variable)[0]
    except (IndexError, TypeError):
        return None, "Could not solve for target variable"
        
    # 3. Substitute the full Planck unit definitions
    final_expr = solution_expr.subs(substitutions)
    
    # 4. Simplify the final expression
    simplified_expr = sympy.simplify(final_expr)
    final_formula = sympy.Eq(target_variable, simplified_expr)
    
    return final_formula, "Success"

# Define your exact substitution dictionary
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

# Physical quantities with their Planck unit symbols
physical_quantities = {
    'T': {'planck_symbol': 'T_P', 'name': 'Temperature', 'symbol': 'T'},
    'M': {'planck_symbol': 'm_P', 'name': 'Mass', 'symbol': 'M'},
    'r': {'planck_symbol': 'l_P', 'name': 'Distance', 'symbol': 'r'},
    'F': {'planck_symbol': 'F_P', 'name': 'Force', 'symbol': 'F'},
    'E': {'planck_symbol': 'E_P', 'name': 'Energy', 'symbol': 'E'},
    'f': {'planck_symbol': 'omega_P', 'name': 'Frequency', 'symbol': 'f'},
    'P': {'planck_symbol': 'P_P', 'name': 'Pressure', 'symbol': 'P'},
    'v': {'planck_symbol': 'v_P', 'name': 'Velocity', 'symbol': 'v'},
    'p': {'planck_symbol': 'p_P', 'name': 'Momentum', 'symbol': 'p'},
    'rho': {'planck_symbol': 'rho_P', 'name': 'Density', 'symbol': 'rho'},
    'A': {'planck_symbol': 'A_P', 'name': 'Area', 'symbol': 'A'},
    'L': {'planck_symbol': 'l_P', 'name': 'Length', 'symbol': 'L'},
    'wavelength': {'planck_symbol': 'l_P', 'name': 'Wavelength', 'symbol': 'lambda'},
    #'V': {'planck_symbol': 'V_P', 'name': 'Voltage', 'symbol': 'V'},
    #'I': {'planck_symbol': 'I_P', 'name': 'Current', 'symbol': 'I'},
    #'R': {'planck_symbol': 'R_P', 'name': 'Resistance', 'symbol': 'R'},
    #'B': {'planck_symbol': 'B_P', 'name': 'Magnetic Field', 'symbol': 'B'},
    #'Q': {'planck_symbol': 'q_P', 'name': 'Charge', 'symbol': 'Q'},
    'm': {'planck_symbol': 'm_P', 'name': 'Mass', 'symbol': 'm'},
    'a': {'planck_symbol': 'a_P', 'name': 'Acceleration', 'symbol': 'a'},
}

def generate_all_laws():
    """Generate all possible physical laws using dimensionless ratios"""
    laws = []
    quantities = list(physical_quantities.keys())
    
    # Generate all pairs of quantities
    for q1 in quantities:
        for q2 in quantities:
            if q1 != q2:
                q1_planck = physical_quantities[q1]['planck_symbol']
                q2_planck = physical_quantities[q2]['planck_symbol']
                
                # Create the target variable symbol
                target_var = all_symbols[q1]
                
                # Different types of relationships - FIXED HTML ENTITIES
                relationships = [
                    # Direct proportionality
                    (f"{q1}/{q1_planck}, {q2}/{q2_planck}", f"{q1} ∝ {q2}", "direct"),
                    
                    # Inverse proportionality
                    (f"{q1}/{q1_planck}, {q2_planck}/{q2}", f"{q1} ∝ 1/{q2}", "inverse"),
                    
                    # Square proportionality
                    (f"{q1}/{q1_planck}, ({q2}/{q2_planck})**2", f"{q1} ∝ {q2}<sup>2</sup>", "square"),
                    
                    # Inverse square
                    (f"{q1}/{q1_planck}, ({q2_planck}/{q2})**2", f"{q1} ∝ 1/{q2}<sup>2</sup>", "inverse_square"),
                    
                    # Square root
                    (f"{q1}/{q1_planck}, sqrt({q2}/{q2_planck})", f"{q1} ∝ √{q2}", "sqrt"),
                    
                    # Inverse square root
                    (f"{q1}/{q1_planck}, sqrt({q2_planck}/{q2})", f"{q1} ∝ 1/√{q2}", "inverse_sqrt"),
                    
                    # Cube
                    (f"{q1}/{q1_planck}, ({q2}/{q2_planck})**3", f"{q1} ∝ {q2}<sup>3</sup>", "cube"),

                    # Fourth power - FIXED
                    (f"{q1}/{q1_planck}, ({q2}/{q2_planck})**4", f"{q1} ∝ {q2}<sup>4</sup>", "fourth"),
                ]
                
                for postulate, formula_text, relation_type in relationships:
                    # Get the display symbols for the formula text
                    q1_symbol = physical_quantities[q1]['symbol']
                    q2_symbol = physical_quantities[q2]['symbol']
                    
                    # Replace the variable names with display symbols in formula_text
                    display_formula = formula_text.replace(q1, q1_symbol).replace(q2, q2_symbol)
                    
                    result, status = derive_formula(postulate, target_var, all_symbols)
                    
                    # Fixed: Check if result is not None instead of checking truthiness
                    if result is not None:
                        laws.append({
                            'dependent': q1,
                            'independent': q2,
                            'relation': relation_type,
                            'formula_text': display_formula,
                            'postulate': postulate,
                            'result': str(result.rhs),
                            'status': status
                        })
    
    return laws

def generate_html_table():
    """Generate HTML periodic table of physical laws"""
    laws = generate_all_laws()
    
    # Group laws by dependent variable
    laws_by_dependent = defaultdict(list)
    for law in laws:
        laws_by_dependent[law['dependent']].append(law)
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Periodic Table of Physical Laws</title>
        <meta charset="UTF-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background: #f0f0f0; }
            .container { max-width: 1400px; margin: 0 auto; }
            h1 { text-align: center; color: #333; margin-bottom: 30px; }
            .quantity-section { margin-bottom: 40px; }
            .quantity-header { 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white; padding: 15px; border-radius: 10px;
                font-size: 24px; font-weight: bold; margin-bottom: 20px;
                text-align: center;
            }
            .laws-grid { 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 15px;
            }
            .law-card {
                background: white;
                border: 2px solid #ddd;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .law-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 15px rgba(0,0,0,0.2);
            }
            .law-title { font-size: 18px; font-weight: bold; color: #333; margin-bottom: 10px; }
            .law-formula { font-size: 16px; color: #666; margin-bottom: 8px; }
            .law-result { font-size: 14px; color: #000; font-family: monospace; background: #f8f8f8; padding: 10px; border-radius: 5px; }
            .law-postulate { font-size: 12px; color: #888; margin-top: 5px; }
            .direct { border-left: 5px solid #4CAF50; }
            .inverse { border-left: 5px solid #FF5722; }
            .square { border-left: 5px solid #2196F3; }
            .inverse_square { border-left: 5px solid #FF9800; }
            .sqrt { border-left: 5px solid #9C27B0; }
            .inverse_sqrt { border-left: 5px solid #607D8B; }
            .fourth { border-left: 5px solid #E91E63; }
            .cube { border-left: 5px solid #795548; }
            .legend {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 20px;
                margin-bottom: 30px;
                padding: 20px;
                background: white;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .legend-item {
                display: flex;
                align-items: center;
                gap: 10px;
            }
            .legend-color {
                width: 20px;
                height: 20px;
                border-radius: 3px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Periodic Table of Physical Laws</h1>
            <p style="text-align: center; font-size: 18px; color: #666; margin-bottom: 30px;">
                All possible proportionality relationships between physical quantities, derived through dimensional analysis with Planck units
            </p>
            
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background: #4CAF50;"></div>
                    <span>Direct (∝)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #FF5722;"></div>
                    <span>Inverse (∝ 1/x)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #2196F3;"></div>
                    <span>Square (∝ x²)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #FF9800;"></div>
                    <span>Inverse Square (∝ 1/x²)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #9C27B0;"></div>
                    <span>Square Root (∝ √x)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #607D8B;"></div>
                    <span>Inverse Square Root (∝ 1/√x)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #E91E63;"></div>
                    <span>Fourth Power (∝ x⁴)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #795548;"></div>
                    <span>Cube (∝ x³)</span>
                </div>
            </div>
    """
    
    # Generate sections for each dependent variable
    for dependent_var in sorted(physical_quantities.keys()):
        if dependent_var in laws_by_dependent:
            var_info = physical_quantities[dependent_var]
            html += f"""
            <div class="quantity-section">
                <div class="quantity-header">
                    {var_info['symbol']} - {var_info['name']}
                </div>
                <div class="laws-grid">
            """
            
            # Sort laws by independent variable for consistency
            sorted_laws = sorted(laws_by_dependent[dependent_var], 
                               key=lambda x: (x['independent'], x['relation']))
            
            for law in sorted_laws:
                ind_var_info = physical_quantities[law['independent']]
                
                html += f"""
                <div class="law-card {law['relation']}">
                    <div class="law-title">
                        {var_info['symbol']} vs {ind_var_info['symbol']}
                    </div>
                    <div class="law-formula">
                        {law['formula_text']}
                    </div>
                    <div class="law-result">
                        {var_info['symbol']} = {law['result']}
                    </div>
                    <div class="law-postulate">
                        Postulate: {law['postulate']}
                    </div>
                </div>
                """
            
            html += """
                </div>
            </div>
            """
    
    html += """
        </div>
    </body>
    </html>
    """
    
    return html

def main():
    """Main function to generate and save the HTML table"""
    print("Generating periodic table of physical laws...")
    laws = generate_all_laws()
    print(f"Generated {len(laws)} laws")
    
    html_content = generate_html_table()
    
    # Save to file
    with open('physics_periodic_table.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("HTML file 'physics_periodic_table.html' generated successfully!")

if __name__ == "__main__":
    main()
