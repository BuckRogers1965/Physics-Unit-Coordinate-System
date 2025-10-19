"""
Physics API with Proper Separation of Concerns
===============================================

Layer 1: Business Logic (Natural Ratios - The Actual Physics)
Layer 2: Coordinate System (Jacobians - Measurement Geometry)  
Layer 3: Presentation (SI Units - Human Interface)

No magic numbers in business logic. All constants isolated to coordinate layer.
"""

import math
from typing import Dict, NamedTuple


# ============================================================================
# LAYER 1: BUSINESS LOGIC - The Actual Physics (Natural/Planck Scale)
# ============================================================================
# All physics happens here in pure dimensionless ratios
# No constants needed - this is reality's native coordinate system

class Physics:
    """Pure physics at natural scale. No magic numbers."""
    
    @staticmethod
    def energy_mass_equivalence(m_natural: float) -> float:
        """E ~ m in natural units. The actual physics is this simple."""
        return m_natural
    
    @staticmethod
    def energy_frequency_relation(f_natural: float) -> float:
        """E ~ f in natural units. Pure 1:1 ratio."""
        return f_natural
    
    @staticmethod
    def gravitational_force(m1_natural: float, m2_natural: float, 
                           r_natural: float) -> float:
        """F ~ m1*m2/r² in natural units. Newton's actual physics."""
        return m1_natural * m2_natural / (r_natural ** 2)
    
    @staticmethod
    def time_dilation_potential(m_natural: float, r_natural: float) -> float:
        """Dimensionless time field: tf ~ m/r. The substrate coupling."""
        return m_natural / r_natural
    
    @staticmethod
    def escape_velocity_beta(m_natural: float, r_natural: float) -> float:
        """β = sqrt(2*m/r). Dimensionless fraction of natural speed scale."""
        return math.sqrt(2 * m_natural / r_natural)
    
    @staticmethod
    def schwarzschild_condition(m_natural: float) -> float:
        """r = 2*m when β=1. Simple geometric limit in natural units."""
        return 2 * m_natural
    
    @staticmethod
    def hawking_temperature(m_natural: float) -> float:
        """T ~ 1/M in natural units. Inverse relationship."""
        return 1.0 / m_natural
    
    @staticmethod
    def planck_einstein_energy(f_natural: float) -> float:
        """E ~ f. Same as energy_frequency_relation, showing unity."""
        return f_natural
    
    @staticmethod
    def de_broglie_wavelength(m_natural: float, v_natural: float) -> float:
        """λ ~ 1/(m*v) in natural units."""
        return 1.0 / (m_natural * v_natural)


# ============================================================================
# LAYER 2: COORDINATE SYSTEM - Jacobians (Measurement Geometry)
# ============================================================================
# This is where "constants" live - they're coordinate transformation coefficients

class UnitSystem(NamedTuple):
    """Defines a measurement coordinate system via its Jacobians."""
    name: str
    # Base Jacobians (the "constants" - really coordinate scaling factors)
    c: float      # length/time scaling (m/s)
    h: float      # action scaling (J·s)
    G: float      # gravitational scaling (m³/(kg·s²))
    k_B: float    # temperature/energy scaling (J/K)
    
    # Derived Jacobians (composed from base Jacobians)
    @property
    def Hz_kg(self) -> float:
        """Mass/frequency Jacobian: h/c²"""
        return self.h / (self.c ** 2)
    
    @property
    def K_Hz(self) -> float:
        """Temperature/frequency Jacobian: k_B/h"""
        return self.k_B / self.h
    
    @property
    def G_natural(self) -> float:
        """G in time² units: G * Hz_kg / c³"""
        return self.G * self.Hz_kg / (self.c ** 3)
    
    # Natural scale references (where all Jacobians = 1)
    @property
    def t_planck(self) -> float:
        """Planck time: sqrt(G_natural)"""
        return math.sqrt(self.G_natural)
    
    @property
    def l_planck(self) -> float:
        """Planck length: c * t_P"""
        return self.c * self.t_planck
    
    @property
    def m_planck(self) -> float:
        """Planck mass: Hz_kg / t_P"""
        return self.Hz_kg / self.t_planck
    
    @property
    def E_planck(self) -> float:
        """Planck energy: m_P * c²"""
        return self.m_planck * (self.c ** 2)
    
    @property
    def T_planck(self) -> float:
        """Planck temperature: 1 / (t_P * K_Hz)"""
        return 1.0 / (self.t_planck * self.K_Hz)
    
    @property
    def F_planck(self) -> float:
        """Planck force: m_P * c / t_P"""
        return self.m_planck * self.c / self.t_planck


# Predefined coordinate systems
SI = UnitSystem(
    name="SI",
    c=299792458.0,           # m/s (exact, by definition since 2019)
    h=6.62607015e-34,        # J·s (exact, by definition since 2019)
    G=6.67430e-11,           # m³/(kg·s²) (measured)
    k_B=1.380649e-23         # J/K (exact, by definition since 2019)
)


# ============================================================================
# LAYER 3: PRESENTATION - Human-Readable Interface
# ============================================================================
# Converts between natural scale and measurement system for human use

class Quantity:
    """A physical quantity with value in both natural and SI coordinates."""
    
    def __init__(self, natural_value: float, dimension: str, 
                 unit_system: UnitSystem = SI):
        self.natural_value = natural_value
        self.dimension = dimension
        self.unit_system = unit_system
    
    @property
    def si_value(self) -> float:
        """Convert natural value to SI via appropriate Jacobian."""
        if self.dimension == "mass":
            return self.natural_value * self.unit_system.m_planck
        elif self.dimension == "length":
            return self.natural_value * self.unit_system.l_planck
        elif self.dimension == "time":
            return self.natural_value * self.unit_system.t_planck
        elif self.dimension == "energy":
            return self.natural_value * self.unit_system.E_planck
        elif self.dimension == "temperature":
            return self.natural_value * self.unit_system.T_planck
        elif self.dimension == "force":
            return self.natural_value * self.unit_system.F_planck
        elif self.dimension == "velocity":
            return self.natural_value * self.unit_system.c
        elif self.dimension == "dimensionless":
            return self.natural_value
        else:
            raise ValueError(f"Unknown dimension: {self.dimension}")
    
    @property
    def si_unit(self) -> str:
        """Return SI unit string."""
        units = {
            "mass": "kg",
            "length": "m",
            "time": "s",
            "energy": "J",
            "temperature": "K",
            "force": "N",
            "velocity": "m/s",
            "dimensionless": ""
        }
        return units.get(self.dimension, "?")
    
    def __str__(self) -> str:
        if self.dimension == "dimensionless":
            return f"{self.si_value:.6e} (dimensionless)"
        return f"{self.si_value:.6e} {self.si_unit}"
    
    @classmethod
    def from_si(cls, si_value: float, dimension: str, 
                unit_system: UnitSystem = SI) -> 'Quantity':
        """Create quantity from SI value (converts to natural)."""
        if dimension == "mass":
            natural = si_value / unit_system.m_planck
        elif dimension == "length":
            natural = si_value / unit_system.l_planck
        elif dimension == "time":
            natural = si_value / unit_system.t_planck
        elif dimension == "energy":
            natural = si_value / unit_system.E_planck
        elif dimension == "temperature":
            natural = si_value / unit_system.T_planck
        elif dimension == "velocity":
            natural = si_value / unit_system.c
        elif dimension == "dimensionless":
            natural = si_value
        else:
            raise ValueError(f"Unknown dimension: {dimension}")
        
        return cls(natural, dimension, unit_system)


# ============================================================================
# PUBLIC API - Clean interface hiding architectural complexity
# ============================================================================

class PhysicsAPI:
    """
    Public API for physics calculations.
    Uses proper architectural separation:
    - Business logic in natural coordinates
    - Presentation layer handles unit conversion
    """
    
    def __init__(self, unit_system: UnitSystem = SI):
        self.unit_system = unit_system
        self.physics = Physics()
    
    def mass_energy_equivalence(self, mass: Quantity) -> Quantity:
        """E = mc² (in SI) or E ~ m (in natural units)."""
        E_natural = self.physics.energy_mass_equivalence(mass.natural_value)
        return Quantity(E_natural, "energy", self.unit_system)
    
    def gravitational_force(self, m1: Quantity, m2: Quantity, 
                          r: Quantity) -> Quantity:
        """Newton's law: F = GMm/r² (SI) or F ~ mm/r² (natural)."""
        F_natural = self.physics.gravitational_force(
            m1.natural_value, m2.natural_value, r.natural_value
        )
        return Quantity(F_natural, "force", self.unit_system)
    
    def time_dilation(self, mass: Quantity, radius: Quantity) -> Quantity:
        """Dimensionless time field: Δt/t = (G/c²)(m/r) = (m/r)_natural"""
        tf_natural = self.physics.time_dilation_potential(
            mass.natural_value, radius.natural_value
        )
        return Quantity(tf_natural, "dimensionless", self.unit_system)
    
    def escape_velocity(self, mass: Quantity, radius: Quantity) -> Quantity:
        """v_e = β*c where β = sqrt(2m/r) in natural units."""
        beta = self.physics.escape_velocity_beta(
            mass.natural_value, radius.natural_value
        )
        return Quantity(beta, "velocity", self.unit_system)
    
    def schwarzschild_radius(self, mass: Quantity) -> Quantity:
        """r_s = 2GM/c² (SI) or r_s = 2m (natural)."""
        r_natural = self.physics.schwarzschild_condition(mass.natural_value)
        return Quantity(r_natural, "length", self.unit_system)
    
    def hawking_temperature(self, mass: Quantity) -> Quantity:
        """T ~ 1/M in natural units."""
        T_natural = self.physics.hawking_temperature(mass.natural_value)
        return Quantity(T_natural, "temperature", self.unit_system)
    
    def show_unit_system_info(self):
        """Display the Jacobian structure of current coordinate system."""
        print(f"\n{'='*70}")
        print(f"COORDINATE SYSTEM: {self.unit_system.name}")
        print(f"{'='*70}")
        print("\nBase Jacobians (the 'constants'):")
        print(f"  c   = {self.unit_system.c:.10e} m/s")
        print(f"  h   = {self.unit_system.h:.10e} J·s")
        print(f"  G   = {self.unit_system.G:.10e} m³/(kg·s²)")
        print(f"  k_B = {self.unit_system.k_B:.10e} J/K")
        
        print("\nDerived Jacobians:")
        print(f"  Hz_kg = h/c²  = {self.unit_system.Hz_kg:.10e} kg/Hz")
        print(f"  K_Hz  = k_B/h = {self.unit_system.K_Hz:.10e} Hz/K")
        
        print("\nNatural Scale References (Planck units):")
        print(f"  t_P = {self.unit_system.t_planck:.10e} s")
        print(f"  l_P = {self.unit_system.l_planck:.10e} m")
        print(f"  m_P = {self.unit_system.m_planck:.10e} kg")
        print(f"  E_P = {self.unit_system.E_planck:.10e} J")
        print(f"  T_P = {self.unit_system.T_planck:.10e} K")
        print(f"  F_P = {self.unit_system.F_planck:.10e} N")
        print(f"{'='*70}\n")


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Initialize API
    api = PhysicsAPI(SI)
    
    # Show coordinate system structure
    api.show_unit_system_info()
    
    print("EXAMPLE CALCULATIONS")
    print("="*70)
    
    # Example 1: Earth's escape velocity
    print("\n1. Earth's Escape Velocity:")
    print("-" * 70)
    M_earth = Quantity.from_si(5.972e24, "mass")  # kg
    R_earth = Quantity.from_si(6.371e6, "length")  # m
    
    print(f"   Mass (SI):   {M_earth}")
    print(f"   Radius (SI): {R_earth}")
    print(f"   Mass (natural):   {M_earth.natural_value:.6e} m_P")
    print(f"   Radius (natural): {R_earth.natural_value:.6e} l_P")
    
    v_escape = api.escape_velocity(M_earth, R_earth)
    print(f"   → Escape velocity: {v_escape}")
    print(f"   → β (natural):     {v_escape.natural_value:.6e}")
    
    # Example 2: Time dilation at Earth's surface
    print("\n2. Gravitational Time Dilation at Earth's Surface:")
    print("-" * 70)
    time_dilation = api.time_dilation(M_earth, R_earth)
    print(f"   → Δt/t = {time_dilation}")
    
    # Example 3: Mass-energy equivalence
    print("\n3. Mass-Energy Equivalence (1 kg):")
    print("-" * 70)
    one_kg = Quantity.from_si(1.0, "mass")
    energy = api.mass_energy_equivalence(one_kg)
    print(f"   Mass:   {one_kg}")
    print(f"   → Energy: {energy}")
    
    # Example 4: Schwarzschild radius of the Sun
    print("\n4. Schwarzschild Radius of the Sun:")
    print("-" * 70)
    M_sun = Quantity.from_si(1.989e30, "mass")
    r_s = api.schwarzschild_radius(M_sun)
    print(f"   Mass: {M_sun}")
    print(f"   → r_s:  {r_s}")
    
    # Example 5: Hawking temperature of a solar mass black hole
    print("\n5. Hawking Temperature (Solar Mass Black Hole):")
    print("-" * 70)
    T_hawking = api.hawking_temperature(M_sun)
    print(f"   Mass: {M_sun}")
    print(f"   → T_Hawking: {T_hawking}")
    
    # Example 6: Gravitational force between Earth and Moon
    print("\n6. Earth-Moon Gravitational Force:")
    print("-" * 70)
    M_moon = Quantity.from_si(7.342e22, "mass")
    distance = Quantity.from_si(3.844e8, "length")
    force = api.gravitational_force(M_earth, M_moon, distance)
    print(f"   Earth mass: {M_earth}")
    print(f"   Moon mass:  {M_moon}")
    print(f"   Distance:   {distance}")
    print(f"   → Force: {force}")
    
    print("\n" + "="*70)
    print("NOTE: All physics calculations happen in natural coordinates.")
    print("      Constants only appear in the coordinate transformation layer.")
    print("      No magic numbers in business logic!")
    print("="*70)
