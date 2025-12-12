"""
Physics API with Proper Separation of Concerns - Final Corrected Model v4
=========================================================================

Final, Final Correction: The Particle/QuantumObject classes have been
completely purged of any knowledge of unit systems or the presentation
layer. They are now pure data objects representing the physical entity's
fundamental, dimensionless state.

The PhysicsAPI is now the sole "Presenter," responsible for taking these
pure objects and projecting their properties into human-readable SI units.
This is the correct, strict separation of concerns.
"""

import math
from typing import Dict, NamedTuple

# ============================================================================
# LAYER 2: COORDINATE SYSTEM - Jacobians, Particle Zoo, & Composite Bodies
# ============================================================================

class UnitSystem(NamedTuple):
    name: str; c: float; h: float; G: float; k_B: float
    @property
    def m_planck(self) -> float: return math.sqrt(self.h * self.c / self.G)
    @property
    def E_planck(self) -> float: return self.m_planck * self.c ** 2
    @property
    def p_planck(self) -> float: return self.m_planck * self.c
    @property
    def l_planck(self) -> float: return self.h / self.p_planck
    @property
    def F_planck(self) -> float: return self.E_planck / self.l_planck

SI = UnitSystem("SI", 299792458.0, 6.62607015e-34, 6.67430e-11, 1.380649e-23)

class ParticleData(NamedTuple):
    rest_mass_natural: float
    charge_state: int

PARTICLE_ZOO: Dict[str, ParticleData] = {
    "electron": ParticleData(9.1093837e-31 / SI.m_planck, -1),
    "proton":   ParticleData(1.6726219e-27 / SI.m_planck, +1),
    "neutron":  ParticleData(1.6749274e-27 / SI.m_planck,  0),
}

COMPOSITE_BODIES: Dict[str, ParticleData] = {
    "earth": ParticleData(5.972e24 / SI.m_planck, 0),
    "sun":   ParticleData(1.989e30 / SI.m_planck, 0)
}

# ============================================================================
# LAYER 1: BUSINESS LOGIC - The Actual Physics
# ============================================================================
class Physics:
    @staticmethod
    def relativistic_energy(rest_mass_natural: float, momentum_natural: float) -> float:
        return math.sqrt(rest_mass_natural**2 + momentum_natural**2)
    @staticmethod
    def velocity_beta(energy_natural: float, momentum_natural: float) -> float:
        if energy_natural == 0: return 0.0
        return momentum_natural / energy_natural
    @staticmethod
    def gravitational_force(m1_nat: float, m2_nat: float, r_nat: float) -> float:
        return m1_nat * m2_nat / (r_nat ** 2)
    @staticmethod
    def coulomb_force(q1: int, q2: int, r_nat: float, alpha: float) -> float:
        return alpha * (q1 * q2) / (r_nat ** 2)

# ============================================================================
# LAYER 3: PRESENTATION (PART 1) - The Pure Data Objects
# ============================================================================

class QuantumObject:
    """
    A pure data object. It knows its fundamental, dimensionless state.
    It has NO KNOWLEDGE of SI units or any measurement system.
    """
    def __init__(self, momentum_natural: float):
        self.momentum_natural = momentum_natural

    @property
    def charge_state(self) -> int: raise NotImplementedError
    def total_energy_natural(self) -> float: raise NotImplementedError

class Photon(QuantumObject):
    """The base case. It IS its momentum."""
    @property
    def charge_state(self) -> int: return 0
    def total_energy_natural(self) -> float:
        return self.momentum_natural
    def __repr__(self) -> str: return f"<Photon p_nat={self.momentum_natural:.2e}>"

class MassiveObject(QuantumObject):
    """An extension that adds an intrinsic identity (rest mass)."""
    def __init__(self, identity_key: str, momentum_natural: float, data_source: Dict):
        super().__init__(momentum_natural)
        self._key = identity_key
        self._data_source = data_source

    @property
    def name(self) -> str: return self._key
    @property
    def charge_state(self) -> int: return self._data_source[self._key].charge_state
    @property
    def rest_mass_natural(self) -> float: return self._data_source[self._key].rest_mass_natural
    
    def total_energy_natural(self) -> float:
        return Physics.relativistic_energy(self.rest_mass_natural, self.momentum_natural)
    
    def __repr__(self) -> str:
        obj_type = "Particle" if self._data_source is PARTICLE_ZOO else "Body"
        return (f"<{obj_type} name='{self.name}' "
                f"p_nat={self.momentum_natural:.2e} "
                f"σ={self.rest_mass_natural:.2e}>")

# ============================================================================
# LAYER 3: PRESENTATION (PART 2) - The Presenter & Human-Readable Format
# ============================================================================

class Quantity:
    """A simple data structure for presenting a final result to a human."""
    def __init__(self, si_value: float, unit: str):
        self.si_value = si_value
        self.unit = unit
    def __str__(self) -> str: return f"{self.si_value:.6e} {self.unit}"

class PhysicsAPI:
    """
    The Presenter. This is the ONLY class that knows about both the pure
    QuantumObjects and the UnitSystem. It is responsible for all conversions.
    """
    def __init__(self, unit_system: UnitSystem = SI, particle_zoo: Dict = PARTICLE_ZOO, composite_bodies: Dict = COMPOSITE_BODIES):
        self.unit_system = unit_system
        self.particle_zoo = particle_zoo
        self.composite_bodies = composite_bodies
        self.physics = Physics()
        self.alpha = 1 / 137.036

    # --- Factory to create pure data objects ---
    def create_object(self, name: str, momentum_si: float = 0.0) -> QuantumObject:
        momentum_natural = momentum_si / self.unit_system.p_planck
        if name.lower() == "photon":
            return Photon(momentum_natural)
        elif name in self.particle_zoo:
            return MassiveObject(name, momentum_natural, self.particle_zoo)
        elif name in self.composite_bodies:
            return MassiveObject(name, momentum_natural, self.composite_bodies)
        else:
            raise ValueError(f"Object '{name}' not found.")

    # --- Presentation Methods: Take a pure object, return a formatted Quantity ---
    def get_total_energy(self, obj: QuantumObject) -> Quantity:
        e_nat = obj.total_energy_natural()
        return Quantity(e_nat * self.unit_system.E_planck, "J")

    def get_momentum(self, obj: QuantumObject) -> Quantity:
        p_si = obj.momentum_natural * self.unit_system.p_planck
        return Quantity(p_si, "kg·m/s")

    def get_velocity(self, obj: QuantumObject) -> Quantity:
        e_nat = obj.total_energy_natural()
        p_nat = obj.momentum_natural
        beta = self.physics.velocity_beta(e_nat, p_nat)
        return Quantity(beta * self.unit_system.c, "m/s")
    
    def get_rest_mass(self, obj: MassiveObject) -> Quantity:
        if not isinstance(obj, MassiveObject):
            raise TypeError("Only MassiveObjects have the property of rest mass.")
        m_si = obj.rest_mass_natural * self.unit_system.m_planck
        return Quantity(m_si, "kg")

    # --- Interaction Methods ---
    def gravitational_force(self, obj1: QuantumObject, obj2: QuantumObject, distance_si: float) -> Quantity:
        r_nat = distance_si / self.unit_system.l_planck
        m1_nat = obj1.rest_mass_natural if isinstance(obj1, MassiveObject) else 0.0
        m2_nat = obj2.rest_mass_natural if isinstance(obj2, MassiveObject) else 0.0
        F_nat = self.physics.gravitational_force(m1_nat, m2_nat, r_nat)
        return Quantity(F_nat * self.unit_system.F_planck, "N")
        
    def coulomb_force(self, obj1: QuantumObject, obj2: QuantumObject, distance_si: float) -> Quantity:
        r_nat = distance_si / self.unit_system.l_planck
        F_nat = self.physics.coulomb_force(obj1.charge_state, obj2.charge_state, r_nat, self.alpha)
        return Quantity(F_nat * self.unit_system.F_planck, "N")

# ============================================================================
# EXAMPLE USAGE - Demonstrating the correct separation of concerns
# ============================================================================

if __name__ == "__main__":
    api = PhysicsAPI()
    
    print("PHYSICS API - FINAL, CONCEPTUALLY PURE ARCHITECTURE")
    print("="*70)
    
    # Step 1: Create a pure, unit-less data object
    electron_obj = api.create_object("electron")
    print(f"\n1. Created a pure data object:")
    print(f"   {electron_obj}")
    print(f"   This object knows nothing about Joules, meters, or seconds.")
    
    # Step 2: Use the API as a "Presenter" to view its properties in SI units
    print("\n2. Use the API to 'present' the object's properties:")
    print("-" * 70)
    print(f"   Rest Mass:   {api.get_rest_mass(electron_obj)}")
    print(f"   Total Energy (at rest): {api.get_total_energy(electron_obj)}")
    print(f"   Velocity (at rest):     {api.get_velocity(electron_obj)}")
    
    # Example with a moving particle
    print("\n3. Relativistic Electron at 0.8c:")
    print("-" * 70)
    beta = 0.8
    # We calculate the required natural momentum to create the object
    m_nat_e = PARTICLE_ZOO["electron"].rest_mass_natural
    p_nat_e = m_nat_e * beta / math.sqrt(1 - beta**2)
    p_si_e = p_nat_e * SI.p_planck
    electron_moving_obj = api.create_object("electron", momentum_si=p_si_e)
    
    print(f"   Created: {electron_moving_obj}")
    # Now present its properties using the API
    print(f"   Total Energy:  {api.get_total_energy(electron_moving_obj)}")
    print(f"   Momentum:    {api.get_momentum(electron_moving_obj)}")
    print(f"   Velocity:    {api.get_velocity(electron_moving_obj)}")
    
    # Example of an interaction
    print("\n4. Interaction between two pure objects:")
    print("-" * 70)
    proton_obj = api.create_object("proton")
    bohr_radius = 5.29e-11 # meters
    # The API takes the pure objects and calculates the force, returning a Quantity
    force_c = api.coulomb_force(proton_obj, electron_obj, bohr_radius)
    print(f"   Force between {proton_obj.name} and {electron_obj.name}: {force_c}")


# Example 5: Photon Velocity Demonstration
    print("\n5. Photon Velocity Demonstration:")
    print("-" * 70)


    # A photon has non-zero momentum
    # We'll use the momentum of a typical green light photon.
    p_photon_si = SI.h / 550e-9 
    moving_photon = api.create_object("photon", momentum_si=p_photon_si)
    print(f"\n   Created a photon with non-zero momentum: {moving_photon}")
    velocity_moving = api.get_velocity(moving_photon)
    print(f"   → Velocity of moving photon:        {velocity_moving}")
    print(f"   (This is the value of c, as expected by the physics.)")



    print("\n" + "="*70)
    print("NOTE: The architecture is now correct.")
    print("      - Particles are pure data objects, ignorant of units.")
    print("      - The API is the sole Presenter, handling all unit conversions.")
    print("      The separation of concerns is complete and rigorous.")
    print("="*70)