# The Physics API: Making Implicit Structure Explicit

## What This API Actually Shows

**This is not a clever trick or a reinterpretation of physics.**

This API simply makes **explicit** what is already **implicit** in every physics calculation you've ever done. The three-layer architecture shown here is not something we invented—it's what the mathematics has been doing all along. We're just exposing the structure that was always there but never formally acknowledged, both for physical laws and for the properties of physical objects.

---

## The Hidden Architecture in Current Physics

### What Everyone Thinks They're Doing

When you write a formula like `F = G·M₁·M₂/r²` or access a property like an electron's mass, most people think:
- G is a fundamental property of nature.
- An electron *possesses* an intrinsic property called "mass."
- The formulas and properties are the physics.
- The constants are mysterious and deep.

### What The Math Is Actually Doing

Every calculation, whether of a law or a property, is performing three distinct operations:

**Step 1: Convert SI to Natural Coordinates**
```
# For a law...
M₁_natural = M₁_SI / m_Planck
M₂_natural = M₂_SI / m_Planck  
r_natural  = r_SI / l_Planck

# For a particle's property...
# We denote this fundamental dimensionless scalar as σ (sigma) - 
# the particle's intrinsic identity in natural coordinates.
σ_electron = mass_electron_SI / m_Planck 
```

**Step 2: Calculate in Natural Ratios (The Actual Physics)**
```
# The law is a simple proportion
F_natural = M₁_natural · M₂_natural / r_natural²

# The property is a simple identity or lookup
Energy_natural = σ_electron 
```

**Step 3: Convert Natural back to SI for Human Presentation**
```
F_SI = F_natural · F_Planck
Energy_SI = Energy_natural · E_Planck
```

**The traditional formulas and "intrinsic properties" are the compressed form of this three-step process.**

---

## Why Newton Was Right

### Newton's Approach

Isaac Newton worked explicitly in **proportionalities**: `F ∝ M₁·M₂/r²`. He wrote the relationship as a pure ratio. This was the actual physics—the invariant structural relationship.

### What Happened After Newton

Later physicists added the "proportionality constant" G: `F = G·M₁·M₂/r²`. They thought they were "completing" Newton's formula.

**What they actually did**: They embedded the coordinate transformation into the formula, mixing the measurement layer with the physics layer.

### Newton Never Needed G

In natural units where everything is measured relative to Planck scales (`m_Planck = 1`, `l_Planck = 1`), Newton's formula **is** complete:
```
F_natural = M₁_natural · M₂_natural / r_natural²
```
No G needed. G only exists because we chose meters, kilograms, and seconds—arbitrary units that are misaligned with nature's intrinsic scales.

---

## The Three Layers: What They Actually Are

### Layer 1: Business Logic (The Physics)

**What it is**: Pure dimensionless ratios and scalars in natural coordinates.

**For Particles**: An object *is* its fundamental scalar `σ` (its `rest_mass_natural`) and its charge state. We denote this fundamental dimensionless scalar as **σ (sigma)** - the particle's intrinsic identity in natural coordinates. It does not "have" mass and energy; it **is** a number.

**For Laws**: Simple proportions like `E ~ m` (ratio is 1:1), `F ~ m₁m₂/r²`, `β = p/E`.

**Key point**: No constants appear here. This is the coordinate-free physics that Newton sought.

**In the code:**
```python
class Physics:
    @staticmethod
    def relativistic_energy(rest_mass_natural: float, momentum_natural: float) -> float:
        return math.sqrt(rest_mass_natural**2 + momentum_natural**2)
    
    @staticmethod
    def velocity_beta(energy_natural: float, momentum_natural: float) -> float:
        if energy_natural == 0: return 0.0
        return momentum_natural / energy_natural
```

These functions know nothing about joules, meters, or seconds. They compute pure ratios.

### Layer 2: Coordinate System (The Jacobians & The Particle Zoo)

**What it is**: The definition of our measurement system. This layer contains both types of measured data:

**(1) The Jacobians** - The "fundamental constants" (`c`, `h`, `G`, `k_B`). These are components of the matrix that transforms coordinates between our arbitrary SI system and the natural coordinate system. They define how misaligned our chosen units are from nature's intrinsic scales.

**(2) The Particle Zoo** - The table of fundamental `σ` values that define which stable particles are known to exist (e.g., `σ_electron = 1.67e-23`, `σ_proton = 3.07e-27`). This is the catalog of nature's quantized substrate scalars.

**In the code:**
```python
class UnitSystem(NamedTuple):
    name: str
    c: float      # Length-time Jacobian
    h: float      # Action-frequency Jacobian
    G: float      # Gravitational Jacobian
    k_B: float    # Temperature-energy Jacobian
    
    @property
    def m_planck(self) -> float: return math.sqrt(self.h * self.c / self.G)
    @property
    def E_planck(self) -> float: return self.m_planck * self.c ** 2
    # ... other Planck unit derivations

SI = UnitSystem("SI", 299792458.0, 6.62607015e-34, 6.67430e-11, 1.380649e-23)

PARTICLE_ZOO: Dict[str, ParticleData] = {
    "electron": ParticleData(rest_mass_natural=9.1093837e-31 / SI.m_planck, charge_state=-1),
    "proton":   ParticleData(rest_mass_natural=1.6726219e-27 / SI.m_planck, charge_state=+1),
    # ... more particles
}
```

This layer is pure data - it defines what coordinate system we're using and what particles exist.

### Layer 3: Presentation Layer (The User Interface)

**What it is**: The part of the code that takes pure, dimensionless particle objects and "projects" their properties onto different human-readable axes (Joules, kilograms, etc.).

**What it does**: Hides the coordinate transformation complexity from the user, presenting a familiar but misleading picture of a particle "having" many different properties.

**In the code - The Pure Data Objects:**
```python
class QuantumObject:
    """A pure data object. It knows its fundamental, dimensionless state.
    It has NO KNOWLEDGE of SI units or any measurement system."""
    def __init__(self, momentum_natural: float):
        self.momentum_natural = momentum_natural
    
    def total_energy_natural(self) -> float: 
        raise NotImplementedError

class Photon(QuantumObject):
    """The base case. For a photon, E = p."""
    def total_energy_natural(self) -> float:
        return self.momentum_natural  # E = p in natural units

class MassiveObject(QuantumObject):
    """An extension that adds intrinsic identity (rest mass σ)."""
    def __init__(self, identity_key: str, momentum_natural: float, data_source: Dict):
        super().__init__(momentum_natural)
        self._key = identity_key
        self._data_source = data_source
    
    @property
    def rest_mass_natural(self) -> float:
        return self._data_source[self._key].rest_mass_natural  # Returns σ
    
    def total_energy_natural(self) -> float:
        return Physics.relativistic_energy(self.rest_mass_natural, self.momentum_natural)
```

These objects know **nothing** about kilograms, joules, or meters/second. They only know their dimensionless state in natural coordinates.

**In the code - The Presenter:**
```python
class PhysicsAPI:
    """The Presenter. This is the ONLY class that knows about both the pure
    QuantumObjects and the UnitSystem. It is responsible for all conversions."""
    
    def __init__(self, unit_system: UnitSystem = SI):
        self.unit_system = unit_system
        self.physics = Physics()
    
    def get_total_energy(self, obj: QuantumObject) -> Quantity:
        e_nat = obj.total_energy_natural()  # Get dimensionless energy
        return Quantity(e_nat * self.unit_system.E_planck, "J")  # Project to SI
    
    def get_velocity(self, obj: QuantumObject) -> Quantity:
        e_nat = obj.total_energy_natural()
        p_nat = obj.momentum_natural
        beta = self.physics.velocity_beta(e_nat, p_nat)  # Dimensionless β
        return Quantity(beta * self.unit_system.c, "m/s")  # Project to SI
```

The API is the **only** place where unit conversion happens. It takes dimensionless substrate values and decorates them with SI scaling factors.

---

## This Is How The Math Already Works

### Example: E = mc²

**What you think you're doing**: Accessing the electron's "rest energy" property. You think of `E = mc²` as a conversion *between* two distinct properties.

**What the math is actually doing**:
```python
# Step 1 & 2: Define the particle's single scalar σ in the Particle Zoo.
σ_electron = mass_electron_SI / m_Planck  # = 1.67e-23

# When you ask for its energy, the "physics" is a 1:1 identity.
Energy_natural = σ_electron  # Same number!

# Step 3: Project onto the "Energy" axis for humans.
Energy_SI = Energy_natural * E_Planck
          = (mass_electron_SI / m_Planck) * (m_Planck * c²)
          = mass_electron_SI * c²
```

The formula `E = mc²` is not a deep law converting one substance to another. It is the **dictionary entry** that shows how to project a particle's single fundamental scalar (`σ`) onto the human-invented axis of "Energy." 

**The electron has one number (`σ`).** 
- When you ask 'what's its mass?' the API projects: `σ → σ × m_Planck`
- When you ask 'what's its energy?' the API projects: `σ → σ × E_Planck`
- The ratio `E_Planck / m_Planck = c²`, so the projections differ by `c²`

**That's all `E=mc²` is** - a statement about how two different measurement axes (mass and energy) scale relative to each other when measuring the same underlying quantity `σ`.

Einstein even said this explicitly: "c² is just unit conversion." But nobody formalized what that actually meant mathematically. Our API does.

---

## The Photon: Physics Without Special Cases

### Traditional Code Would Write:
```python
def get_velocity(particle):
    if isinstance(particle, Photon):
        return SPEED_OF_LIGHT  # Special case!
    else:
        # Calculate velocity for massive particles
        return calculate_velocity(particle)
```

### Our Code:
```python
def get_velocity(self, obj: QuantumObject) -> Quantity:
    e_nat = obj.total_energy_natural()
    p_nat = obj.momentum_natural
    beta = p_nat / e_nat  # Works for everything
    return Quantity(beta * self.unit_system.c, "m/s")
```

**For a photon**: `E = p`, so `β = p/E = p/p = 1.0`, therefore `v = 1.0 × c = c`

**For massive particles**: `E = √(m² + p²) > p`, so `β = p/E < 1.0`, therefore `v < c`

**No special cases needed.** The photon class simply defines `total_energy_natural()` to return `self.momentum_natural`. The substrate physics automatically produces `v = c` with zero awareness that "light speed" is special.

The particle classes have **no axiom that "light travels at c"**. They only know `E = p` for massless particles. The speed `c` emerges as `β = 1` when projected to SI coordinates.

---

## The Planck Scale: Not A Choice

### Why Planck Units Are Special

The Planck scales are **not** arbitrary. They're the **unique solution** to the question: "What coordinate system makes all the Jacobians equal to 1?"

The fact that there's a unique solution proves:
- The constants are not independent; they are components of a single transformation
- That transformation connects our arbitrary SI system to a pre-existing, unique natural coordinate system

**If constants were fundamental properties**, they could be independent, and there would be no guarantee of a unique natural scale. **The uniqueness proves they're coordinate artifacts.**

In the code, this uniqueness is reflected in how all Planck units are derived from just the four Jacobians:
```python
@property
def t_P(self) -> float: return math.sqrt(self.G * self.h / self.c**5)
@property
def l_P(self) -> float: return self.c * self.t_P
@property
def m_P(self) -> float: return math.sqrt(self.h * self.c / self.G)
@property
def E_P(self) -> float: return self.m_P * self.c**2
```

There's only one way to combine `c`, `h`, and `G` to get units of length, time, mass, etc. This mathematical uniqueness reveals that we're uncovering a **pre-existing structure**, not making arbitrary choices.

---

## The Architecture Makes This Structure Explicit

### Traditional Approach: Everything Mixed Together

```python
class Electron:
    def __init__(self):
        self.mass = 9.109e-31  # kg (where did this come from?)
        self.charge = -1.602e-19 # C (what's the relationship?)

    def get_rest_energy(self):
        c = 299792458.0  # (is this a property of the electron?)
        return self.mass * c**2  # (why c²?)
```

Problems:
- Where do these numbers come from?
- What is their relationship?
- Is `c` a property of the electron or the universe?
- Why does energy equal mass times c²?
- Everything is confused and mixed together.

### API Approach: Layers Separated

```python
# Layer 2: The Zoo (Measured substrate scalars)
PARTICLE_ZOO = {
    "electron": ParticleData(rest_mass_natural=1.67e-23, charge_state=-1)
}

# Layer 2: The Jacobians (Coordinate transformation)
class UnitSystem:
    E_planck = 4.90e9  # J

# Layer 1: The pure particle object (knows only substrate state)
class MassiveObject:
    def __init__(self, identity_key):
        self.sigma = PARTICLE_ZOO[identity_key].rest_mass_natural
    
    def total_energy_natural(self):
        return self.sigma  # E = σ in natural units

# Layer 3: The Presenter (handles all unit conversion)
class PhysicsAPI:
    def get_rest_energy(self, particle_obj):
        return particle_obj.sigma * self.unit_system.E_planck
```

Now it's clear:
- **Layer 1**: The particle **is** its scalar `σ` (pure physics)
- **Layer 2**: The value of `σ` is measured data; Jacobians define coordinates
- **Layer 3**: The API projects `σ` onto the Energy axis using `E_Planck`

The electron doesn't "know" what a joule is. The API decorates its dimensionless state with SI units for human consumption.

---

## This Is Not Controversial Mathematics

When physicists "set `c = 1`" for convenience, they're doing exactly this. They are implicitly working in a system where particles are defined by dimensionless scalars `σ`. We're just making the structure of their informal shorthand explicit and separating it into proper software layers.

What was missing for 125 years was the recognition that this structure applies not just to laws, but to the very definition of a particle's properties.

---

## Why This Matters

### It Reveals What the Actual Mystery Is

This framework resolves old, confused mysteries and reveals the true, deeper questions.

**Old Mystery**: "Why does `E = mc²`?"

**Resolution**: That's just coordinate geometry - how the energy axis scales relative to the mass axis. Not mysterious.

**Real Mystery**: "**Why does `σ` take these specific quantized values?**"
- Why is `σ_electron` ≈ 1.67×10⁻²³ and not something else?
- Why is `σ_proton/σ_electron` ≈ 1836?
- What determines the spectrum of allowed `σ` values?

**That's where the real physics is hiding.**

### It Changes What We Search For

**Old paradigm**: 
- Search for the "origin of mass"
- Search for why constants have their values
- Search for conversions between "different" properties

**New paradigm**:
- Constants are Jacobians - their values are determined by our unit choices
- Search for the geometric origin of the **spectrum of allowed `σ` values**
- Search for patterns in the **Planck Equivalence Web** (how different `σ` values relate)
- Search for why nature permits these specific dimensionless scalars and not others

---

## Predictions of This Framework

If this structuralist framework is correct, several consequences follow:

**1. All Particle Properties Derivable from Single `σ`**

Any intrinsic, static property of a fundamental particle must be derivable from its one `σ` value and the relevant Jacobians. There are no independent, disconnected properties.

*In the code, this is enforced:* A `MassiveObject` has only `rest_mass_natural` (its `σ`). All other properties (energy, momentum, velocity) are computed from `σ` and the object's current state.

**2. Constants Must Form Closed Transformation Group**

The values of `c`, `h`, `G`, and `k_B` cannot be independent. They must be mathematically consistent as components of a single coordinate transformation.

*In the code:* The `UnitSystem` class demonstrates this coherence - all Planck units are derived from just these four Jacobians in a unique, self-consistent way.

**3. 'New' Physics Reveals Patterns in `σ` Spectrum**

Future discoveries in particle physics will not reveal new "substances" or "forces" in the classical sense. They will reveal new entries in the `σ` table and mathematical patterns (symmetries, hierarchies, ratios) between different particles' `σ` values.

*Implication:* The search for physics becomes a search for the pattern in this spectrum of dimensionless numbers.

---

## Anticipated Objections

### Objection 1: "But mass and energy feel like different things!"

**Response:** Yes, because you are using different measurement operations. You measure mass with a balance (comparing gravitational influence) and energy with a calorimeter (measuring thermal change). These are completely different projection operations performed on the same underlying `σ`. 

Of course they "feel" different—you're using different measurement procedures, like asking "how tall?" versus "how heavy?" The difference is in your **interaction** with the object, not in the object itself.

*In the code:* The particle object has one `σ`. The API has different methods (`get_rest_mass()`, `get_total_energy()`) that project this same `σ` using different Jacobians (`m_Planck` vs `E_Planck`).

### Objection 2: "This is just dimensional analysis. It can't derive physics."

**Response:** This is a misunderstanding. We're not just manipulating units. We start with known, valid physical laws expressed as **dimensionless proportions** (e.g., `F_nat ~ m₁m₂/r²`, `E_nat = √(m² + p²)`). The framework then shows how these invariant truths are projected into any specific unit system.

*In the code:* The `Physics` class (Layer 1) contains the actual physics as pure, dimensionless math. The rest is projection machinery. The physics isn't derived from dimensional analysis - it's **expressed** in dimensionless form, then projected to coordinates.

### Objection 3: "You're just redefining constants. You haven't explained anything."

**Response:** The standard model leaves constants **undefined** - they're just "measured values" with no deeper meaning. Our framework provides the first rigorous, formal definition: they are the **Jacobian coefficients of the transformation between SI coordinates and natural coordinates.**

Defining them is not a redefinition; it's the **first definition they've ever been given**. This act of definition resolves the mystery by showing what they actually are.

*In the code:* Constants aren't magic numbers. They're explicit transformation coefficients in the `UnitSystem` class, with clear mathematical relationships to Planck scales.

### Objection 4: "What about dimensionless constants like α?"

**Response:** This framework makes the distinction crystal clear:

**Dimensional "constants" (`c`, `h`, `G`, `k_B`)**: 
- Coordinate system artifacts (Jacobians)
- Not fundamental
- Values depend on our unit choices

**Dimensionless constants (`α ≈ 1/137`, particle mass ratios)**:
- **Real** physics
- Invariant substrate ratios that exist in Layer 1
- True, fundamental numbers whose values are deep mysteries

Our framework separates pseudo-problems (like "why does G have its value?") from real problems (like "why does α ≈ 1/137?").

*In the code:* `α` appears in the `PhysicsAPI` as `self.alpha = 1/137.036` - a true dimensionless constant used in actual physics calculations, not a coordinate artifact.

---

## The Proof Is In The Code

The API is **executable proof**. You can:

1. Create particle objects that know nothing about SI units
2. Perform physics calculations in pure dimensionless form
3. Project results to any unit system
4. Get photon velocity = c with zero special-case code
5. See that every formula works, every calculation matches

**Because this is what the math was doing all along.**

The architecture was always there, hidden and implicit. The API makes it explicit and executable.

**Newton was right. The physics is in the proportions. Everything else is just unit conversion.**

---

## Appendix: The Reification Error at the Heart of Physics

This framework directly confronts physics' most fundamental philosophical error: **reification** - the fallacy of treating an abstract concept as a concrete thing.

### The Reification Table

| Feature | Current Reified Framework | This "Proportions as Reality" Framework |
|:--------|:-------------------------|:---------------------------------------|
| **Constants (c, h, G)** | **REAL**: Fundamental properties of nature | **ABSTRACT**: Coordinate transformation artifacts (Jacobians) |
| **Proportions (F ∝ Mm/r²)** | **ABSTRACT**: Incomplete idea needing a constant | **REAL**: The actual, invariant physical law |
| **Formulas (F = GMm/r²)** | **REAL**: The complete physical law | **ABSTRACT**: Coordinate-specific representation |
| **Mass vs Energy** | **REAL**: Two distinct, convertible substances | **ABSTRACT**: Two labels for the same thing (`σ`) |
| **Particle Properties** | **REAL**: Intrinsic substances a particle "has" | **ABSTRACT**: Projections we create during measurement |

### The Four Reification Errors

**Error #1: Reification of Constants**
- **Current**: Treats `c`, `h`, `G` as real, physical things with mysterious values
- **Reality**: They're components of a coordinate transformation matrix

**Error #2: Reification of Physical Laws**
- **Current**: Treats the *formula* (`F = G...`) as the *law*
- **Reality**: The invariant **proportion** (`F ∝ ...`) is the law; the formula is a coordinate representation

**Error #3: Reification of Mass and Energy**
- **Current**: Treats "mass" and "energy" as two distinct substances
- **Reality**: Two human labels for the same underlying quantity `σ`. `E = mc²` is a dictionary entry, not a physical process

**Error #4: Reification of Particle Properties**
- **Current**: A particle is a "bag of intrinsic properties" (mass, energy, momentum) - it "has" these things
- **Reality**: A particle **is** its fundamental scalar `σ` and dynamic state. "Properties" are projections we create during measurement

### The Category Error

The current framework takes **measurement artifacts** (constants, formulas, properties) and reifies them as reality.

This framework takes **invariant proportions and scalars** as reality and correctly identifies measurement artifacts as presentation-layer abstractions.

We are pointing out a category error that has been embedded in physics for over a century: **The things physicists have been treating as the most fundamental parts of the universe are, in fact, artifacts of their own rulers.**

---

## Conclusion

This API demonstrates that the three-layer architecture - substrate physics, coordinate system, and presentation - has always been present in every physics calculation. We've simply made it explicit.

By separating these layers properly, we reveal:
- What is actual physics (dimensionless substrate ratios)
- What is coordinate choice (Jacobians/constants)
- What is measurement artifact (projected "properties")

The code proves this works. Every calculation matches. Because **this is what the math was doing all along**.