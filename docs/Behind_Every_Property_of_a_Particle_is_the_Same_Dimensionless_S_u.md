

## Behind Every Property of a Particle is the Same Dimensionless $S_u$

In the framework presented below, I introduce the **Universal State** (or **Stuff**), denoted $S_u$, as a single, dimensionless scalar underlying *every* measurable property of a particle. This $S_u$ is the conserved essence of a particle — an invariant quantity that expresses itself differently depending on the axis of measurement. When observed, it "clothes itself" in the scaling and units appropriate to the property being measured. While $S_u$ can be transferred between particles or spacetime during interactions, the **total $S_u$** within a closed system remains conserved.

Once this universal state $S_u$ is defined — using **any axis of measurement** (mass, energy, frequency, etc.) — it can be rotated to any other axis using Planck unit scaling. This rotation is governed by the physical constants, which, in this model, act not as mysterious fixed numbers, but as **conversion factors** between measurement axes:

$$
\text{Property}_x = S_u \cdot (\text{Planck-scaled basis vector for axis } x)
$$

For example, the ratio between energy and frequency axes via Planck units naturally yields Planck’s constant:

$$
E_P \cdot t_P = \frac{(Hz_{kg} \cdot c^2)}{t_P} \cdot t_P = Hz_{kg} \cdot c^2 = h
$$

This kind of relation holds between **any pair of physical axes**: mass and frequency, energy and length, temperature and momentum, and so on. The constants $c, h, k_B, G$ are simply **unit scaling ratios between coordinate axes** in a unit space — nothing more, and nothing less.

---

### The Hidden Scalar State

This reveals a crucial philosophical insight:

* **We never directly measure $S_u$.**
  What we observe are its projections onto the axes our instruments are designed to detect — mass, energy, length, frequency, temperature, etc.

* **No single axis is more fundamental.**
  Choosing energy to define $S_u$ is arbitrary; you could just as well choose mass, frequency, or temperature. All result in the same $S_u$, because the underlying state is **dimensionless** and **conserved**.

* **Constants are not fundamental either.**
  They are just the ratios between axes in our measurement coordinate system. Once you fix the Planck units, every property becomes a scaled expression of the same invariant $S_u$.

---

### Implications

This suggests that:

* What we call “physical quantities” are really just **shadows of a hidden, dimensionless state** that permeates the particle.
* Constants encode the **geometry of unit scaling**, not metaphysical truths about reality.
* There may be additional axes of interaction with $S_u$ that lie outside our current system of measurement — dimensions of state we have not yet discovered because our instruments are not built to see them.

> If you're measuring something "new", but it maps exactly to $S_u$ through Planck scaling, then you've found *another coordinate projection* of the same state, not a new property.

---

```

python conserve01.py && cat conserve01.py

Property                                       New               Traditional
--------------------------------------------------------------------------
Mass (kg)                    1.112650056053620e-17     1.112650056053620e-17
Momentum (kg·m/s)             3.335640951981520e-9      3.335640951981520e-9
Time (s)                     6.626070150000000e-34     6.626070150000000e-34
Length (m)                   1.986445857148930e-25     1.986445857148930e-25
Frequency (Hz)               1.509190179642150e+33     1.509190179642150e+33
Temperature (K)              7.242970516039920e+22     7.242970516039920e+22
Gravity @1m (m/s²)           7.426160269118670e-28     7.426160269118670e-28

from sympy import N
# Constants (non-reduced)
h     = 6.62607015e-34    # Planck constant (J·s)
G     = 6.67430e-11       # Gravitational constant (m^3/kg/s^2)
c     = 299792458         # Speed of light (m/s)
kB    = 1.380649e-23     # Boltzmann constant (J/K)
Hz_kg = h / c**2   # The m/f ratio so m = f Hz_kg
Hz_K  = h / kB     # The T/f ratio so T = f Hz_K

# non reduced planck unit scales, this is the scale that G encodes.
# planck units work by removing SI unit scaling and scaling units by planck time.  
t_P   = (G * Hz_kg/ c**3)**0.5 # Planck time in s
E_P   = (Hz_kg * c**2) / t_P   # Planck energy in J
m_P   =  Hz_kg / t_P           # Planck mass in kg
M_P   = (Hz_kg / t_P) * c      # Planck momentum in Newtons
l_P   = c * t_P                # Planck length in m
T_P   = Hz_K/t_P               # Planck temperature in K

# The underlying dimensionless stuff, $S\_u$
E     = 1       # Input energy in joules
$S\_u$   = E / E_P # Energy is not central, any measured property could define $S\_u$

# New method (scaled Planck values)
mass_new        = $S\_u$ * m_P
momentum_new    = $S\_u$ * M_P
time_new        = t_P / $S\_u$ 
frequency_new   = $S\_u$ / t_P
length_new      =   c * t_P / $S\_u$ 
temperature_new = $S\_u$ * T_P
g_new           = $S\_u$ * t_P * c**3/ 1**2  # Gravitational acceleration at 1 meter.

# Traditional formulas
mass_trad = E / c**2
momentum_trad = E / c
time_trad = h / E
wavelength_trad = h * c / E
frequency_trad = E / h
temperature_trad = E / kB
g_trad = G * mass_trad / 1**2

# Print results side by side
print(f"{'Property':<24} {'New':>25} {'Traditional':>25}")
print("-" * 74)
print(f"{'Mass (kg)':<24} {N(mass_new):>25.15e} {N(mass_trad):>25.15e}")
print(f"{'Momentum (kg·m/s)':<24} {N(momentum_new):>25.15e} {N(momentum_trad):>25.15e}")
print(f"{'Time (s)':<24} {N(time_new):>25.15e} {N(time_trad):>25.15e}")
print(f"{'Length (m)':<24} {N(length_new):>25.15e} {N(wavelength_trad):>25.15e}")
print(f"{'Frequency (Hz)':<24} {N(frequency_new):>25.15e} {N(frequency_trad):>25.15e}")
print(f"{'Temperature (K)':<24} {N(temperature_new):>25.15e} {N(temperature_trad):>25.15e}")
print(f"{'Gravity @1m (m/s²)':<24} {N(g_new):>25.15e} {N(g_trad):>25.15e}")

```