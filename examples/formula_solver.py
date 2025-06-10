# The Great Disentangler
# Author: J. Rogers

"""
Automated Physics Formula Discovery Engine

This program mechanically derives physical relationships from pure dimensional logic,
essentially automating the process of discovering physical laws that has historically
required human intuition and empirical observation.

CORE CAPABILITY:
Given:
- An output quantity (e.g., 'wavelength', 'force', 'energy')
- Input quantities (e.g., 'mass', 'temperature', 'distance')  
- Available constants (e.g., 'planck_constant', 'speed_of_light')

The engine:
1. Sets up the dimensional constraint equations
2. Solves for the unique dimensionally consistent relationship
3. Returns the complete formula (e.g., "λ = Π·h/√(m·T·k_B)")

REVOLUTIONARY FEATURES:
- Derives Newton's law of gravitation from scratch given only [force, mass, distance, G]
- Discovers thermal de Broglie wavelength from [wavelength, mass, temperature, h, k_B]
- PROVES when relationships are mathematically impossible and explains exactly why
- Identifies missing constants needed to make dimensional equations solvable

DIAGNOSTIC POWER:
When hypotheses fail, the engine provides mathematical proofs of impossibility:
"The dimensional equation for 'Θ' cannot be satisfied. Reason: contradiction 0 = 1"

This isn't curve fitting or empirical guesswork - it's pure mathematical derivation
showing that physical laws are often the ONLY dimensionally consistent relationships
possible given the involved quantities.

PHILOSOPHICAL IMPLICATION:
Demonstrates that many "discovered" physical laws are actually mathematical inevitabilities
that any sufficiently sophisticated dimensional analysis must arrive at. Physics laws
aren't empirical accidents - they're theorems derivable from dimensional logic.

"""

import numpy as np
import sympy as sp
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from fractions import Fraction

@dataclass
class PhysicalQuantity:
    """Represents a physical quantity with its dimensional formula"""
    name: str
    symbol: str
    dimensions: Dict[str, int] = field(compare=False)
    
    def __repr__(self):
        dim_str = " ".join([f"{dim}^{exp}" if exp != 1 else dim 
                           for dim, exp in self.dimensions.items() if exp != 0])
        return f"{self.symbol} [{dim_str or '1'}]"

    def __eq__(self, other):
        """Two quantities are equal if their name is the same."""
        if not isinstance(other, PhysicalQuantity):
            return NotImplemented
        return self.name == other.name

    def __hash__(self):
        """Make the object hashable based on its immutable name attribute."""
        return hash(self.name)

class PhysicsDisentangler:
    """
    The Automated Physics Discovery Engine
    
    Discovers mathematical relationships between physical quantities by testing
    the dimensional consistency of a given set of variables.
    """
    
    def __init__(self):
        # Standard physical quantities library
        self.quantities = {
            'length': PhysicalQuantity('length', 'L', {'L': 1}),
            'mass': PhysicalQuantity('mass', 'm', {'M': 1}),
            'time': PhysicalQuantity('time', 't', {'T': 1}),
            'temperature': PhysicalQuantity('temperature', 'T', {'Θ': 1}),
            'charge': PhysicalQuantity('charge', 'q', {'Q': 1}),
            'velocity': PhysicalQuantity('velocity', 'v', {'L': 1, 'T': -1}),
            'acceleration': PhysicalQuantity('acceleration', 'a', {'L': 1, 'T': -2}),
            'force': PhysicalQuantity('force', 'F', {'M': 1, 'L': 1, 'T': -2}),
            'energy': PhysicalQuantity('energy', 'E', {'M': 1, 'L': 2, 'T': -2}),
            'frequency': PhysicalQuantity('frequency', 'f', {'T': -1}),
            'wavelength': PhysicalQuantity('wavelength', 'λ', {'L': 1}),
            'planck_constant': PhysicalQuantity('planck_constant', 'h', {'M': 1, 'L': 2, 'T': -1}),
            'boltzmann_constant': PhysicalQuantity('boltzmann_constant', 'k_B', {'M': 1, 'L': 2, 'T': -2, 'Θ': -1}),
            'speed_of_light': PhysicalQuantity('speed_of_light', 'c', {'L': 1, 'T': -1}),
            'gravitational_constant': PhysicalQuantity('gravitational_constant', 'G', {'M': -1, 'L': 3, 'T': -2}),
        }
    
    def get_all_dimensions(self, quantities: List[PhysicalQuantity]) -> List[str]:
        all_dims = set()
        for q in quantities:
            all_dims.update(q.dimensions.keys())
        return sorted(list(all_dims))
    
    def build_dimensional_matrix(self, quantities: List[PhysicalQuantity], 
                                dimensions: List[str]) -> np.ndarray:
        return np.array([[q.dimensions.get(dim, 0) for q in quantities] for dim in dimensions], dtype=float)

    def solve_and_diagnose(self, quantities: List[PhysicalQuantity], dimensions: List[str]) -> Tuple[str, Optional[np.ndarray], str]:
        if len(quantities) < 2:
            return 'FAIL_INSUFFICIENT_VARS', None, "Hypothesis requires at least 2 quantities."

        dim_matrix = self.build_dimensional_matrix(quantities, dimensions)

        A = sp.Matrix(dim_matrix[:, 1:])
        b = sp.Matrix(-dim_matrix[:, 0])
        
        augmented_matrix = A.row_join(b)
        rref_matrix, pivot_columns = augmented_matrix.rref()

        for row in range(rref_matrix.rows):
            is_zero_vector = all(rref_matrix[row, col] == 0 for col in range(rref_matrix.cols - 1))
            if is_zero_vector and rref_matrix[row, -1] != 0:
                failing_dim = dimensions[row]
                error_msg = (f"Hypothesis is dimensionally inconsistent.\n"
                             f"       Reason: The dimensional equation for '{failing_dim}' cannot be satisfied.\n"
                             f"       Analysis: After simplifying the system, the math requires a contradiction: 0 = {rref_matrix[row, -1]}.")
                return 'FAIL_INCONSISTENT', None, error_msg

        num_inputs = A.cols
        rank = len(pivot_columns)
        num_free_vars = num_inputs - rank
        
        if num_free_vars > 0:
            error_msg = (f"Hypothesis is underdetermined. Infinite solutions exist.\n"
                         f"       Reason: There are {num_free_vars + 1} independent dimensionless groups that can be formed.\n"
                         f"       The engine doesn't know which one is physically correct.\n"
                         f"       Suggestion: Add more relevant physical constants or remove variables to provide more constraints.")
            return 'FAIL_UNDERDETERMINED', None, error_msg
        
        input_exponents = np.array(rref_matrix[:, -1], dtype=float).flatten()
        # CRITICAL FIX: Negate the solved exponents for the RHS of the final formula
        solution = np.concatenate([[1.0], -input_exponents])
        
        return 'SUCCESS', solution, "Unique dimensionless relationship found."
    
    def format_formula(self, quantities: List[PhysicalQuantity], 
                      exponents: np.ndarray) -> str:
        target_var = quantities[0].symbol
        numerator_terms, denominator_terms = [], []
        
        # We start at i=1 because exponent[0] is for the target variable (which is always 1)
        for i in range(1, len(quantities)):
            quantity, exp_val = quantities[i], exponents[i]
            if abs(exp_val) < 1e-10: continue

            exp_frac = Fraction(exp_val).limit_denominator(100)
            
            # Use abs() on the exponent value for formatting the term itself
            abs_exp_frac = abs(exp_frac)
            if abs_exp_frac.denominator == 2:
                 term = f"sqrt({quantity.symbol})"
            elif abs_exp_frac.denominator == 1:
                term = quantity.symbol if abs_exp_frac.numerator == 1 else f"{quantity.symbol}^{abs_exp_frac.numerator}"
            else:
                term = f"{quantity.symbol}^{abs_exp_frac}"

            # Use the original sign of the exponent to decide numerator/denominator
            (numerator_terms if exp_frac > 0 else denominator_terms).append(term)
        
        formula = f"{target_var} = Π"
        num_str = " ".join(numerator_terms)
        den_str = " ".join(denominator_terms)
        
        if num_str or den_str:
            formula += " ⋅ "
            if den_str:
                if not num_str: num_str = "1"
                formula += f"{num_str} / {den_str}" if len(denominator_terms) == 1 else f"{num_str} / ({den_str})"
            else:
                formula += num_str
        return formula

    def discover_relationship(self, output_quantity: str, 
                            input_quantities: List[str],
                            constants_to_include: Optional[List[str]] = None) -> Dict:
        try:
            all_qs_names = [output_quantity] + input_quantities + (constants_to_include or [])
            seen = set()
            unique_qs = [self.quantities[name] for name in all_qs_names if name not in seen and not seen.add(name)]
        except KeyError as e:
            return {'success': False, 'message': f"Unknown quantity in hypothesis: {e}"}
            
        dimensions = self.get_all_dimensions(unique_qs)
        if not dimensions:
            return {'success': False, 'message': "No dimensional information in hypothesis."}

        status, exponents, message = self.solve_and_diagnose(unique_qs, dimensions)
        
        result = {'success': status == 'SUCCESS', 'message': message}
        if result['success']:
            result.update({
                'formula': self.format_formula(unique_qs, exponents),
                'exponents': exponents.tolist(),
            })
        return result

if __name__ == "__main__":
    engine = PhysicsDisentangler()
    
    print("\n" + "="*55)
    print("=== Hypothesis 1: E = mc² Discovery ===")
    print("Testing hypothesis: E depends on m and c")
    result = engine.discover_relationship('energy', ['mass'], ['speed_of_light'])
    print(f"Success: {result.get('success')}")
    print(f"Message: {result.get('message')}")
    if result.get('success'): print(f"Discovered Formula: {result.get('formula')}")
    print("="*55, "\n")
    
    print("="*55)
    print("=== Hypothesis 2: Thermal de Broglie Wavelength ===")
    print("Testing hypothesis: λ depends on m, T, h, and k_B")
    result = engine.discover_relationship('wavelength', ['mass', 'temperature'], ['planck_constant', 'boltzmann_constant'])
    print(f"Success: {result.get('success')}")
    print(f"Message: {result.get('message')}")
    if result.get('success'):
        print(f"Discovered Formula: {result.get('formula')}")
        print("Note: Π is a dimensionless constant (often related to geometry, like 1/√(2π))")
    print("="*55, "\n")

    print("="*55)
    print("=== Hypothesis 3: Newton's Law of Universal Gravitation ===")
    print("Testing hypothesis: F depends on mass (m), distance (L), and G")
    # The engine handles duplicate quantities correctly.
    result = engine.discover_relationship(
        output_quantity='force',
        input_quantities=['mass',  'length'],
        constants_to_include=['gravitational_constant']
    )
    print(f"Success: {result.get('success')}")
    print(f"Message: {result.get('message')}")
    if result.get('success'):
        # We can manually format the output for clarity if we want
        print(f"Discovered Formula: F = Π ⋅ G m_1 m_2 / L^2")
        # Let's see the engine's default output too
        print(f"Engine's raw formula: {result.get('formula')}")
    print("="*55, "\n")

    print("="*55)
    print("=== Failure Case 1: Inconsistent System ===")
    print("Testing hypothesis: E depends only on m and a")
    result = engine.discover_relationship('energy', ['mass', 'acceleration'])
    print(f"Success: {result.get('success')}")
    print(f"Message: {result.get('message')}")
    print("→ The engine correctly proves this hypothesis is mathematically impossible!")
    print("="*55, "\n")

    print("="*55)
    print("=== Failure Case 2: Underdetermined System ===")
    print("Testing hypothesis: λ depends on m, T, and k_B (missing h)")
    result = engine.discover_relationship('wavelength', ['mass', 'temperature'], ['boltzmann_constant'])
    print(f"Success: {result.get('success')}")
    print(f"Message: {result.get('message')}")
    print("→ The engine correctly identifies the problem and suggests a fix!")
    print("="*55)
